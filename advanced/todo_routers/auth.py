from fastapi import APIRouter, status, HTTPException, Header, Depends
from fastapi.responses import JSONResponse
from advanced.data import USERS_DATA, USER
from advanced.todo_routers.user import hash_password
from jose import jwt, JWTError
from datetime import datetime, timedelta

user_auth = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
# this prefix and tags can be used at the time of including this route to the FastAPI app

JWT_SECRET_KEY = "1dweinwrgrqpo3oj3094ioqfne5yo43#@*&^$*"
JWT_ALGO = "HS256"


@user_auth.post('/user', status_code=status.HTTP_200_OK)
async def authenticate_user_and_get_token(login_details: USER):
    username = login_details.username
    given_pass = login_details.password
    hash_pass = hash_password(given_pass)
    if username not in list(USERS_DATA.keys()) or USERS_DATA[username] != hash_pass:
        return JSONResponse(status_code=403, content="Invalid username or password")

    return {"token": generate_token(username)}


def generate_token(username):
    payload = {
        "user": username
    }
    expire = datetime.utcnow() + timedelta(minutes=1)
    payload.update({"exp": expire})

    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGO)


def validate_token(token: str):
    try:
        # we don't need to chk for timestamp it will be automatically calculated and expire the token
        jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGO])
        return {"status": "Token is valid"}
    except JWTError as j:
        print(j)
        if "Signature has expired" in str(j):
            raise HTTPException(status_code=401, detail={"status": "Token Expired"})
        raise HTTPException(status_code=403)


@user_auth.post('/token/validate', status_code=status.HTTP_200_OK)
def validate_token_status(x_auth_token: str = Header()):
    return validate_token(x_auth_token)

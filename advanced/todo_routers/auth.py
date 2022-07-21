from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from advanced.data import USERS_DATA, USER
from advanced.todo_routers.user import hash_password

user_auth = APIRouter()


@user_auth.post('/user/login', status_code=status.HTTP_200_OK)
async def authenticate_user(login_details: USER):
    username = login_details.username
    given_pass = login_details.password
    hash_pass = hash_password(given_pass)
    if username not in list(USERS_DATA.keys()) or USERS_DATA[username] != hash_pass:
        return JSONResponse(status_code=403, content="Invalid username or password")

    return {"token": "ur_token"}

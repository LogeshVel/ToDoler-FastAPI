from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from advanced.data import USERS_DATA, USER
import bcrypt

user = APIRouter()

salt = bcrypt.gensalt()


def hash_password(password):
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, salt)


@user.get('/user/all')
async def list_all_users():
    return {"users": list(USERS_DATA.keys())}


@user.post('/user/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_details: USER):
    usr = user_details.username
    u = {usr: hash_password(user_details.password)}
    if usr in USERS_DATA:
        return JSONResponse(status_code=406,
                            content=f"Username - {usr} already exists"
                            )
    USERS_DATA.update(u)
    return {"status": "Successfully created User"}

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from advanced.custom_exceptions import NegativeNumberException
from advanced.todo_routers.advanced_api import todo
from advanced.todo_routers.user import user
from advanced.todo_routers.auth import user_auth

todo_app = FastAPI()
todo_app.include_router(user)
todo_app.include_router(user_auth)
todo_app.include_router(todo)
# We can give the prefix and tags to the .include_router() function

@todo_app.exception_handler(NegativeNumberException)
async def negative_id_exception(request: Request, exc: NegativeNumberException):
    print(request)
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! Found unexpected negative todo id : {exc.negative_id}"},
    )

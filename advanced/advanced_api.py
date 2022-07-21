from fastapi import FastAPI, Request, status, Form, Header
from fastapi.responses import JSONResponse

from advanced.todo_routers.auth import user_auth, validate_token
from advanced.custom_exceptions import NegativeNumberException
from advanced.data import ToDo_List, Priority, Tag, TODO, ToDoName
from advanced.todo_routers.user import user
from advanced.workers import AdvancedTodoWorkers

todo = FastAPI()
todo.include_router(user)
todo.include_router(user_auth)


@todo.exception_handler(NegativeNumberException)
async def negative_id_exception(request: Request, exc: NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! Found unexpected negative todo id : {exc.negative_id}"},
    )


@todo.get('/')
async def root_page():
    return {"status": "Success", "description": "Welcome to the root page"}


@todo.get('/todo/list')
async def list_todos(x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": ToDo_List}


@todo.get('/todo/priority/{todo_priority}')
async def list_todo_for_given_priority(todo_priority: Priority, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": AdvancedTodoWorkers.get_todo_item(priority=todo_priority)}


@todo.get('/todo/tag/{todo_tag}')
async def list_todo_for_given_priority(todo_tag: Tag, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": AdvancedTodoWorkers.get_todo_item(tag=todo_tag)}


@todo.get('/todo/filter')
async def filter_todo(priority: Priority, tag: Tag, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": AdvancedTodoWorkers.get_todo_item(priority=priority, tag=tag)}


@todo.post("/todo/create", status_code=status.HTTP_201_CREATED)
async def create_todo(payload: TODO, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"id": AdvancedTodoWorkers.add_todo_item(payload), "status": "Success"}


@todo.get('/todo/{todo_id}')
async def get_todo(todo_id: int, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.get_todo_by_id(todo_id)


# using response model
@todo.get('/todo/name/{todo_id}', response_model=ToDoName)
async def get_todo_name(todo_id: int, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.get_todo_by_id(todo_id)


@todo.put('/todo/{todo_id}')
async def update_todo(todo_id: int, payload: TODO, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.update_todo_item(payload, todo_id)


@todo.patch('/todo/{todo_id}')
async def patch_todo(todo_id: int, todo_name: str = None, priority: Priority = None, tag: Tag = None, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.patch_todo_item(todo_id=todo_id, todo_name=todo_name, priority=priority, tag=tag)


@todo.delete('/todo/{todo_id}')
async def delete_todo(todo_id: int, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.delete_todo_item(todo_id)

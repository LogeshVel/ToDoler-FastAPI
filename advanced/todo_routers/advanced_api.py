from fastapi import APIRouter, status, Header

from advanced.todo_routers.auth import validate_token
from advanced.data import ToDo_List, Priority, Tag, TODO, ToDoName
from advanced.workers import AdvancedTodoWorkers

todo = APIRouter(
    prefix="/todo",
    tags=["todos"]
)


@todo.get('/list')
async def list_todos(x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": ToDo_List}


@todo.get('/priority/{todo_priority}')
async def list_todo_for_given_priority(todo_priority: Priority, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": AdvancedTodoWorkers.get_todo_item(priority=todo_priority)}


@todo.get('/tag/{todo_tag}')
async def list_todo_for_given_priority(todo_tag: Tag, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": AdvancedTodoWorkers.get_todo_item(tag=todo_tag)}


@todo.get('/filter')
async def filter_todo(priority: Priority, tag: Tag, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"todo_list": AdvancedTodoWorkers.get_todo_item(priority=priority, tag=tag)}


@todo.post("/create", status_code=status.HTTP_201_CREATED)
async def create_todo(payload: TODO, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return {"id": AdvancedTodoWorkers.add_todo_item(payload), "status": "Success"}


@todo.get('/{todo_id}')
async def get_todo(todo_id: int, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.get_todo_by_id(todo_id)


# using response model
@todo.get('/{todo_id}/name', response_model=ToDoName)
async def get_todo_name(todo_id: int, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.get_todo_by_id(todo_id)


@todo.put('/{todo_id}')
async def update_todo(todo_id: int, payload: TODO, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.update_todo_item(payload, todo_id)


@todo.patch('/{todo_id}')
async def patch_todo(todo_id: int, todo_name: str = None, priority: Priority = None, tag: Tag = None,
                     x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.patch_todo_item(todo_id=todo_id, todo_name=todo_name, priority=priority, tag=tag)


@todo.delete('/{todo_id}')
async def delete_todo(todo_id: int, x_auth_token: str = Header()):
    validate_token(x_auth_token)
    return AdvancedTodoWorkers.delete_todo_item(todo_id)

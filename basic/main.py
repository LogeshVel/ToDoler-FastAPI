from fastapi import FastAPI
from data import ToDo_List, Priority, Tag, TODO
from workers import TodoWorkers

todo = FastAPI()


@todo.get('/')
async def root_page():
    return {"status": "Success", "description": "Welcome to the root page"}


@todo.get('/todo/list')
async def list_todos():
    return {"todo_list": ToDo_List}


@todo.get('/todo/priority/{todo_priority}')
async def list_todo_for_given_priority(todo_priority: Priority):
    return {"todo_list": TodoWorkers.get_todo_item(priority=todo_priority)}


@todo.get('/todo/tag/{todo_tag}')
async def list_todo_for_given_priority(todo_tag: Tag):
    return {"todo_list": TodoWorkers.get_todo_item(tag=todo_tag)}


@todo.get('/todo/filter')
async def filter_todo(priority: Priority, tag: Tag):
    return {"todo_list": TodoWorkers.get_todo_item(priority=priority, tag=tag)}


@todo.post("/todo/create")
async def create_todo(payload: TODO):
    return {"id": TodoWorkers.add_todo_item(payload), "status": "Success"}


@todo.get('/todo/{todo_id}')
async def get_todo(todo_id: int):
    return TodoWorkers.get_todo_by_id(todo_id)


@todo.put('/todo/{todo_id}')
async def update_todo(todo_id: int, payload: TODO):
    return TodoWorkers.update_todo_item(payload, todo_id)


@todo.patch('/todo/{todo_id}')
async def patch_todo(todo_id: int, todo_name: str = None, priority: Priority = None, tag: Tag = None):
    return TodoWorkers.patch_todo_item(todo_id=todo_id, todo_name=todo_name, priority=priority, tag=tag)


@todo.delete('/todo/{todo_id}')
async def delete_todo(todo_id: int):
    return TodoWorkers.delete_todo_item(todo_id)

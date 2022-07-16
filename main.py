from fastapi import FastAPI
from data import ToDo, Priority, Tag

todo = FastAPI()


@todo.get('/')
async def root_page():
    return {"status": "Success", "description": "Welcome to the root page"}


@todo.get('/todo/list')
async def list_todos():
    return {"todo_list": ToDo}


@todo.get('/todo/priority/{todo_priority}')
async def list_todo_for_given_priority(todo_priority: Priority):
    return_list = []
    for _todo in ToDo:
        if "priority" in _todo:
            if _todo["priority"] == todo_priority:
                return_list.append(_todo)
    return {"todo_list": return_list}


@todo.get('/todo/tag/{todo_tag}')
async def list_todo_for_given_priority(todo_tag: Tag):
    return_list = []
    for _todo in ToDo:
        if "tag" in _todo:
            if _todo["tag"] == todo_tag:
                return_list.append(_todo)
    return {"todo_list": return_list}


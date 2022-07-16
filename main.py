from fastapi import FastAPI
from data import ToDo_List, Priority, Tag, TODO

todo = FastAPI()


@todo.get('/')
async def root_page():
    return {"status": "Success", "description": "Welcome to the root page"}


@todo.get('/todo/list')
async def list_todos():
    return {"todo_list": ToDo_List}


@todo.get('/todo/priority/{todo_priority}')
async def list_todo_for_given_priority(todo_priority: Priority):
    return_list = []
    for _todo in ToDo_List:
        if "priority" in _todo:
            if _todo["priority"] == todo_priority:
                return_list.append(_todo)
    return {"todo_list": return_list}


@todo.get('/todo/tag/{todo_tag}')
async def list_todo_for_given_priority(todo_tag: Tag):
    return_list = []
    for _todo in ToDo_List:
        if "tag" in _todo:
            if _todo["tag"] == todo_tag:
                return_list.append(_todo)
    return {"todo_list": return_list}


@todo.get('/todo/filter')
async def filter_todo(priority: Priority, tag: Tag):
    return_todo_list = []
    for _todo in ToDo_List:
        if "priority" in _todo and "tag" in _todo:
            if _todo["priority"] == priority and _todo["tag"] == tag:
                return_todo_list.append(_todo)
    return {"todo_list": return_todo_list}


@todo.post("/todo/create")
async def create_todo(payload: TODO):
    last_todo_id = ToDo_List[-1]["id"]

    _todo = {
        "id": last_todo_id + 1,
        "todo_name": payload.todo_name,
        "priority": payload.priority,
        "tag": payload.tag
    }
    ToDo_List.append(_todo)
    return {"status": "Success"}

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
    return {"id": last_todo_id + 1, "status": "Success"}


@todo.put('/todo/{todo_id}')
async def update_todo(todo_id: int, payload: TODO):
    for idx, _todo in enumerate(ToDo_List):
        if todo_id == _todo.get("id"):
            _todo_update = {
                "todo_name": payload.todo_name,
                "priority": payload.priority,
                "tag": payload.tag
            }
            ToDo_List[idx] = _todo_update
            return {"status": "Success"}

    return {"status": "Failed", "Reason": f"No such Todo id {todo_id}"}


@todo.patch('/todo/patch/{todo_id}')
async def patch_todo(todo_id: int, todo_name: str = None, priority: Priority = None, tag: Tag = None):
    for _todo in ToDo_List:
        if todo_id == _todo.get("id"):
            if todo_name is not None:
                _todo["todo_name"] = todo_name
            if priority is not None:
                _todo["priority"] = priority
            if tag is not None:
                _todo["tag"] = tag
            return {"status": "Success", "description": f"Successfully patched the Todo item - {todo_id}"}
    return {"status": "Failed", "description": f"There is no such todo item with the given id - {todo_id}"}


@todo.delete('/todo/delete/{todo_id}')
async def delete_todo(todo_id: int):
    for idx, _todo in enumerate(ToDo_List):
        if todo_id == _todo.get("id"):
            del ToDo_List[idx]
            return {"status": "Success", "description": f"Successfully deleted the Todo item - {todo_id}"}
    return {"status": "Failed", "description": f"There is no such todo item with the given id - {todo_id}"}

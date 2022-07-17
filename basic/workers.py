from data import ToDo_List, Priority, Tag, TODO


def get_todo_by_id(todo_id: int):
    for _todo in ToDo_List:
        if todo_id == _todo.get("id"):
            return _todo
    return {}


def get_todo_item(priority: Priority = None, tag: Tag = None):
    return_list = []
    if priority is not None and tag is not None:
        for _todo in ToDo_List:
            if "priority" in _todo and "tag" in _todo:
                if _todo["priority"] == priority and _todo["tag"] == tag:
                    return_list.append(_todo)
        return return_list
    if priority is not None:
        for _todo in ToDo_List:
            if "priority" in _todo:
                if _todo["priority"] == priority:
                    return_list.append(_todo)
        return return_list

    if tag is not None:
        for _todo in ToDo_List:
            if "tag" in _todo:
                if _todo["tag"] == tag:
                    return_list.append(_todo)
        return return_list


def add_todo_item(payload: TODO):
    if len(ToDo_List) == 0:
        last_todo_id = 0
    else:
        last_todo_id = ToDo_List[-1]["id"]

    _todo = {
        "id": last_todo_id + 1,
        "todo_name": payload.todo_name,
        "priority": payload.priority,
        "tag": payload.tag
    }
    ToDo_List.append(_todo)

    return last_todo_id + 1


def update_todo_item(payload: TODO, todo_id: int):
    for idx, _todo in enumerate(ToDo_List):
        if todo_id == _todo.get("id"):
            _todo_update = {
                "todo_name": payload.todo_name,
                "priority": payload.priority,
                "tag": payload.tag
            }
            ToDo_List[idx] = _todo_update
            return {"status": "Success", "isError": False}
    return {"status": "Failed", "Reason": f"No such Todo id {todo_id}", "isError": True}


def patch_todo_item(todo_id: int, todo_name: str = None, priority: Priority = None, tag: Tag = None):
    for _todo in ToDo_List:
        if todo_id == _todo.get("id"):
            if todo_name is not None:
                _todo["todo_name"] = todo_name
            if priority is not None:
                _todo["priority"] = priority
            if tag is not None:
                _todo["tag"] = tag
            return {"status": "Success", "description": f"Successfully patched the Todo item - {todo_id}", "isError": False}
    return {"status": "Failed", "description": f"There is no such todo item with the given id - {todo_id}", "isError": True}


def delete_todo_item(todo_id_to_del: int):
    for idx, _todo in enumerate(ToDo_List):
        if todo_id_to_del == _todo.get("id"):
            del ToDo_List[idx]
            return {"status": "Success", "description": f"Successfully deleted the Todo item - {todo_id_to_del}", "isError": False}
    return {"status": "Failed", "description": f"There is no such todo item with the given id - {todo_id_to_del}", "isError": True}
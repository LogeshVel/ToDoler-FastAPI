from enum import Enum, IntEnum

from pydantic import BaseModel


class Tag(str, Enum):
    learn = "Learn"
    fun = "Fun"
    health = "Health"


class Priority(IntEnum):
    """
    Explicitly mention that this enum is Int type so that we could use them easily in the Path varibales
    """
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class TODO(BaseModel):
    todo_name: str
    priority: Priority
    tag: Tag


ToDo_List = [
    {
        "todo_name": "Learn Everyday",
        "priority": Priority.one,
        "tag": Tag.learn,
        "id": 1
    }
]

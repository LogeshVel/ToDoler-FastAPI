from enum import Enum


class Tag(str, Enum):
    learn = "Learn"
    fun = "Fun"
    health = "Health"


class Priority(int, Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


ToDo = [
    {
        "todo_name": "Learn Everyday",
        "priority": Priority.one,
        "tag": Tag.learn
    }
]

from enum import Enum, IntEnum
from typing import Optional

from pydantic import BaseModel, Field


class Tag(str, Enum):
    learn = "Learn"
    fun = "Fun"
    health = "Health"


class Priority(IntEnum):
    # Explicitly mention that this enum is Int type so that we could use them easily in the Path variables
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


# With some more validation by making use of the FastAPI
class TODO(BaseModel):
    todo_name: str = Field(title="ToDo name", min_length=2)
    # the min_length makes FastAPI to expect atleast 2 char length for this field from the user.
    priority: Priority
    tag: Tag
    # If we want to specify the filed that is optional then
    # from typing import Optional
    # estimated_time: Optional[str]
    # Say if we have some int field and we need to limit the values given by the user with some range then
    no_of_days: Optional[int] = Field(gt=-1, lt=101)

    # this gives the user the range of 0-100. Value within this range is allowed
    # we can also specify the example input for this class
    class Config:
        schema_extra = {
            "example": {
                "todo_name": "Your ToDO name",
                "priority": 1,
                "tag": "Learn",
                "no_of_days": 5
            }
        }


ToDo_List = [
    {
        "id": 1,
        "todo_name": "Learn Everyday",
        "priority": Priority.one,
        "tag": Tag.learn
    }
]

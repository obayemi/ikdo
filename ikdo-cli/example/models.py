from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import string
from uuid import UUID

class Level(Enum):
    """Level of a task"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class User:
    id: UUID
    username: string
    password: string

@dataclass
class List:
    owner: User
    name: string

@dataclass
class ListItem:
    created: datetime
    updated: datetime
    completed: datetime
    deadline: string
    content: datetime
    priority: Level
    difficulty: Level
    detail: string

@dataclass
class ListSharing:
    list: List
    write: bool
    user: User
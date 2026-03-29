from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# -------------------- Task --------------------
@dataclass
class Task:
    task_id: int
    title: str
    date_time: datetime
    status: str = "pending"
    pet: Optional["Pet"] = None

    def mark_complete(self):
        pass

    def reschedule(self, new_date_time: datetime):
        pass

    def get_details(self):
        pass


# -------------------- Pet --------------------
@dataclass
class Pet:
    pet_id: int
    name: str
    type: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self) -> List[Task]:
        pass

    def update_details(self, name: str, type: str, age: int):
        pass


# -------------------- Owner --------------------
class Owner:
    def __init__(self, owner_id: int, name: str, email: str):
        self.owner_id = owner_id
        self.name = name
        self.email = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet_id: int):
        pass

    def get_pets(self) -> List[Pet]:
        pass


# Scheduler --------------------
class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        pass

    def get_tasks_for_today(self) -> List[Task]:
        pass

    def get_tasks_by_pet(self, pet_id: int) -> List[Task]:
        pass

    def remove_task(self, task_id: int):
        pass
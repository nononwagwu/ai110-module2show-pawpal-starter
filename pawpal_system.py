from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Optional


# -------------------- Task --------------------
@dataclass
class Task:
    task_id: int
    description: str
    date_time: datetime
    frequency: str = "once"   # e.g., once, daily, weekly
    status: str = "pending"
    pet: Optional["Pet"] = None

    def mark_complete(self):
        self.status = "completed"

    def reschedule(self, new_date_time: datetime):
        self.date_time = new_date_time
        self.status = "pending"

    def get_details(self) -> str:
        return f"{self.description} for {self.pet.name if self.pet else 'Unknown'} at {self.date_time} [{self.status}]"


# -------------------- Pet --------------------
@dataclass
class Pet:
    pet_id: int
    name: str
    type: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        task.pet = self
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def update_details(self, name: str, type: str, age: int):
        self.name = name
        self.type = type
        self.age = age


# -------------------- Owner --------------------
class Owner:
    def __init__(self, owner_id: int, name: str, email: str):
        self.owner_id = owner_id
        self.name = name
        self.email = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet_id: int):
        self.pets = [pet for pet in self.pets if pet.pet_id != pet_id]

    def get_pets(self) -> List[Pet]:
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


# -------------------- Scheduler --------------------
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        return self.owner.get_all_tasks()

    def get_tasks_for_today(self) -> List[Task]:
        today = date.today()
        return [
            task for task in self.get_all_tasks()
            if task.date_time.date() == today
        ]

    def get_tasks_by_pet(self, pet_id: int) -> List[Task]:
        return [
            task for task in self.get_all_tasks()
            if task.pet and task.pet.pet_id == pet_id
        ]

    def add_task(self, pet_id: int, task: Task):
        for pet in self.owner.get_pets():
            if pet.pet_id == pet_id:
                pet.add_task(task)
                return

    def remove_task(self, task_id: int):
        for pet in self.owner.get_pets():
            pet.tasks = [t for t in pet.tasks if t.task_id != task_id]
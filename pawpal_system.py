from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Optional


# -------------------- Task --------------------
@dataclass
class Task:
    task_id: int
    description: str
    date_time: datetime
    frequency: str = "once"
    status: str = "pending"
    pet: Optional["Pet"] = None

    def mark_complete(self):
        """Mark the task as completed."""
        self.status = "completed"

    def reschedule(self, new_date_time: datetime):
        """Reschedule the task."""
        self.date_time = new_date_time
        self.status = "pending"

    def get_details(self):
        """Return readable task info."""
        pet_name = self.pet.name if self.pet else "Unknown"
        return f"{self.description} for {pet_name} at {self.date_time.strftime('%I:%M %p')} [{self.status}]"


# -------------------- Pet --------------------
@dataclass
class Pet:
    pet_id: int
    name: str
    type: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task and link it to this pet."""
        task.pet = self
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks

    def update_details(self, name: str, type: str, age: int):
        """Update pet info."""
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
        """Add a pet."""
        self.pets.append(pet)

    def remove_pet(self, pet_id: int):
        """Remove a pet by ID."""
        self.pets = [p for p in self.pets if p.pet_id != pet_id]

    def get_pets(self) -> List[Pet]:
        """Return all pets."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


# -------------------- Scheduler --------------------
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks."""
        return self.owner.get_all_tasks()

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by time."""
        return sorted(tasks, key=lambda t: t.date_time)

    def get_tasks_for_today(self) -> List[Task]:
        """Get today's tasks sorted by time."""
        today_tasks = [
            task for task in self.get_all_tasks()
            if task.date_time.date() == date.today()
        ]
        return self.sort_by_time(today_tasks)

    def get_tasks_by_pet(self, pet_id: int) -> List[Task]:
        """Get tasks for a specific pet."""
        return [
            task for task in self.get_all_tasks()
            if task.pet and task.pet.pet_id == pet_id
        ]

    def filter_by_pet_name(self, pet_name: str) -> List[Task]:
        """Filter tasks by pet name."""
        return [
            task for task in self.get_all_tasks()
            if task.pet and task.pet.name.lower() == pet_name.lower()
        ]

    def get_tasks_by_status(self, status: str) -> List[Task]:
        """Filter tasks by status."""
        return [
            task for task in self.get_all_tasks()
            if task.status == status
        ]
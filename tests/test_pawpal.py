from datetime import datetime
from pawpal_system import Task, Pet


def test_task_mark_complete():
    task = Task(1, "Walk dog", datetime.now())
    task.mark_complete()
    assert task.status == "completed"


def test_pet_add_task():
    pet = Pet(1, "Buddy", "Dog", 3)
    task = Task(1, "Feed dog", datetime.now())

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert task.pet == pet
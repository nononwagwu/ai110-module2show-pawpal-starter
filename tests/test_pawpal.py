from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


# -------- Existing Tests --------
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


# -------- New Tests --------

def test_sort_by_time():
    owner = Owner(1, "John", "john@example.com")
    pet = Pet(1, "Buddy", "Dog", 3)
    owner.add_pet(pet)

    now = datetime.now()

    task1 = Task(1, "Late Task", now + timedelta(hours=3))
    task2 = Task(2, "Early Task", now + timedelta(hours=1))
    task3 = Task(3, "Middle Task", now + timedelta(hours=2))

    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)

    scheduler = Scheduler(owner)

    sorted_tasks = scheduler.sort_by_time(scheduler.get_all_tasks())

    assert sorted_tasks[0].description == "Early Task"
    assert sorted_tasks[1].description == "Middle Task"
    assert sorted_tasks[2].description == "Late Task"


def test_filter_by_status():
    owner = Owner(1, "John", "john@example.com")
    pet = Pet(1, "Buddy", "Dog", 3)
    owner.add_pet(pet)

    task1 = Task(1, "Task 1", datetime.now())
    task2 = Task(2, "Task 2", datetime.now())

    pet.add_task(task1)
    pet.add_task(task2)

    task1.mark_complete()

    scheduler = Scheduler(owner)

    completed_tasks = scheduler.get_tasks_by_status("completed")

    assert len(completed_tasks) == 1
    assert completed_tasks[0].description == "Task 1"


def test_filter_by_pet_name():
    owner = Owner(1, "John", "john@example.com")

    dog = Pet(1, "Buddy", "Dog", 3)
    cat = Pet(2, "Mochi", "Cat", 2)

    owner.add_pet(dog)
    owner.add_pet(cat)

    task1 = Task(1, "Walk dog", datetime.now())
    task2 = Task(2, "Feed cat", datetime.now())

    dog.add_task(task1)
    cat.add_task(task2)

    scheduler = Scheduler(owner)

    buddy_tasks = scheduler.filter_by_pet_name("Buddy")

    assert len(buddy_tasks) == 1
    assert buddy_tasks[0].description == "Walk dog"
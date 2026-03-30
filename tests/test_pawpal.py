from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


# -------- Sorting Correctness --------
def test_sorting_tasks_chronologically():
    owner = Owner(1, "John", "john@example.com")
    pet = Pet(1, "Buddy", "Dog", 3)
    owner.add_pet(pet)

    now = datetime.now()

    t1 = Task(1, "Late", now + timedelta(hours=3))
    t2 = Task(2, "Early", now + timedelta(hours=1))
    t3 = Task(3, "Middle", now + timedelta(hours=2))

    pet.add_task(t1)
    pet.add_task(t2)
    pet.add_task(t3)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time(scheduler.get_all_tasks())

    assert [t.description for t in sorted_tasks] == ["Early", "Middle", "Late"]


# -------- Recurrence Logic --------
def test_daily_task_creates_next_occurrence():
    owner = Owner(1, "John", "john@example.com")
    pet = Pet(1, "Buddy", "Dog", 3)
    owner.add_pet(pet)

    now = datetime.now()

    task = Task(1, "Walk dog", now, frequency="daily")
    pet.add_task(task)

    new_task = task.mark_complete()

    # original task completed
    assert task.status == "completed"

    # new task created
    assert new_task is not None
    assert new_task in pet.tasks

    # new task is scheduled for next day
    assert new_task.date_time.date() == (now + timedelta(days=1)).date()


# -------- Conflict Detection --------
def test_conflict_detection_same_time():
    owner = Owner(1, "John", "john@example.com")

    dog = Pet(1, "Buddy", "Dog", 3)
    cat = Pet(2, "Mochi", "Cat", 2)

    owner.add_pet(dog)
    owner.add_pet(cat)

    same_time = datetime.now()

    t1 = Task(1, "Walk dog", same_time)
    t2 = Task(2, "Feed cat", same_time)

    dog.add_task(t1)
    cat.add_task(t2)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "Conflict" in conflicts[0]
from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


# Create owner
owner = Owner(1, "John Doe", "john@example.com")

# Create pets
dog = Pet(1, "Buddy", "Dog", 3)
cat = Pet(2, "Whiskers", "Cat", 2)

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# SAME TIME (to trigger conflict)
same_time = datetime.now() + timedelta(hours=2)

task1 = Task(1, "Morning Walk", same_time)
task2 = Task(2, "Feed Dinner", same_time)

# Another task (different time)
task3 = Task(3, "Vet Appointment", datetime.now() + timedelta(days=1))

# Assign tasks
dog.add_task(task1)
cat.add_task(task2)
cat.add_task(task3)

# Create scheduler
scheduler = Scheduler(owner)

# -------------------- Schedule --------------------
today_tasks = scheduler.get_tasks_for_today()

print("\n=== Today's Schedule ===\n")

if not today_tasks:
    print("No tasks scheduled for today.")
else:
    for task in today_tasks:
        time_str = task.date_time.strftime("%I:%M %p")
        pet_name = task.pet.name if task.pet else "Unknown"
        status = "✓" if task.status == "completed" else "•"

        print(f"{status} {time_str} | {pet_name:<10} | {task.description}")


# -------------------- Conflict Detection --------------------
print("\n=== Conflict Check ===\n")

conflicts = scheduler.detect_conflicts()

if not conflicts:
    print("No conflicts found.")
else:
    for c in conflicts:
        print(c)
import streamlit as st
from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

# -------------------- Session State --------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner(1, "Default User", "user@example.com")

owner = st.session_state.owner


# -------------------- Page Setup --------------------
st.set_page_config(page_title="PawPal+", page_icon="🐾")

st.title("🐾 PawPal+")

# -------------------- Add Pet --------------------
st.subheader("Add Pet")

owner_name = st.text_input("Owner name", value=owner.name)
pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "other"])

owner.name = owner_name

if st.button("Add Pet"):
    new_pet = Pet(
        pet_id=len(owner.get_pets()) + 1,
        name=pet_name,
        type=species,
        age=1
    )
    owner.add_pet(new_pet)
    st.success(f"{pet_name} added!")

# Show pets
pets = owner.get_pets()
if pets:
    st.write("Your Pets:")
    for pet in pets:
        st.write(f"- {pet.name} ({pet.type})")
else:
    st.info("No pets yet.")

st.divider()

# -------------------- Add Task --------------------
st.subheader("Add Task")

task_title = st.text_input("Task title")
task_time = st.time_input("Task time")

if st.button("Add Task"):
    if not pets:
        st.warning("Add a pet first!")
    else:
        pet = pets[0]  # simple version

        new_task = Task(
            task_id=len(pet.tasks) + 1,
            description=task_title,
            date_time=datetime.combine(datetime.today(), task_time)
        )

        pet.add_task(new_task)
        st.success(f"Task added to {pet.name}!")

st.divider()

# -------------------- Filters --------------------
st.subheader("Filters")

scheduler = Scheduler(owner)

selected_pet = st.selectbox(
    "Filter by Pet",
    ["All"] + [pet.name for pet in pets]
)

selected_status = st.selectbox(
    "Filter by Status",
    ["All", "pending", "completed"]
)

# -------------------- Get Tasks --------------------
tasks = scheduler.get_all_tasks()

# Apply pet filter
if selected_pet != "All":
    tasks = scheduler.filter_by_pet_name(selected_pet)

# Apply status filter
if selected_status != "All":
    tasks = [t for t in tasks if t.status == selected_status]

# Sort tasks
tasks = scheduler.sort_by_time(tasks)

# -------------------- Display --------------------
st.subheader("Tasks")

if not tasks:
    st.info("No tasks available.")
else:
    for task in tasks:
        st.write(
            f"{task.date_time.strftime('%I:%M %p')} | "
            f"{task.pet.name} → {task.description} [{task.status}]"
        )
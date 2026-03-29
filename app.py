import streamlit as st
from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

# -------------------- Session State --------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner(1, "Default User", "user@example.com")

owner = st.session_state.owner


# -------------------- Page Setup --------------------
st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown("Simple pet care planner demo.")

st.divider()


# -------------------- Owner & Pet Input --------------------
st.subheader("Add Pet")

owner_name = st.text_input("Owner name", value=owner.name)
pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "other"])

# update owner name
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

# display pets
if owner.get_pets():
    st.write("Your Pets:")
    for pet in owner.get_pets():
        st.write(f"- {pet.name} ({pet.type})")
else:
    st.info("No pets yet.")


st.divider()


# -------------------- Task Input --------------------
st.subheader("Add Task")

task_title = st.text_input("Task title")
task_time = st.time_input("Task time")

if st.button("Add Task"):
    if not owner.get_pets():
        st.warning("Add a pet first!")
    else:
        pet = owner.get_pets()[0]  # simple: first pet

        new_task = Task(
            task_id=len(pet.tasks) + 1,
            description=task_title,
            date_time=datetime.combine(datetime.today(), task_time)
        )

        pet.add_task(new_task)
        st.success(f"Task '{task_title}' added to {pet.name}!")

# display tasks
if owner.get_pets():
    pet = owner.get_pets()[0]
    if pet.tasks:
        st.write("Tasks:")
        for task in pet.tasks:
            st.write(f"- {task.description} at {task.date_time.strftime('%I:%M %p')} [{task.status}]")
    else:
        st.info("No tasks yet.")


st.divider()


# -------------------- Schedule --------------------
st.subheader("Today's Schedule")

scheduler = Scheduler(owner)
tasks_today = sorted(
    scheduler.get_tasks_for_today(),
    key=lambda t: t.date_time
)

if st.button("Generate Schedule"):
    if not tasks_today:
        st.warning("No tasks scheduled for today.")
    else:
        st.success("Schedule generated!")

        for task in tasks_today:
            st.write(
                f"{task.date_time.strftime('%I:%M %p')} | "
                f"{task.pet.name} → {task.description} [{task.status}]"
            )
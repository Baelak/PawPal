import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# --- Initialize session state once ---
if "owner" not in st.session_state:
    st.session_state["owner"] = None

if "scheduler" not in st.session_state:
    st.session_state["scheduler"] = Scheduler()

# ---------------------------------------------------------------------------
# Section 1: Owner setup
# ---------------------------------------------------------------------------
st.title("🐾 PawPal+")
st.subheader("Owner Setup")

owner_name = st.text_input("Owner name", value="Jordan")
available_time = st.number_input("Time available today (minutes)", min_value=10, max_value=480, value=90)

if st.button("Save Owner"):
    st.session_state["owner"] = Owner(name=owner_name, available_time=int(available_time))
    st.success(f"Owner '{owner_name}' saved with {available_time} minutes available.")

# Convenience reference — may be None if owner not saved yet
owner: Owner | None = st.session_state["owner"]

st.divider()

# ---------------------------------------------------------------------------
# Section 2: Add a Pet
# ---------------------------------------------------------------------------
st.subheader("Add a Pet")

if owner is None:
    st.info("Save an owner above before adding pets.")
else:
    pet_name = st.text_input("Pet name", value="Biscuit")
    pet_type = st.selectbox("Species", ["dog", "cat", "bird", "other"])

    if st.button("Add Pet"):
        new_pet = Pet(name=pet_name, type=pet_type)
        owner.add_pet(new_pet)          # Owner.add_pet() handles the relationship
        st.success(f"Added {pet_type} '{pet_name}' to {owner.name}'s pets.")

    if owner.pets:
        st.write(f"{owner.name}'s pets: " + ", ".join(f"{p.name} ({p.type})" for p in owner.pets))

st.divider()

# ---------------------------------------------------------------------------
# Section 3: Add a Task to a Pet
# ---------------------------------------------------------------------------
st.subheader("Add a Task")

if owner is None or not owner.pets:
    st.info("Add at least one pet before scheduling tasks.")
else:
    pet_names = [p.name for p in owner.pets]
    selected_pet_name = st.selectbox("Assign task to", pet_names)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_name = st.text_input("Task name", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["high", "medium", "low"])

    frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])

    if st.button("Add Task"):
        # Find the selected pet and call Pet.add_task()
        target_pet = next(p for p in owner.pets if p.name == selected_pet_name)
        new_task = Task(name=task_name, duration=int(duration), priority=priority, frequency=frequency)
        target_pet.add_task(new_task)   # Pet.add_task() stores it on the pet
        st.success(f"Added '{task_name}' to {selected_pet_name}.")

    # Show all current tasks across all pets
    all_tasks = owner.get_all_tasks()
    if all_tasks:
        st.write("Current tasks:")
        st.table([
            {"Pet": p.name, "Task": t.name, "Duration": t.duration, "Priority": t.priority, "Frequency": t.frequency}
            for p in owner.pets for t in p.get_pending_tasks()
        ])

st.divider()

# ---------------------------------------------------------------------------
# Section 4: Generate Schedule
# ---------------------------------------------------------------------------
st.subheader("Build Schedule")

if owner is None or not owner.pets or not owner.get_all_tasks():
    st.info("Add an owner, pets, and tasks before generating a schedule.")
else:
    if st.button("Generate Schedule"):
        schedule = st.session_state["scheduler"].generate_plan(owner)  # Scheduler.generate_plan()
        st.success("Schedule generated!")
        st.text(schedule.get_plan())    # Schedule.get_plan() formats the output

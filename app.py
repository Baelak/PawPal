import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# --- Initialize session state once ---
if "owner" not in st.session_state:
    st.session_state["owner"] = None

if "scheduler" not in st.session_state:
    st.session_state["scheduler"] = Scheduler()

scheduler: Scheduler = st.session_state["scheduler"]

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
        owner.add_pet(Pet(name=pet_name, type=pet_type))
        st.success(f"Added {pet_type} '{pet_name}' to {owner.name}'s pets.")

    if owner.pets:
        st.caption(f"{owner.name}'s pets: " + ", ".join(f"{p.name} ({p.type})" for p in owner.pets))

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

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        task_name = st.text_input("Task name", value="Morning walk")
    with col2:
        task_time = st.text_input("Start time (HH:MM)", value="08:00")
    with col3:
        duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
    with col4:
        priority = st.selectbox("Priority", ["high", "medium", "low"])

    frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])

    if st.button("Add Task"):
        target_pet = next(p for p in owner.pets if p.name == selected_pet_name)
        target_pet.add_task(Task(
            name=task_name,
            duration=int(duration),
            priority=priority,
            scheduled_time=task_time,
            frequency=frequency,
        ))
        st.success(f"Added '{task_name}' to {selected_pet_name}.")

    # --- All pending tasks, sorted chronologically via Scheduler.sort_by_time() ---
    all_tasks = owner.get_all_tasks()
    if all_tasks:
        sorted_tasks = scheduler.sort_by_time(all_tasks)

        st.markdown("**Current tasks** (sorted by start time)")
        # Build a pet-name lookup so we can show which pet each task belongs to
        task_to_pet = {id(t): p.name for p in owner.pets for t in p.tasks}
        st.table([
            {
                "Pet":       task_to_pet.get(id(t), "—"),
                "Start":     t.scheduled_time,
                "Task":      t.name,
                "Duration":  f"{t.duration} min",
                "Priority":  t.priority.capitalize(),
                "Frequency": t.frequency,
            }
            for t in sorted_tasks
        ])

        # --- Conflict warnings via Scheduler.conflict_warnings() ---
        warnings = scheduler.conflict_warnings(all_tasks)
        if warnings:
            st.markdown("**Schedule conflicts**")
            for w in warnings:
                # Strip the leading "WARNING: " prefix — Streamlit's icon does that job
                st.warning(w.replace("WARNING: ", ""))
        else:
            st.success("No scheduling conflicts detected.")

st.divider()

# ---------------------------------------------------------------------------
# Section 4: Generate Schedule
# ---------------------------------------------------------------------------
st.subheader("Today's Schedule")

if owner is None or not owner.pets or not owner.get_all_tasks():
    st.info("Add an owner, pets, and tasks before generating a schedule.")
else:
    if st.button("Generate Schedule"):
        schedule = scheduler.generate_plan(owner)

        if not schedule.tasks:
            st.error("No tasks could fit within the available time budget.")
        else:
            st.success(f"Scheduled {len(schedule.tasks)} task(s) — "
                       f"{sum(t.duration for t in schedule.tasks)} of "
                       f"{owner.available_time} minutes used.")

            # Scheduled tasks table
            st.markdown("**Planned tasks** (priority order, then by time)")
            st.table([
                {
                    "Start":     t.scheduled_time,
                    "End":       t.end_time(),
                    "Task":      t.name,
                    "Duration":  f"{t.duration} min",
                    "Priority":  t.priority.capitalize(),
                    "Frequency": t.frequency,
                }
                for t in schedule.tasks
            ])

        # Skipped tasks
        if schedule.skipped:
            st.markdown("**Skipped** (not enough time remaining)")
            for t in schedule.skipped:
                st.warning(f"{t.name} ({t.duration} min, {t.priority} priority) could not be scheduled today.")

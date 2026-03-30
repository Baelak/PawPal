from pawpal_system import Owner, Pet, Task, Scheduler

# --- Setup owner ---
owner = Owner(name="Jordan", available_time=90)

# --- Pet 1: dog ---
dog = Pet(name="Biscuit", type="dog")
dog.add_task(Task(name="Morning walk",      duration=20, priority="high",   frequency="daily"))
dog.add_task(Task(name="Feeding",           duration=10, priority="high",   frequency="daily"))
dog.add_task(Task(name="Flea medication",   duration=5,  priority="high",   frequency="weekly"))
dog.add_task(Task(name="Fetch in the yard", duration=15, priority="medium", frequency="daily"))

# --- Pet 2: cat ---
cat = Pet(name="Luna", type="cat")
cat.add_task(Task(name="Litter box clean",  duration=10, priority="high",   frequency="daily"))
cat.add_task(Task(name="Feeding",           duration=5,  priority="high",   frequency="daily"))
cat.add_task(Task(name="Brushing",          duration=10, priority="medium", frequency="weekly"))
cat.add_task(Task(name="Laser pointer play",duration=10, priority="low",    frequency="daily"))

owner.add_pet(dog)
owner.add_pet(cat)

# --- Generate and print schedule ---
scheduler = Scheduler()
schedule = scheduler.generate_plan(owner)

print(f"\nToday's Schedule for {owner.name} ({owner.available_time} min available)")
print("=" * 50)
print(schedule.get_plan())

from pawpal_system import Task, Pet


def test_mark_complete_changes_status():
    task = Task(name="Morning walk", duration=20, priority="high")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Biscuit", type="dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task(name="Feeding", duration=10, priority="high"))
    assert len(pet.tasks) == 1

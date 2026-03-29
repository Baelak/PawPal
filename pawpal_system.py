from __future__ import annotations
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Task
# ---------------------------------------------------------------------------

@dataclass
class Task:
    name: str
    duration: int       # minutes
    priority: str       # "high" | "medium" | "low"


# ---------------------------------------------------------------------------
# Pet
# ---------------------------------------------------------------------------

@dataclass
class Pet:
    name: str
    type: str           # "dog" | "cat" | "bird" | etc.
    tasks: list[Task] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Owner
# ---------------------------------------------------------------------------

@dataclass
class Owner:
    name: str
    preferences: dict = field(default_factory=dict)
    available_time: int = 0     # total minutes available per day


# ---------------------------------------------------------------------------
# Schedule
# ---------------------------------------------------------------------------

class Schedule:
    def __init__(self, tasks: list[Task]) -> None:
        self.tasks = tasks

    def get_plan(self) -> str:
        """Return a human-readable string describing the scheduled tasks."""
        pass


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------

class Scheduler:
    def generate_plan(self, owner: Owner, pet: Pet) -> Schedule:
        """Select and order tasks for the pet given the owner's constraints."""
        pass


# ---------------------------------------------------------------------------
# PawPalApp  (entry point)
# ---------------------------------------------------------------------------

class PawPalApp:
    def run(self) -> None:
        """Launch the application (CLI demo or Streamlit UI)."""
        pass

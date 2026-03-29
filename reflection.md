# PawPal+ Project Reflection

## 1. System Design
This is my first idea for the system design.
    - Walking
            > Who is walking the pet
            > Walking Schedule
            
    - Feeding
            > Feeding Schedule
            > Who is feeding the pet
            > Payment
    - Grooming
            > Grooming Store
            > Grooming Appointment
**a. Initial design**

The initial design centered on five classes

- **Owner** — represents a pet owner; holds contact info and a list of associated pets.
- **Pet** — represents an individual animal; stores species, age, and a list of tasks.
- **Task** — the core unit of work (feeding, walk, grooming,); holds a scheduled time, priority level, category, and recurrence settings.
- **Scheduler** — stateless utility class containing the algorithmic logic: sorting tasks by priority/time, detecting time conflicts between tasks, and generating future instances of recurring tasks.




**b. Design changes**

During implementation, the `Scheduler` was initially conceived as methods spread across the `Pet` class. It was refactored into its own standalone class to keep `Pet` focused purely on data ownership and to make the scheduling logic independently testable. This separation follows the Single Responsibility Principle — `Pet` stores tasks, `Scheduler` reasons about them.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

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

The system is built on six classes. 
- Task is the simplest — it just holds a task name, how long it takes, and its priority.
- Pet groups a pet's name and type together with its list of tasks.-
- Owner stores the owner's name, their preferences, and how much time they have available each day. 
- Schedule holds the final ordered list of tasks and can produce a readable plan.
- Scheduler contains the core logic — it takes an owner and a pet and decides which tasks to include and in what order. 
- PawPalApp is the entry point that wires everything together and launches the app.

**b. Design changes**

Yes, the design changed during implementation. The original Owner class had no link to Pet — ownership was implied but never modeled in code. During review it became clear that without a pets list on Owner, there was no way to retrieve all pets for a given owner or pass them to the scheduler.

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

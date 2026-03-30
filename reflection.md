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

- The scheduler considers two main constraints: the owner's total available time per day and each task's priority level. It sorts tasks by priority first, then fits them into the time budget. Time felt like the most important constraint because no matter how urgent a task is, it can't happen if there's no time. The priority just decides which tasks get the limited slots first.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

- The scheduler uses a greedy approach. It picks the highest priority tasks first and stops when time runs out. The tradeoff is that a short low priority task that would easily fit might get skipped if a long high-priority task consumed most of the budget. This is because missing a high-priority task like medication is worse than skipping a low priority one like play, even if the low priority task would have technically fit.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used Claude for UML brainstorming, generating class skeletons, implementing scheduling logic, and writing tests. The most helpful prompts were specific and scoped which accomplishes the task efficiently. such as asking it to review a single method or flag missing relationships. Vague prompts needed more correction and back and forth than focused ones.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

When Claude generated next occurrence, it calculated the next date from the self scheduled date. A task created last week would schedule its follow up relative to that old date which possibly might be still in the past. I caught this by tracing through a manual scenario, then modified the method and verified it with a test.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion status, chronological sorting, recurring task creation (daily,weekly,once), conflict detection, and edge cases. These matter because they cover the three core behaviors the app promises which are scheduling correctly, catching conflicts, and handling recurring tasks without crashing.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am confident in the core logic as all 13 tests passed. Next I'd test the multi-day chains where a recurring task's follow up also becomes due, and behavior when there is no available time.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The Scheduler class. Having all the scheduling code in one place made it easy to test and easy to use in the app.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I believe adding a scheduled date filter to generate a plan so it only considers tasks due today. Right now the plan includes any pending task regardless of date, which would cause issues across multiple days of use.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

AI is most useful when you already have a clear mental model of what you're building which allows you to be specific. Specific, scoped prompts produce accurate output fast and make the project go faster and smoother. If you know enough to evaluate what the AI produces then it is easier to redirect it when it drifts.

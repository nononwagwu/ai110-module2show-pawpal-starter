# PawPal+ Project Reflection

## 1. System Design
Add and manage pets
Schedule pet-related tasks
View and track daily tasks

**a. Initial design**

- Briefly describe your initial UML design.
The initial UML design includes four main classes: Owner, Pet, Task, and Scheduler, each with a clear responsibility in the system.

- What classes did you include, and what responsibilities did you assign to each?
Owner: Represents the user of the app. It manages a collection of pets and is responsible for adding, removing, and viewing pets.
Pet: Represents an individual pet. It stores details such as name, type, and age, and maintains a list of tasks associated with that pet. It can add and retrieve tasks and update its own information.
Task: Represents a specific activity (e.g., feeding, walking). It contains details like title, date/time, status, and the pet it belongs to. It is responsible for marking completion, rescheduling, and providing task details.
Scheduler: Manages all tasks across the system. It handles adding tasks, retrieving tasks for a specific day or pet, and removing tasks.



**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Yes,First I removed the task list from the Pet class. At first Pet and scheduler classes stored tasks which created duplicate sources of truth.This could lead to inconsistencies if a task was added or removed in one place but not the other. To fix this, I made the Scheduler the single source of truth for all tasks.
Second, I kept the relationship between Task and Pet by ensuring each task still has a reference to the pet it belongs to (task.pet). This preserves the connection without needing to store tasks inside the Pet class.

Third, I clarified responsibilities across classes. The Owner manages pets, the Scheduler manages tasks, and Task represents individual activities. This separation of concerns makes the system easier to understand and maintain.

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

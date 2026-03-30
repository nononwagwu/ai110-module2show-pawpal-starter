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
The scheduler considers several key constraints when organizing tasks. The primary constraint is time, as tasks are scheduled and sorted based on their date_time to ensure a clear chronological order. It also considers task status (pending or completed), which allows filtering and tracking progress. Additionally, the system accounts for task frequency (once, daily, weekly) to support recurring tasks. Another important constraint is conflict detection, where the scheduler checks if multiple tasks occur at the same exact time and flags them as potential issues.

- How did you decide which constraints mattered most?
I prioritized time as the most important constraint because scheduling fundamentally depends on when tasks occur. Without proper time ordering, the system would not provide a useful daily plan. After that, I focused on recurrence and conflict detection, as these features add practical value by automating repeated tasks and identifying scheduling issues. I chose not to implement more complex constraints such as task duration or user preferences at this stage in order to keep the system simple, readable, and maintainable. This allowed me to build a stable foundation before adding more advanced scheduling logic.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff in my scheduler is the way conflict detection is implemented. The algorithm only checks for tasks that occur at the exact same time rather than detecting overlapping durations. This simplifies the implementation and keeps the code easy to read and maintain. However, it means the system may not detect conflicts where tasks overlap but start at slightly different times. Additionally, I chose a more explicit loop-based approach instead of a more compact Pythonic version to prioritize readability and clarity over conciseness.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI tools, particularly VS Code Copilot and Chat, throughout multiple stages of the project. During the design phase, I used AI to brainstorm the structure of the system, including identifying key classes such as Owner, Pet, Task, and Scheduler, and how they should interact. During implementation, AI helped generate method skeletons and provided guidance on writing algorithms for sorting, filtering, recurring tasks, and conflict detection. It was also useful for debugging when errors occurred and for refactoring code to improve readability and structure. Additionally, AI assisted in generating unit tests and suggesting improvements to make the system more robust.

- What kinds of prompts or questions were most helpful?
I used AI tools, particularly VS Code Copilot and Chat, throughout multiple stages of the project. During the design phase, I used AI to brainstorm the structure of the system, including identifying key classes such as Owner, Pet, Task, and Scheduler, and how they should interact. During implementation, AI helped generate method skeletons and provided guidance on writing algorithms for sorting, filtering, recurring tasks, and conflict detection. It was also useful for debugging when errors occurred and for refactoring code to improve readability and structure. Additionally, AI assisted in generating unit tests and suggesting improvements to make the system more robust.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
One moment where I did not accept an AI suggestion as-is was during the implementation of the conflict detection algorithm. The AI suggested a more compact, “Pythonic” version using list comprehensions to generate conflict warnings in a single expression. While this approach was shorter, I found it harder to read and less intuitive to debug, especially when handling multiple tasks and conditions. I chose to keep a more explicit loop-based implementation instead, as it made the logic clearer and easier to maintain.
- How did you evaluate or verify what the AI suggested?
To evaluate and verify AI suggestions, I compared them against my existing design goals, focusing on readability, correctness, and maintainability. I also tested the suggested code by running it in main.py and through my pytest suite to ensure it behaved as expected. If a suggestion introduced unnecessary complexity or reduced clarity, I modified it to better fit my system. This process helped ensure that AI-generated code was not only functional but also aligned with the overall structure and quality of my project.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested several core behaviors of the PawPal+ system to ensure it functioned correctly. These included task sorting, to verify that tasks are returned in chronological order; recurrence logic, to confirm that daily tasks automatically generate a new task for the next day when marked complete; and conflict detection, to ensure the system correctly identifies tasks scheduled at the same exact time. I also tested basic task management behaviors such as adding tasks to pets and marking tasks as completed.
- Why were these tests important?
I tested several core behaviors of the PawPal+ system to ensure it functioned correctly. These included task sorting, to verify that tasks are returned in chronological order; recurrence logic, to confirm that daily tasks automatically generate a new task for the next day when marked complete; and conflict detection, to ensure the system correctly identifies tasks scheduled at the same exact time. I also tested basic task management behaviors such as adding tasks to pets and marking tasks as completed.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am moderately to highly confident in the correctness of my scheduler, around 4 out of 5. The core features—such as sorting, filtering, recurring tasks, and conflict detection—have been implemented and verified through automated tests and manual testing in the CLI demo. These tests confirm that the system behaves as expected under normal conditions. However, there are still some limitations and untested edge cases that could affect reliability in more complex scenarios.

- What edge cases would you test next if you had more time?
If I had more time, I would test additional edge cases to improve the system’s robustness. For example, I would test tasks with overlapping durations rather than just exact matching times, as the current conflict detection only checks for identical timestamps. I would also test scenarios with a large number of tasks to evaluate performance and scalability. Other edge cases include handling invalid or missing data (such as tasks without assigned pets), multiple recurring tasks interacting over time, and ensuring that task IDs remain unique when new recurring tasks are generated. These tests would help ensure the scheduler performs reliably in more complex and realistic situations.


---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The part of the project I am most satisfied with is the implementation of the scheduling logic, especially features like sorting, recurring tasks, and conflict detection. These components work together to make the system feel intelligent rather than just a basic task manager. I am also satisfied with how the backend and frontend were successfully connected, allowing user actions in the Streamlit UI to interact with the underlying classes. Additionally, building and passing a test suite gave me confidence that the system behaves correctly.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the scheduling system by adding more advanced constraints, such as handling overlapping task durations instead of only exact time matches. I would also redesign parts of the system to better support multiple pets in the UI, rather than relying on a simplified approach. Another improvement would be implementing persistent storage (e.g., saving data to a file or database) so that user data is not lost between sessions. Finally, I would enhance the UI to make it more interactive and user-friendly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned from this project is the importance of balancing AI assistance with human judgment. While AI tools like Copilot were very helpful for generating ideas and speeding up development, it was necessary to critically evaluate and refine those suggestions to ensure they fit my design goals. I also learned that designing systems requires clear structure and separation of concerns, which made it easier to build, test, and extend the application.

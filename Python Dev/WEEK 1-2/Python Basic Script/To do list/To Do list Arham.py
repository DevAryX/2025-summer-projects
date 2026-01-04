"""
Simple To-Do List App

This script allows the user to:
1. Add multiple tasks to a list.
2. Type 'done' to finish input.
3. View a numbered list of all added tasks.
"""

# Initialize an empty list to store tasks
tasks = []

# Greeting message and instructions
print("Welcome to your To-Do List App!")
print("Type 'done' when you're finished adding tasks.")

# --- Task Input Loop ---
# Continuously prompt user to enter tasks until they type 'done'
while True:
    task = input("Enter a task: ")
    
    if task.lower() == "done":
        # Exit the loop when user is finished
        break

    # Add the task to the list
    tasks.append(task)

# --- Display All Tasks ---
print("\nHere are your tasks:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

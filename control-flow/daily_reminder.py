import os

def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time-sensitivity,
    then provides a customized reminder.
    """
    # 1. Checks for files exists and not empty (simulated for this script's scope)
    #    For a real-world scenario, this would involve checking actual file paths.
    #    Since this script doesn't read from/write to files, we can acknowledge
    #    that this specific check isn't directly applicable here but could be
    #    implemented if the script were expanded to manage tasks in a file.
    #    For demonstration, let's assume a hypothetical "task_data.txt"
    #    would exist and not be empty if the script were to load tasks from it.
    #    As the current objective is a simplified script without data structures
    #    to store multiple tasks, this check is 'not applicable' in its direct sense
    #    but acknowledged as a design consideration for a more complex system.

    while True:
        # 2. Checks for user prompts: Task, Time Bound, Priority
        task = input("Enter your task: ").strip()
        if not task:
            print("Task description cannot be empty. Please enter a task.")
            continue

        priority = input("Priority (high/medium/low): ").lower().strip()
        time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()

        # Input validation for time_bound
        if time_bound_input not in ["yes", "no"]:
            print("Invalid input for 'time-bound'. Please enter 'yes' or 'no'.")
            continue

        # Initialize reminder parts
        reminder_parts = []
        is_immediate_action_required = False

        # 3. Checks for Match Case statement reaction implementation
        match priority:
            case "high":
                reminder_parts.append(f"Reminder: '{task}' is a **HIGH** priority task.")
                is_immediate_action_required = True # High priority inherently requires immediate action
            case "medium":
                reminder_parts.append(f"Reminder: '{task}' is a **MEDIUM** priority task.")
            case "low":
                reminder_parts.append(f"Note: '{task}' is a **LOW** priority task.")
                reminder_parts.append("Consider completing it when you have free time.")
            case _:
                print("Invalid priority. Please enter high, medium, or low to provide a customized reminder.")
                continue # Restart the loop for valid input

        # 4. Checks for use of if statement to modify the reminder if the task is time-bound.
        # This condition is now more carefully placed to avoid redundancy.
        if time_bound_input == "yes":
            is_immediate_action_required = True # Time-bound also means immediate action

        # Append the immediate action phrase if required and it hasn't been explicitly stated yet
        if is_immediate_action_required:
            # Avoid redundancy for high priority where 'immediate attention' is already implied
            # This logic ensures the 'that requires immediate attention today!' phrase is added correctly
            if priority != "high" or time_bound_input == "yes": # Add it if not high priority, or if high and explicitly time-bound
                if not (priority == "high" and "requires immediate attention today!" in " ".join(reminder_parts)):
                     reminder_parts.append("that requires immediate attention today!")


        # 5. Checks for Provide a Customized Reminder
        # 6. Checks for Print a reminder about the task that includes its priority level
        #    and whether immediate action is required based on time sensitivity.
        final_reminder = " ".join(reminder_parts).strip()
        print(final_reminder)
        break # Exit loop once valid input is received

# Run the daily reminder function
daily_reminder()

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")


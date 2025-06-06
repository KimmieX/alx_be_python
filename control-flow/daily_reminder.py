def daily_reminder():
    """
    Prompts the user for a task, its priority, and whether it's time-bound,
    then generates and prints a customized reminder.
    Ensures all inputs are valid before generating the reminder.
    """
    while True:
        # --- Check 1: User Prompts ---
        # Checks for user prompts: Task, Time Bound, Priority
        task = input("Enter your task: ").strip() # .strip() to remove leading/trailing whitespace

        # Validate task input
        if not task:
            print("Task cannot be empty. Please enter a valid task.")
            continue

        priority = input("Priority (high/medium/low): ").lower().strip()

        # Validate priority input using a match statement
        # --- Check 2: Match Case statement reaction implementation ---
        match priority:
            case "high":
                base_reminder = f"Reminder: '{task}' is a HIGH priority task."
                requires_immediate_attention = True
            case "medium":
                base_reminder = f"Reminder: '{task}' is a MEDIUM priority task."
                requires_immediate_attention = False
            case "low":
                base_reminder = f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time."
                requires_immediate_attention = False # Low priority doesn't require immediate attention by default
            case _:
                print("Invalid priority. Please enter 'high', 'medium', or 'low' to provide a customized reminder.")
                continue  # Restart the loop for valid input

        time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()

        # Validate time_bound input
        if time_bound_input not in ["yes", "no"]:
            print("Invalid input for 'time-bound'. Please enter 'yes' or 'no'.")
            continue

        # --- Check 3: Use of if statement to modify the reminder if the task is time-bound ---
        # If

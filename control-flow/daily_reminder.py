def daily_reminder_improved():
    while True:
        task = input("Enter your task: ")
        priority = input("Priority (high/medium/low): ").lower()
        time_bound = input("Is it time-bound? (yes/no): ").lower()

        reminder_parts = []
        requires_immediate_action = False

        if priority == "high":
            reminder_parts.append(f"Reminder: '{task}' is a HIGH priority task.")
            requires_immediate_action = True # High priority inherently requires immediate action
        elif priority == "medium":
            reminder_parts.append(f"Reminder: '{task}' is a MEDIUM priority task.")
        elif priority == "low":
            reminder_parts.append(f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time.")
        else:
            print("Invalid priority. Please enter high, medium, or low to provide a customized reminder")
            continue  # Restart the loop for valid input

        if time_bound == "yes":
            # If it's time-bound, it definitely requires immediate action
            requires_immediate_action = True

        if requires_immediate_action:
            if priority == "high":
                # For high priority, we've already stated it's high priority. Just add the time-bound specific part.
                reminder_parts.append("It requires immediate attention today due to its high priority and time sensitivity!")
            elif time_bound == "yes":
                # For medium/low priority, if it's time-bound, add a specific time-sensitive phrase.
                reminder_parts.append("This task is time-bound and requires immediate attention today!")

        # Join the parts to form the final reminder
        final_reminder = " ".join(reminder_parts)
        print(final_reminder)
        break

# daily_reminder_improved() # Uncomment to test the improved version

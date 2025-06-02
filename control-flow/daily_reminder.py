# daily_reminder.py

if __name__ == "__main__":
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound_input = input("Is it time-bound? (yes/no): ").lower()
    time_bound = time_bound_input == 'yes'

    match priority:
        case 'high':
            priority_message = "is a high priority task"
        case 'medium':
            priority_message = "is a medium priority task"
        case 'low':
            priority_message = "is a low priority task. Consider completing it when you have free time."
        case _:
            priority_message = "has a noted priority"

    reminder = f"Note: '{task}' {priority_message}"

   if time_bound:
    reminder = f"Reminder: '{task}' {priority_message} that requires immediate attention today!"
elif priority == 'low':
    pass # The low priority message is already included

    print("\n" + reminder)

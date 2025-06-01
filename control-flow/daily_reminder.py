# daily_reminder.py

if __name__ == "__main__":
    task = input("Enter your priority task for today: ")
    priority = input("What is the priority of this task? (high, medium, low): ").lower()
    time_bound_input = input("Is this task time-bound? (yes/no): ").lower()
    time_bound = time_bound_input == 'yes'

    match priority:
        case 'high':
            priority_message = "This is a high-priority task."
        case 'medium':
            priority_message = "This is a medium-priority task."
        case 'low':
            priority_message = "This is a low-priority task."
        case _:
            priority_message = "The priority of this task is noted."

    reminder = f"Reminder: You need to do '{task}'. {priority_message}"

    if time_bound:
        reminder += " That requires immediate attention today!"

    print("\nYour daily reminder:")
    print(reminder)

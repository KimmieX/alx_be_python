def daily_reminder():
    while True:
        task = input("Enter your task: ")
        priority = input("Priority (high/medium/low): ").lower()
        time_bound = input("Is it time-bound? (yes/no): ").lower()

        match priority:
            case "high":
                reminder = f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!"
            case "medium":
                reminder = f"Reminder: '{task}' is a MEDIUM priority task."
            case "low":
                reminder = f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time."
            case _:
                print("Invalid priority. Please enter high, medium, or low to provide a customized reminder")
                continue  # Restart the loop for valid input

        if time_bound == "yes":
            reminder += " That requires immediate attention today!"

        print(reminder)
        break  # Exit loop once valid input is received

daily_reminder()

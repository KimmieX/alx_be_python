def draw_pattern():
    size = int(input("Enter the size of the pattern: "))

    while size < 1:  # Ensure the user enters a positive integer
        print("Please enter a positive integer.")
        size = int(input("Enter the size of the pattern: "))

    row = 0
    while row < size:  # Iterate through each row
        for _ in range(size):  # Print asterisks in a row
            print("*", end="")
        print()  # Move to the next line after printing a full row
        row += 1

draw_pattern()

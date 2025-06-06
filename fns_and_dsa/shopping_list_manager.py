# shopping_list_manager.py

def display_menu():
    """
    Displays the main menu options for the Shopping List Manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the Shopping List Manager application.
    Manages the shopping list, user input, and program flow.
    """
    shopping_list = [] # Your script should start with an empty list named shopping_list.

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip() # Ensure input is clean

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list: # Check if list is empty before attempting removal
                print("Your shopping list is empty. Nothing to remove.")
                continue # Go back to the menu

            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove: # Ensure item name to remove is not empty
                try:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' removed from the list.")
                except ValueError:
                    # If the item is not found, display a message indicating so.
                    print(f"'{item_to_remove}' not found in the list.")
            else:
                print("Item name to remove cannot be empty. Please try again.")

        elif choice == '3':
            # Display the shopping list
            if not shopping_list: # Check if list is empty for display
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list): # Use enumerate to display numbered list
                    print(f"{i + 1}. {item}")
                print("--------------------------")

        elif choice == '4':
            print("Goodbye!")
            break # Exit the loop to terminate the program

        else:
            # Ensure your script handles invalid menu choices gracefully.
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

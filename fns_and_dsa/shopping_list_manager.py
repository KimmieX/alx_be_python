def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu() 
        choice = input("Enter your choice: ").strip() 

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item cannot be empty. Please enter a valid item.")

        elif choice == '2':
            if not shopping_list: 
                print("Your shopping list is empty. Nothing to remove.")
                continue
            
            # Display current items for easier removal
           # print("\n--- Current Shopping List ---")
           # for i, item in enumerate(shopping_list):
               # print(f"{i + 1}. {item}")
            
            try:
                item_to_remove_input = input("Enter the item number or name to remove: ").strip()
                
                if item_to_remove_input.isdigit(): # If input is a number, try removing by index
                    index_to_remove = int(item_to_remove_input) - 1
                    if 0 <= index_to_remove < len(shopping_list):
                        removed_item = shopping_list.pop(index_to_remove)
                        print(f"'{removed_item}' removed from the list.")
                    else:
                        print("Invalid item number.")
                else: # Otherwise, try removing by name
                    if item_to_remove_input in shopping_list:
                        shopping_list.remove(item_to_remove_input)
                        print(f"'{item_to_remove_input}' removed from the list.")
                    else:
                        print(f"'{item_to_remove_input}' not found in the list.")
            except ValueError:
                print("Invalid input. Please enter an item number or name.")

        elif choice == '3':
            if not shopping_list: 
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list): 
                    print(f"{i + 1}. {item}")
                print("--------------------------")

        elif choice == '4':
            print("Goodbye! Your shopping list is saved for next time...") 
            break 

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

# multiplication_table.py

if __name__ == "__main__":
    try:
        number_str = input("Enter a number to see its multiplication table: ")
        number = int(number_str)

        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

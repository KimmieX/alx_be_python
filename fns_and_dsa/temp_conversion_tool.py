def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

            if unit == 'f':
                celsius = convert_to_celsius(temperature)
                print(f"{temperature}°F is {celsius:.2f}°C")
            elif unit == 'c':
                fahrenheit = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {fahrenheit:.2f}°F")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue  # Restart the loop
            
            break  # Exit the loop when successful
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

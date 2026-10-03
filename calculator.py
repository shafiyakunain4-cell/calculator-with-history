# Python Calculator with Permanent History
# Project by Shafiya Kunain
# Demonstrates File Handling

def show_history():
    try:
        with open("history.txt", "r") as file:
            history = file.read()
            if history == "":
                print("No history found.")
            else:
                print("\n--- Calculation History ---")
                print(history)
    except FileNotFoundError:
        print("No history found yet.")

def clear_history():
    open("history.txt", "w").close()
    print("History cleared!")

def calculator():
    print("=== Python Calculator with History ===")
    while True:
        print("\nOptions: 1.Add 2.Sub 3.Mul 4.Div 5.History 6.Clear History 7.Exit")
        choice = input("Choose (1-7): ")

        if choice == '5':
            show_history()
            continue
        if choice == '6':
            clear_history()
            continue
        if choice == '7':
            print("Thank you!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                op = '+'
            elif choice == '2':
                result = num1 - num2
                op = '-'
            elif choice == '3':
                result = num1 * num2
                op = '*'
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2
                op = '/'
            else:
                print("Invalid choice!")
                continue

            print(f"Result: {result}")

            # Save to history.txt (File Handling)
            with open("history.txt", "a") as file:
                file.write(f"{num1} {op} {num2} = {result}\n")

        except ValueError:
            print("Please enter valid numbers!")

calculator()

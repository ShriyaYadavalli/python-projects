import art


# Function to add 
def add(n1, n2):
    return n1 + n2

# Function to subtract 
def subtract(n1, n2):
    return n1 - n2


# Function to multiply 
def multiply(n1, n2):
    return n1 * n2


# Function to divide 
def divide(n1, n2):
    return n1 / n2


# Dictionary that maps operation symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Main calculator function
def calculator():
    # Print the calculator logo
    print(art.logo)

    # Variable to keep the calculator running
    continue_calculating = True

    # Get the first number from the user
    num1 = float(input("What is the first number?: "))

    # Keep asking for operations until the user chooses to stop
    while continue_calculating:

        # Display all available operation symbols
        for sign in operations:
            print(sign)

        # Get the operation and second number from the user
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        # Call the appropriate function from the dictionary
        answer = operations[operation](num1, num2)

        # Display the result
        print(f"{num1} {operation} {num2} = {answer}")

        # Ask if the user wants to continue with the current answer
        choice = input( f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )

        if choice == "y":
            # Use the current answer as the first number for the next calculation
            num1 = answer
        else:
            # Stop the current calculation and start over
            continue_calculating = False
            print("\n" * 20)  # Clears the screen by printing blank lines
            calculator()      # Recursively start a new calculator session


# Start the calculator program
calculator()
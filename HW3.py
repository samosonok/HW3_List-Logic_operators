# SIMPLE CALCULATOR
# The program should perform basic mathematical operations (+, -, *, /).
# The user is prompted to enter numbers and the operation to be performed on these numbers one by one.
# The program, based on the operation, calculates and prints the result.
# Include a check to ensure that the divisor is not equal to 0 when performing division!

input_first_number = float(input("Please enter 1st number: "))
input_second_number = float(input("Please enter 2nd number: "))

chosen_operator = input("Please chose operator: "
                        "\nEnter 1 - for '+'"
                        "\nEnter 2 - for '-'"
                        "\nEnter 3 - for '*'"
                        "\nEnter 4 - for '/'")

if chosen_operator == "1":
    print(input_first_number + input_second_number)
elif chosen_operator == "2":
    print(input_first_number - input_second_number)
elif chosen_operator == "3":
    print(input_first_number * input_second_number)
elif chosen_operator == "4":
    if input_second_number == 0:
        print("Error! Division by 0")
    else:
        print(input_first_number / input_second_number)
else:
    print("You have to choose one of the numbers!")

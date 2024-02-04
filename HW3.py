# SIMPLE CALCULATOR
# The program should perform basic mathematical operations (+, -, *, /).
# The user is prompted to enter numbers and the operation to be performed on these numbers one by one.
# The program, based on the operation, calculates and prints the result.
# Include a check to ensure that the divisor is not equal to 0 when performing division!

while True:
    input_first_number = float(input("Please enter 1st number: "))
    input_second_number = float(input("Please enter 2nd number: "))
    chosen_operator = input("Please choose operator: '+' '-' '*' '/' ")

    result = 0
    if chosen_operator == "+":
        result = input_first_number + input_second_number
    elif chosen_operator == "-":
        result = input_first_number - input_second_number
    elif chosen_operator == "*":
        result = input_first_number * input_second_number
    elif chosen_operator == "/":
        if input_second_number == 0:
            print("Error! Division by 0")
        else:
            result = input_first_number / input_second_number
    else:
        print("You have to choose one of the options!")
        break
    print("Result: ", result)

    another_calculation = input("Would you like to do another calculation? 1 - yes, 2 - no: ")
    if another_calculation != "1":
        break

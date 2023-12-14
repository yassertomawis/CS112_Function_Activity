# Prompt the user to enter 3 numbers

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

# Formula for the input numbers


def formula():
    if num1 == num2 == num3:
        result = num1 * num2 * num3
        print(f"The product of {num1}, {num2}, and {num3} is {result}")
    elif num1 == num2 != num3:
        result = (num1 * num2) + num3
        print(f"{num1} multiplied by {num2} plus {num3} is {result}")
    elif num1 == num3 != num2:
        result = (num1 * num3) + num2
        print(f"{num1} multiplied by {num3} plus {num2} is {result}")
    elif num2 == num3 != num1:
        result = (num2 * num3) + num1
        print(f"{num2} multiplied by {num1} plus {num2} is {result}")
    elif num1 != num2 != num3:
        result = num1 + num2 + num3
        print(f"The product of {num1}, {num2}, and {num3} is {result}")


formula()

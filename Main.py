import Calculations

print("Matt Becker is a bitch")


if __name__ == "__main__":

    calc = Calculations

    print("Enter two numbers")
    first_num = input("First number")
    second_num = input("Second number")
    choice = input("Do you want to add or subtract? 1 for add or 2 for subtract")
    if choice == "1":

        print(calc.adding(int(first_num), int(second_num)))

    elif choice == "2":

        print(calc.subtract(int(first_num), int(second_num)))

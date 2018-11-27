print("Matt Becker is a bitch")


def adding_subtracting(first_num, second_num):

    choice = input("Do you want to add or subtract? 1 for add or 2 for subtract")
    if choice == "2":

        return print(first_num - second_num)
    elif choice == "1":

        return print(int(first_num) + int(second_num))


if __name__ == "__main__":

    print("Enter two numbers")
    first_num = input("First number")
    second_num = input("Second number")
    adding_subtracting(first_num, second_num)

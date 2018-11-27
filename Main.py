print("Matt Becker is a bitch")


def adding_subtracting(first_num, second_num):

    choice = input("Do you want to add or subtract?")
    if choice == "subtract":

        return print(first_num - second_num)
    elif choice == "add":

        return print(int(first_num) + int(second_num))


if __name__ == "__main__":

    print("Enter two numbers")
    firstnum = input("First number")
    secondnum = input("Second number")
    adding_subtracting(firstnum, secondnum)

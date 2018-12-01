print("Matt Becker is a bitch")


def adding(first_num, second_num):

    return print(first_num + second_num)


def subtract(first_num, second_num):

        return print(int(first_num) - int(second_num))


if __name__ == "__main__":

    print("Enter two numbers")
    first_num = input("First number")
    second_num = input("Second number")
    choice = input("Do you want to add or subtract? 1 for add or 2 for subtract")
    if choice == "1":

        print(adding(int(first_num) - int(second_num)))

    elif choice == "2":

        print(subtract(int(first_num), int(second_num)))

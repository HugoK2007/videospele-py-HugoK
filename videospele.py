import random
#https://gist.github.com/cwil323/9b1bfd25523f75d361879adfed550be2

def display_intro():
    title = "** Sveicināts matemātikas spēlē! **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_menu():
    menu_list = ["1. Saskaitīšana", "2. Atņemšana", "3. Reizināšana", "4. Dalīšana", "5. Iziet"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])


def display_separator():
    print("-" * 24)


def get_user_input():
    user_input = int(input("Ievadiet savu izvēli: "))
    while user_input > 5 or user_input <= 0:
        print("Nepareiza opcija.")
        user_input = int(input("Lūdzu mēģini vēlreiz: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Ievadi savu atbildi")
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Pareizi.")
        return count
    else:
        print("Nepareizi.")
        return count


def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index is 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        problem = str(number_one) + " // " + str(number_two)
        solution = number_one // number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count


def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("Tu atbildēji", total, "jautājumiem ar", correct, "pareiziem.")
    print("Tavs rezultāts ir: ", percentage, "%.", sep = "")


def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Iziet no spēles.")
    display_separator()
    display_result(total, correct)

main()
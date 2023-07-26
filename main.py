# def intials(first_name, last_name, fathers_name):
#     if first_name[0].lower() == "j":
#       return "success!"
#     return f"{last_name.title()} {first_name[0].upper()}. {fathers_name[0].upper()}."
#     print("hello")
#
# def sum(number):
#             number += 1
#             if number <= 10:
#                 print(number)
#                 sum(number)
#             else:
                # return number
# def fib(first_number, second_number, end_number):
#     fib_numbers = []
#     while second_number <= end_number:
#         next_number = first_number + second_number
#         first_number = second_number
#         second_number = next_number
#         if second_number <= end_number:
#                 fib_numbers.append(next_number)
#
#     return fib_numbers
# import json
# if __name__ == "__main__":
#     print(fib(1, 2, 100))
#     with open("products(1)". json, "r") as file:
#         products = json.load(file)
#         omer_name = input("Vvedity imya")
#         if omer_name == "John Doe":
#             print("balance")
#         elif omer_name == "Jane Smith"
def sumNumbers(a, b):
     return a + b

def createInitials(name, last_name, fathers_name):
    initials = False
    try:
        initials = f"{last_name.capitalize()} {(name[0].upper())}. {fathers_name[0].upper()}."
    except Exception as err:
        print("сталась помилка в створенні ініціалів")
    return initials




def runProgram():
    sumNumbers(1, 2)
    initials = createInitials("Roman", "Pfayfer", "Andriyovich")
    if initials:
        print(initials)
    temperature = int(input("Введіть температуру"))
    if temperature > 0:
        print("Teplo")
    else:
        print("Cholodno")
if __name__ == "__main__":
    active = True
    while active:
        try:
            runProgram()
        except Exception as err:
            print(err)
        finally:
            ch = input("Чи бажаєте продовжити користування (Y/N): ")
            if ch.lower() == "n":
                active = False

# if __name__ == "__main__":
#     try:
#         num = int("test")
#     except  Exception as err:
#         try:
#             print(err)
#             print("помилка")
#         except Exception as err:
#             print(err)
#     finally:
#         print("Some text")

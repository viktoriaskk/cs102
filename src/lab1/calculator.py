def add(x, y):
    '''Сложение'''
    return x + y


def subtract(x, y):
    '''Вычитание'''
    return x - y


def multiply(x, y):
    '''Произведение'''
    return x * y


def divide(x, y):
    '''Деление'''
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"


# def test_calculator():
#     assert add(456, 353) == 809
#     assert subtract(1000, 548) == 452
#     assert multiply(59, 32) == 1888
#     assert divide(756, 9) == 84
#     assert divide(439, 0) == "Ошибка: деление на ноль"
#     print("Тесты пройдены успешно")

# test_calculator()

print("Выберите операцию:")
print("1)+")
print("2)-")
print("3)*")
print("4)/")


if __name__ == "__main__":
    while True:
        num1 = float(input("Введите первое число: "))
        choice = input("Введите номер операции: ")
        num2 = float(input("Введите второе число: "))

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Неверный ввод")

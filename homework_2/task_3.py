# Написать калькулятор с основными операциями(+, -, *, /)

number_1 = (input("Ввести первое число: "))
number_2 = (input("Ввести второе число: "))
arithmetic_operation = input("Ввести арифметическое действие: \n + \n - \n * \n / \n ")

print(eval(f'{number_1} {arithmetic_operation} {number_2}'))


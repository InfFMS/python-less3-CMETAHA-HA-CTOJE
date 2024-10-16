# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
count_nums_true = 0
count_nums_false = 0
number = int(input('>> '))
while number != 0:
    if number in range(10, 100): count_nums_true += 1
    else: count_nums_false += 1
    number = int(input('>> '))
print(f'Двузначных натуральных чисел: {count_nums_true}, остальных: {count_nums_false}.')

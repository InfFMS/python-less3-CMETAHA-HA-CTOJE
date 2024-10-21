#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
num_in = 1
plus_nums, minus_nums = 0, 0
while num_in != 0:
    num_in = int(input())
    if num_in > 0: plus_nums += 1
    elif num_in < 0: minus_nums += 1
print(f'Введено {plus_nums} положительных и {minus_nums} отрицательных чисел.')

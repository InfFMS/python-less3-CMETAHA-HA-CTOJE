# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
def if_pow_2(num):
    while num > 1:
        num /= 2
    if num == 1: return True
    else: return False

num_input = float(input('>> '))
count = 0
sum_nums_pow_2 = 0
while num_input != 0:
    if if_pow_2(num_input):
        count += 1
        sum_nums_pow_2 += num_input
    num_input = float(input('>> '))

if count == 0:
    print('нет')
else:
    print(sum_nums_pow_2 / count)


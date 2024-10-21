# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
number_input = float(input('>> '))
sum_nums_5 = 0
while number_input != 0:
    if number_input % 5 == 0:
        sum_nums_5 += number_input
    number_input = float(input('>> '))
print(sum_nums_5)


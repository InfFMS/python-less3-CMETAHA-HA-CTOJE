# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
num_input = float(input('>> '))
prevMaxNum = num_input
prevMinNum = num_input
while num_input != 0:
    if num_input > prevMaxNum:
        prevMaxNum = num_input
    elif num_input < prevMinNum:
        prevMinNum = num_input
    # Можно было решить с помощью массива и min(), max()
    num_input = float(input('>> '))


print(f'минимальное: {prevMinNum}, максимальное: {prevMaxNum}')


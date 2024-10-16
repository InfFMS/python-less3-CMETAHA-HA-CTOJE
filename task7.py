# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное из введённых чисел Фибоначчи.
# Вывести "нет", если чисел Фибоначчи в последовательности нет.
# Числа Фибоначчи – это последовательность чисел,
# которая начинается с двух единиц и каждое следующее число
# равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …


num_input = float(input('>> '))
nums_list = []
while num_input != 0:
    nums_list.append(num_input)
    num_input = float(input('>> '))


numsFib_list = [1, 1]
newNum = numsFib_list[-1] + numsFib_list[-2]
while newNum < int(max(nums_list)):
    newNum = numsFib_list[-1] + numsFib_list[-2]
    numsFib_list.append(newNum)

numsFib_in_input = [i for i in numsFib_list if i in nums_list]
print(numsFib_in_input)

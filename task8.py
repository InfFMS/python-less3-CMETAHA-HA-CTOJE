# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).
countPlus, countMinus = 0, 0
for i in range(int(input('N >> '))):
    num_in = int(input())
    if num_in > 0: countPlus += 1
    elif num_in < 0: countMinus += 1
print(countPlus, countMinus)




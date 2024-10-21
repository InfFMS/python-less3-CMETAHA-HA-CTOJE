# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
num_in_list = []
for i in range(int(input('N >> '))):
    num_in = int(input())
    if num_in // 10 in range(1, 10) and num_in % 3 == 0:
        num_in_list.append(num_in)
if num_in_list == []: print('нет')
else: print(max(num_in_list), min(num_in_list))

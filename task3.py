# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
def prime_numbers(n):
    numbers_set = set(range(2, n+1))
    numbers_list = []
    while numbers_set:
        numbers_list.append(min(numbers_set))
        numbers_set -= set(range(min(numbers_set), n + 1, min(numbers_set)))
    return numbers_list

numbers_input_list = []
num_input = int(input())
while num_input != 0:
    numbers_input_list.append(num_input)
    num_input = int(input())

prime_list = prime_numbers(max(numbers_input_list))

prime_count_in_input = 0
for i in numbers_input_list:
    if i in prime_list:
        prime_count_in_input += 1

print(f'Введено простых: {prime_count_in_input}, а составных: {len(numbers_input_list)-prime_count_in_input}.')
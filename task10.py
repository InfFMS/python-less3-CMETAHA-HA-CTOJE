# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".

def get_primes(n):
    n += 1
    sieve = [True] * n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
        for i in range(p * p, n, p):
            sieve[i] = False
    return primes[-1]


num_prime_list = []
for i in range(int(input('N >> '))):
    num_in = int(input())
    if num_in == get_primes(num_in):
        num_prime_list.append(num_in)

if len(num_prime_list) == 0: print('нет')
elif min(num_prime_list) == max(num_prime_list): print(min(num_prime_list))
else:print(min(num_prime_list), max(num_prime_list))


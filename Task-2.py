import cProfile
import timeit
from timeit import timeit
from cProfile import run


def test(num, a=10000):
    sieve = [i for i in range(a)]
    sieve[1] = 0
    for i in range(2, a):
        if sieve[i] != 0:
            j = i + i
            while j < a:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество чисел в диапазоне до {a}: {len(res)}')

    assert num < len(res)
    return res[num - 1]


def Eratosthenes(a):
    count = 1
    start = 3
    end = 4 * a

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if a == 1:
        return 2

    while count < a:

        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1
                if count == a:
                    return sieve[i]
                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * a
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


print(timeit('Eratosthenes(2)', number=100, globals=globals()))  # 0.00010220000000000021
print(timeit('Eratosthenes(4)', number=100, globals=globals()))  # 0.0001808000000000018
print(timeit('Eratosthenes(8)', number=100, globals=globals()))  # 0.00033309999999999937
print(timeit('Eratosthenes(16)', number=100, globals=globals()))  # 0.000733000000000001
print(timeit('Eratosthenes(32)', number=100, globals=globals()))  # 0.004199700000000001
print(timeit('Eratosthenes(64)', number=100, globals=globals()))  # 0.0105278

run('Eratosthenes(100)')
run('Eratosthenes(1000)')
run('Eratosthenes(10000)')


#        353 function calls in 0.000 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task-2.py:23(Eratosthenes)
#        1    0.000    0.000    0.000    0.000 Task-2.py:28(<listcomp>)
#        1    0.000    0.000    0.000    0.000 Task-2.py:47(<listcomp>)
#        1    0.000    0.000    0.000    0.000 Task-2.py:50(<listcomp>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      345    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


#         4289 function calls in 0.019 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#        1    0.018    0.018    0.019    0.019 Task-2.py:23(Eratosthenes)
#        1    0.000    0.000    0.000    0.000 Task-2.py:28(<listcomp>)
#        2    0.000    0.000    0.000    0.000 Task-2.py:47(<listcomp>)
#        2    0.000    0.000    0.000    0.000 Task-2.py:50(<listcomp>)
#        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#     4278    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


#         48786 function calls in 3.162 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    3.162    3.162 <string>:1(<module>)
#        1    3.149    3.149    3.162    3.162 Task-2.py:23(Eratosthenes)
#        1    0.003    0.003    0.003    0.003 Task-2.py:28(<listcomp>)
#        4    0.002    0.001    0.002    0.001 Task-2.py:47(<listcomp>)
#        4    0.005    0.001    0.005    0.001 Task-2.py:50(<listcomp>)
#        1    0.000    0.000    3.162    3.162 {built-in method builtins.exec}
#    48769    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

# Время выполнения нарастает.

def search(a):
    count = 1
    num_ = 1
    prime = [2]

    if a == 1:
        return 2

    while count != a:
        num_ += 2

        for num in prime:
            if num_ % num == 0:
                break
        else:
            count += 1
            prime.append(num_)

    return num_



print(timeit('search(2)', number=100, globals=globals())) # 7.489999999998886e-05
print(timeit('search(4)', number=100, globals=globals())) # 7.149999999978007e-05
print(timeit('search(8)', number=100, globals=globals())) # 0.00021929999999992233
print(timeit('search(16)', number=100, globals=globals())) # 0.0011996000000000784
print(timeit('search(32)', number=100, globals=globals())) # 0.004377499999999923
print(timeit('search(64)', number=100, globals=globals())) # 0.015709699999999938

run('search(100)')
run('search(1000)')
run('search(10000)')

a = 300
#        103 function calls in 0.000 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task-2.py:115(search)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         1003 function calls in 0.019 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#        1    0.019    0.019    0.019    0.019 Task-2.py:115(search)
#        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         10003 function calls in 1.966 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.966    1.966 <string>:1(<module>)
#        1    1.965    1.965    1.966    1.966 Task-2.py:115(search)
#        1    0.000    0.000    1.966    1.966 {built-in method builtins.exec}
#     9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Время выполнения нарастает.
# Время работы алгоритиов примерно одинаково.
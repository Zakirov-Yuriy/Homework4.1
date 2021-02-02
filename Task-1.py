# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import cProfile
import timeit
from timeit import timeit
from cProfile import run

MIN_DIV = 2
MAX_DIV = 20

def div_count(m):
    div_dict = dict()
    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = m // div

    return div_dict

print(timeit('div_count(2)', number=100, globals=globals())) # 0.0001567999999999986
print(timeit('div_count(4)', number=100, globals=globals())) # 0.00037840000000000096
print(timeit('div_count(8)', number=100, globals=globals())) # 0.0004236999999999991
print(timeit('div_count(16)', number=100, globals=globals())) # 0.00015130000000000005
print(timeit('div_count(32)', number=100, globals=globals())) # 0.00015070000000000014
print(timeit('div_count(64)', number=100, globals=globals())) # 0.00038619999999999974

run('div_count(100)')
run('div_count(1000)')
run('div_count(10000)')
run('div_count(100000)')
run('div_count(1000000)')

#4 function calls in 0.000 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task-1.py:13(div_count)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# Алгоритм работает быстро, в оптимизации не нуждается.


def div_count_2(m):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = 0
        for num in range(2, m + 1):
            if num % div == 0:
                div_dict[div] += 1

    return div_dict

print(timeit('div_count_2(2)', number=100, globals=globals())) # 0.0010986000000000051
print(timeit('div_count_2(4)', number=100, globals=globals())) # 0.0014042000000000013
print(timeit('div_count_2(8)', number=100, globals=globals())) # 0.0018617999999999968
print(timeit('div_count_2(16)', number=100, globals=globals())) # 0.0031576000000000035
print(timeit('div_count_2(32)', number=100, globals=globals())) # 0.0053097000000000005
print(timeit('div_count_2(64)', number=100, globals=globals())) # 0.009799700000000001

run('div_count_2(100)')
run('div_count_2(1000)')
run('div_count_2(10000)')
run('div_count_2(100000)')
run('div_count_2(1000000)')

#4 function calls in 0.000 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task-1.py:42(div_count_2)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#4 function calls in 0.001 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 Task-1.py:42(div_count_2)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#4 function calls in 0.016 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#        1    0.016    0.016    0.016    0.016 Task-1.py:42(div_count_2)
#        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#4 function calls in 0.129 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.129    0.129 <string>:1(<module>)
#        1    0.129    0.129    0.129    0.129 Task-1.py:42(div_count_2)
#        1    0.000    0.000    0.129    0.129 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#4 function calls in 1.205 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.205    1.205 <string>:1(<module>)
#        1    1.205    1.205    1.205    1.205 Task-1.py:42(div_count_2)
#        1    0.000    0.000    1.205    1.205 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#Время выполнения нарастает линейно.


def div_count_3(m):
    div_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(2, m + 1):
        if num % 2 == 0:
            div_dict[2] += 1
        if num % 3 == 0:
            div_dict[3] += 1
        if num % 4 == 0:
            div_dict[4] += 1
        if num % 5 == 0:
            div_dict[5] += 1
        if num % 6 == 0:
            div_dict[6] += 1
        if num % 7 == 0:
            div_dict[7] += 1
        if num % 8 == 0:
            div_dict[8] += 1
        if num % 9 == 0:
            div_dict[9] += 1

    return div_dict

print(timeit('div_count_3(2)', number=100, globals=globals())) # 8.570000000007738e-05
print(timeit('div_count_3(4)', number=100, globals=globals())) # 0.00015079999999989546
print(timeit('div_count_3(8)', number=100, globals=globals())) # 0.00030090000000004835
print(timeit('div_count_3(16)', number=100, globals=globals())) # 0.0005730999999999931
print(timeit('div_count_3(32)', number=100, globals=globals())) # 0.0011296000000000639
print(timeit('div_count_3(64)', number=100, globals=globals())) # 0.0021849999999998815

run('div_count_3(100)')
run('div_count_3(1000)')
run('div_count_3(10000)')
run('div_count_3(100000)')
run('div_count_3(1000000)')

#        4 function calls in 0.000 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task-1.py:112(div_count_3)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.000 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task-1.py:112(div_count_3)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.004 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#        1    0.004    0.004    0.004    0.004 Task-1.py:112(div_count_3)
#        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.036 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.036    0.036 <string>:1(<module>)
#        1    0.036    0.036    0.036    0.036 Task-1.py:112(div_count_3)
#        1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.432 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.432    0.432 <string>:1(<module>)
#        1    0.432    0.432    0.432    0.432 Task-1.py:112(div_count_3)
#        1    0.000    0.000    0.432    0.432 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

m = 99
print(div_count(m))
print(div_count_2(m))
print(div_count_3(m))

#Время выполнения нарастает линейно.
# Вывод:
# Алгоритм, использованный в функции div_count(), является самым оптимальным.

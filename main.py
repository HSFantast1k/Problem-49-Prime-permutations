import itertools
import time


def is_prime(num):
    for div in range(2, num):
        if num % div == 0:
            return False
    return True


def convers(num):
    list_perm = []
    for i in itertools.permutations(num):
        a = int("".join([str(k) for k in i]))
        if is_prime(a):
            list_perm.append(a)
    return list_perm


def no_name(number):
    list_perm = convers(number)
    for i in range(len(list_perm)):
        for k in range(1, len(list_perm) - 1):
            difference = list_perm[k] - list_perm[i]
            if difference + list_perm[k] in list_perm:
                return [list_perm[i], list_perm[k], difference + list_perm[k], difference]


number = 999
while number < 9999:
    number += 1
    temp = no_name(list(str(number)))
    if temp:
        if temp[-1] > 0:
            print(temp)

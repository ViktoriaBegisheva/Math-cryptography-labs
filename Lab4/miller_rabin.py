# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:11:29 2023

@author: User
"""


import random

def evklid(a, b): # Функція знаходження найбільшого спільного дільника
    if a % b == 0:
        return b
    else:
        return evklid(b, a%b)

def _miller_rabin_helper(d: int, n: int) -> bool:
    # a - random number in [2..n-2]
    a = 2 + random.randint(1, n - 4)
    if evklid(n, a)!=1:
        return False
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def miller_rabin(n: int, k=12) -> bool:
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    # n - 1 =  2^t * m for t >=0, m >= 1
    d = n - 1
    t=0
    while d % 2 == 0:
        d //= 2
        t+=1
    m=d
    #print("-",n-1,t,m)
    # Iterate given number of 'k' times
    for _ in range(1):
        if not _miller_rabin_helper(d, n):
            return False
    return True


if __name__ == '__main__':
    # for test
    # output all prime numbers from 0 to 100
    for i in range(3, 100):
        if miller_rabin(i):
            print(i, end=" ")
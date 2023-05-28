# -*- coding: utf-8 -*-
"""
Created on Sat May 27 05:30:57 2023

@author: User
"""


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def fun(a):
    l = [1]
    for i in range(2, a+1):
        if a % i == 0:
            l.append(i)
    return l


def Z_(p):
    z = []
    for i in range(1, p):
        if gcd(p, i) == 1:
            z.append(i)
    return z


def deg_elem(g, Z):
    n = len(Z)
    p = Z[-1]+1
    deg = fun(n)
    for a in deg:
        if g**a % p == 1:
            return(a)
    return 0


def task(p):
    Z = Z_(p)
    n = len(Z)
    print("phi(p) =", n)
    for g in Z:
        d = deg_elem(g, Z)
        print(g, d)
        if d == n:
            print("el", g, "- deg =", d, "== n")
            print("group cyclic")
            return g
    return None


if __name__ == "__main__":
    p = 49
    task(p)

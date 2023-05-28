# -*- coding: utf-8 -*-
"""
Created on Sun May 28 04:13:44 2023

@author: User
"""
from baby_gigant_steps import baby_gigant_steps as log
import random


def secret(p, g, a, b):
    pk_a = pow(g, a, p)
    print('pk_a =', pk_a)
    pk_b = pow(g, b, p)
    print('pk_b =', pk_b)
    sk_1 = pow(pk_b, a, p)
    sk_2 = pow(pk_a, b, p)
    print(sk_1 == sk_2)
    print("secret key =", sk_1)

    #print("a = ",log(p,g, pk_a))
    #print("b =",log(p,g, pk_b))
    return pk_a, pk_b, sk_1


p = 467
g = 4

a = random.randint(3, p - 2)
b = random.randint(3, p - 2)

a = 400
b = 134
print('a =', a, ' b =', b)
secret(p, g, a, b) 

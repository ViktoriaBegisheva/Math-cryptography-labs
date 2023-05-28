# -*- coding: utf-8 -*-
"""
Created on Sat May 27 05:13:23 2023

@author: User
"""


def baby_steps(p, g, h):
    n = int((p-1)**(1/2))+1
    deg = []
    #print("\nbaby step")
    for a in range(1, n+1):
        g_a = g**a % p
        deg.append(g_a)
        #print(g,"^",a,"=",g_a)
        if g_a == h:
            #print("log_", g, "(", h, ")=", a)
            return g_a
    return deg


def gigant_steps(p, g, h, deg):
    n = int((p-1)**(1/2))+1
    #print("\ngiant step")
    g_1 = pow(g, -n, p)
    #print(g_1)
    for a in range(1, n+1):
        g_a = h*g_1**a % p
        #print(h, "*", g_1, "^", a, "=", g_a)
        if g_a in deg:
            #print("deg in deg --", deg.index(g_a)+1)
            return a, deg.index(g_a)+1


def baby_gigant_steps(p, g, h):
    n = int((p-1)**(1/2))+1

    deg = baby_steps(p, g, h)
    #print(deg)
    if type(deg)==int:
        return deg
    a, a0 = gigant_steps(p, g, h, deg)
    #print()
    # g_a = h*g^(-n*a) = g*a0
    # log_g(h) = a*n + a0
    #print("log_", g, "(", h, ") =", a*n+a0)
    return a*n+a0


if __name__ == "__main__":
    p = 101
    g = 3
    h = 37
    print(baby_gigant_steps(p, g, h))



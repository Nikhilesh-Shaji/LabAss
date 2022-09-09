# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:05:31 2022

@author: 20pt19
"""

import sympy as sp

def bisection(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

f = lambda x: sp.sin(x)
approx_phi = bisection(f,-1,1,25)
print(approx_phi)

f1 = lambda x: sp.cos(x) + 3*x -x
f2 = lambda x: sp.cos(x) - sp.exp(x)*x
f3 = lambda x: x**3 + 2*x**2 + 10*x -20
f4 = lambda x: x - sp.cos(x)
f5 = lambda x: sp.exp(x) * (x**2+5*x+2) + 1
f6 = lambda x: x - sp.sin(x) - 1/2
f7 = lambda x: x * sp.exp(x) - 3
f8 = lambda x: x * sp.cos(x/(x-2))
f9 = lambda x: x**2 - sp.sin(x)/x
f10 = lambda x: sp.tan(x) - x - 1
f11 = lambda x: 3*x + sp.sin(x) - sp.exp(x)
f12 = lambda x: sp.exp(-x)

import numpy as np
from scipy import integrate
from math import exp, log1p, abs, pi
from cmath import sqrt

def prA():
    k=3
    log_laur = lambda t: log1p(abs(Laurent(k,exp(2*math.pi*cmath.sqrt(-1)*t))))
    integrand=integrate.quad(log_laur,0,1)
    print exp(integrand)

def Laurent(k,z):
    sum = 0
    for i in range(1,k+1):
        sum+=((z**i)+(z**((-1)*i)))
    return 2*k-sum

prA()


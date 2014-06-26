#!/usr/bin/env python
# coding: utf-8

#------------ Fibonacci numbers START ----------------#

def fibo(rng=10):
    
    fibs = sum(range(1,rng+1))   
     
    print fibs
    return (fibs)

#------------ Fibonacci numbers END -------------------#

import sys
try:
    rng = int(sys.argv[1])
except:
    rng = 10

fibo(rng)

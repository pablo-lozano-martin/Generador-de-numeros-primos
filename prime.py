import random as rn
import math

def generate_number(num):
    
    n = rn.randrange(1,10,2) 
    
    for i in range(num-2):
        n = n*10 + rn.randint(0, 9)
    
    odd_number = rn.randrange(1,10,2)
    n = n*10 + odd_number
    
    return n

def factorized_number(n):
    num = n-1
    s = 0
    while (num%2 == 0):
        s += 1
        num = num/2
    r = math.trunc(num)
    
    return r, s

def miller_rabin(n):
    r, s = factorized_number(n)
    a = rn.randrange(1,n-1)
          
    cond1 = (a**r)%n != 1
    cond2 = True
    for j in range(0, s-1):
        cond2 = (a**((2^j) * r))%n != n-1
        if (not cond2): break
    if(not cond1 or not cond2): return True
    return False

def generate_prime_number(num):
    cont = True
    while(cont):
        n = generate_number(num)
        check = 0
        for i in range(1,10):
            if (miller_rabin(n)):
                check += 1
            else: break
            if (check == 9): cont = False
    print(n)

generate_prime_number(int(input()))
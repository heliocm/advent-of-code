from math import *
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]
 
def printDivisors (n):
    divisors = []
    i = 1
    while (i * i < n):
        if (n % i == 0):
            divisors.append(i)
 
        i += 1
 
    for i in range(int(sqrt(n)), 0, -1):
        if (n % i == 0):
            divisors.append(n // i)
    return divisors
number = int(data[0])//10

i = 0
while sum(printDivisors(i)) < number:
    i += 1

print(i)
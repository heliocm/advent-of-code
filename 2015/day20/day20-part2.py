from math import *
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]
 
def find_divisors (n):
    divisors = []
    i = 1
    while (i * i < n):
        if (n % i == 0):
            divisors.append(i)
 
        i += 1
 
    for i in range(int(sqrt(n)), 0, -1):
        if (n % i == 0):
            divisors.append(n // i)
    real_divisors = []
    for each in divisors:
        if each * 50 >= n:
            real_divisors.append(each)
    return real_divisors
number = int(data[0])
print(number)
print(find_divisors(200))
i = 655200
# i = 0
while (sum(find_divisors(i)) * 11) <= number:
    i += 1

print(i)
print(find_divisors(i))
'''
Problem Statement -: In this even odd problem Given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.

Calculate the number of all such permutations.

As this number can be large, print it modulo (1e9 +7).

Constraints

0 <= low <= high <= 10^9
K <= 10^6.
Input

First line contains two space separated integers denoting low and high respectively
Second line contains a single integer K.
Output

Print a single integer denoting the number of all such permutations
Time Limit

1
'''

rangeOfvalues = input().split(" ")

k = int(input())

lower = int(rangeOfvalues[0])
higher = int(rangeOfvalues[1])

total = higher - lower + 1

if higher%2 == 0:
    if lower%2 == 0:
        n = (higher-lower)/2 +1
        
    else:
         n = (higher-lower-1)/2 +1
         
else:
    if lower%2 == 0:
        n = (higher-1-lower)/2 +1
        
    else:
         n = (higher-lower-2)/2 +1
         
comb = n**k

i = 2
def factorial(m):
    if m == 1 or m == 0:
        return 1
    else:
        return m*factorial(m-1)
    

def ncr(n,k):
    nFact = factorial(n)
    kFact = factorial(k)
    nkFact = factorial(n-k)
    return nFact//(kFact*nkFact)
    

while True:
    if k//i==0:
        break
    else:
        comb+= ncr(k,i)*n**(k-i)*(total - n)**i
        
        i += 2
        
print(round(comb))

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

'''
abcde
01234
-4-3-2-1
In this 3 Palindrome, Given an input string word, split the string into exactly 3 palindromic substrings. Working from left to right, choose the smallest split for the first substring that still allows the remaining word to be split into 2 palindromes.

Similarly, choose the smallest second palindromic substring that leaves a third palindromic substring.

If there is no way to split the word into exactly three palindromic substrings, print “Impossible” (without quotes). Every character of the string needs to be consumed.

Cases not allowed –

After finding 3 palindromes using above instructions, if any character of the original string remains unconsumed.
No character may be shared in forming 3 palindromes.

'''

def palindrome(param):
    
    n = len(param)
    str1 = param[0:n//2]
    str2 = param[-1:-1*(n//2+1):-1]
    if str1==str2:
        return True
    else:
        return False
    
    
data = str(input())

found = False
if len(data)>=3:    
    for i  in range(1,len(data)-2):
        str1 = data[0:i]
        if palindrome(str1):
            for j in range(1,len(data[i:])):
                str2 = data[i:i+j]
                str3 = data[i+j:]
                if palindrome(str2) and palindrome(str3):
                    
                    found = True
                    break
        if found :
            print(str1+"\n"+str2+"\n"+str3,end="")
            break
if not(found):
    print("Imposible")
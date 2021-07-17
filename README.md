#Problem Description
#1.
In this 3 Palindrome, Given an input string word, split the string into exactly 3 palindromic substrings. Working from left to right, choose the smallest split for the first substring that still allows the remaining word to be split into 2 palindromes.

Similarly, choose the smallest second palindromic substring that leaves a third palindromic substring.

If there is no way to split the word into exactly three palindromic substrings, print “Impossible” (without quotes). Every character of the string needs to be consumed.

Cases not allowed –

After finding 3 palindromes using above instructions, if any character of the original string remains unconsumed.
No character may be shared in forming 3 palindromes.

#Constraint
1 <= the length of input sting <= 1000

#Input

First line contains the input string consisting of characters between [a-z].
#Output

Print 3 substrings one on each line.
#Time Limit

1

#Examples

##Example 1

###Input

nayannamantenet

###Output

nayan

naman

tenet

##Explanation

- The original string can be split into 3 palindromes as mentioned in the output.
- However, if the input was nayanamantenet, then the answer would be “Impossible”.
##Example 2

###Input

aaaaa

###Output

a

a

aaa

##Explanation

- The other ways to split the given string into 3 palindromes are as follows –
[a, aaa, a], [aaa, a, a], [aa, aa, a], etc.
- Since we want to minimize the length of the first palindromic substring using left to right processing, the correct way to split is [a, a, aaa].

##Example 3

###Input

aaaabaaaa

###Output

a

aaabaaa

a

##Explanation

- The other ways to split the given string into 3 palindromes are as follows –
[aaaa, b, aaaa], [aa, aabaa, aa], etc.
- Since we want to minimize the length of the first palindromic substring using left to right processing, the correct way to split is [a, aaabaaa, a].

---

#2.
n this even odd problem Given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.

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

Examples

Example 1

Input

4 5

3

Output

4

Explanation

There are 4 valid permutations viz. {4, 4, 4}, {4, 5, 5}, {5, 4, 5} and {5, 5, 4} which sum up to an even number.

Example 2

Input

1 10

2

Output

50

Explanation

There are 50 valid permutations viz. {1,1}, {1, 3},.. {1, 9} {2,2}, {2, 4},… {2, 10} . . . {10, 2}, {10, 4},… {10, 10}. These 50 permutations, each sum up to an even number.

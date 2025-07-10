# given a string test for palindrome over any of its permutation.
# input edified
# output deified
from collections import Counter
N = input()
c = Counter(N)
oddChar = 0

for i in c.values():
    if i%2 == 1 :
        oddChar += 1

if oddChar > 1:
    print("False")
else:
    print("True")        
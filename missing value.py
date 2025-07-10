n = int(input())
num = list(map(int, input().split() ))
m = n*(n+1)//2
s = sum(num)
missing_number = m - s
print(missing_number)
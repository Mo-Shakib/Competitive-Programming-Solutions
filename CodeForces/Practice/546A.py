# https://codeforces.com/problemset/problem/546/A
k, n, w = map(int, input().split())
total = 0
for i in range(1, w+1):
    total += (k*i)

print(total - n)
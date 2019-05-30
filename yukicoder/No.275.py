import math

N = int(input())
A = list(map(int, input().split()))

A.sort()
N2 = math.floor(N / 2)
if N % 2 == 0:
    ans = (A[N2 - 1] + A[N2]) / 2
    print(ans)
else:
    ans = A[N2]
    print(ans)

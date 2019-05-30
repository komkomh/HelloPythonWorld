N: int = int(input())
A = list(map(int, input().split()))
V: int = int(input())

diff = sum(A) - V
print(str(diff))

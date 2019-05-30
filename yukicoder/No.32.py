import math

L = int(input())
M = int(input())
N = int(input())
amount = L * 100 + M * 25 + N * 1

amount = amount % 1000
hyaku = math.floor(amount / 100)
amount = amount % 100
nigo = math.floor(amount / 25)
amount = amount % 25
ichi = math.floor(amount / 1)

maisu = hyaku + nigo + ichi
print(maisu)

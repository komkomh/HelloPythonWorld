N: int = int(input())
V = list(map(int, input().split()))

for i in range(0, len(V)):
    minus2 = 0
    if i - 2 >= 0:
        minus2 = V[i - 2]

    minus3 = 0
    if i - 3 >= 0:
        minus3 = V[i - 3]

    if minus2 > minus3:
        V[i] += minus2
    else:
        V[i] += minus3

print(max(V))

N: int = int(input())
X = list(map(int, input().split()))

X.sort()

min_distance = 0
for i in range(1, len(X)):
    distance = abs(X[i] - X[i - 1])
    if distance == 0:
        continue

    if min_distance == 0 or distance < min_distance:
        min_distance = distance

print(str(min_distance))

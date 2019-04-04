A, B = map(int, input().split())


def has3(s: str):
    for i in range(len(s)):
        if int(s[i]) == 3:
            return True


for i in range(A, B + 1):
    s = str(i)
    if i % 3 == 0 or has3(s):
        print(i)

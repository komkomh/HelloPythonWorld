def strToNumber(s: str):
    if s.isnumeric():
        return int(s)
    return 0


S = input()
sum = 0
for i in range(len(S)):
    sum += strToNumber(S[i])

print(sum)

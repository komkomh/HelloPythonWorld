def turnUpLow(s: str):
    if s.islower():
        return s.upper()
    if s.isupper():
        return s.lower()
    return s


S = input()

turned = ""
for i in range(len(S)):
    turned += turnUpLow(S[i])

print(turned)

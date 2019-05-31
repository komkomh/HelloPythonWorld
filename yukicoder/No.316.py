N: int = int(input())
abc = map(int, input().split())

# a, b, c = map(int, input().split())

print(str(N))
for i in abc:
    print(str(i) + " ", end="")


ignores = []
for i in abc:
    for j in abc:
        if i == j:
            continue
        if i % j == 0:
            ignores.append(i)

for ignore in ignores:
    print(str(ignore))


a_count = N // a
b_count = N // b
c_count = N // c
print("a_count = " + str(a_count))
print("b_count = " + str(b_count))
print("c_count = " + str(c_count))

sum = a_count + b_count + c_count
print("sum = " + str(sum))

ab_count = N // (a * b)
ac_count = N // (a * c)
bc_count = N // (b * c)
abc_count = N // (a * b * c)

print("ab_count = " + str(ab_count))
print("ac_count = " + str(ac_count))
print("bc_count = " + str(bc_count))
print("abc_count = " + str(abc_count))

dup = ab_count + ac_count + bc_count
print("dup = " + str(dup))

ans = sum - dup + abc_count
print(str(ans))

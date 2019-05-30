N, K = map(int, input().split())

# 0:グー 1:チョキ 2:パー
if N == 0:
    if K == 0:
        print("Drew")
    if K == 1:
        print("Won")
    if K == 2:
        print("Lost")

if N == 1:
    if K == 0:
        print("Lost")
    if K == 1:
        print("Drew")
    if K == 2:
        print("Won")

if N == 2:
    if K == 0:
        print("Won")
    if K == 1:
        print("Lost")
    if K == 2:
        print("Drew")

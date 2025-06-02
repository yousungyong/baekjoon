a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

def check_O_n(a1, a0, c, n0):
    for i in range(n0, 101):
        if a1 * i + a0 > c * i:
            return 0
    return 1

print(check_O_n(a1, a0, c, n0))
A = int(input())
B = int(input())

d = B // 100
e = (B // 10) - (d * 10)
f = B % 10

print(A * f)
print(A * e)
print(A * d)
print(A * B)

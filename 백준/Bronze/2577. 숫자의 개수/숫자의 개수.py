A = int(input())
B = int(input())
C = int(input())

M = str(A*B*C)

for i in range(10):
  j = str(i)
  print(M.count(j))

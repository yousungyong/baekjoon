A = [1,1,2,2,2,8]
B = list(map(int,input().split()))
result = []

for i in range(6):
  C = A[i] - B[i]
  result.append(C)

print(' '.join(map(str,result)))
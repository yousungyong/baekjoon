T = int(input())
for i in range(T):
  A = list(map(int,input().split()))

  N = A[0]
  sum = 0
  count = 0

  for i in range(1,len(A)):
    sum += A[i]
  avg = sum / A[0]
    
  for i in range(1,len(A)):
    if A[i] > avg :
      count += 1

  rate = count / A[0] * 100
  print ("{:.3f}%".format(rate))

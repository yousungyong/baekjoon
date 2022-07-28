N,X = map(int, input().split())
b = list(map(int, input().split()))

for i in range(len(b)) :
  if b[i] < X :
    print (b[i])


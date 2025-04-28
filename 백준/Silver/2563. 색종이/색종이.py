n = int(input())

array = [[i for i in range(1,101)] for j in range(1,101)]

for i in range(n):
  x,y = map(int, input().split())
  for j in range(x,x+10):
    for k in range(y,y+10):
      array[j][k] = 0

count = 0
for row in array:
    for elem in row:
        if elem == 0:
            count += 1

print(count)


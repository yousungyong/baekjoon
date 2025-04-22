NM = list(map(int, input().split()))
N = NM[0]

list_1 = []
list_2 = []
list_3 = []

for i in range(N):
    list_1.append(list(map(int,input().split())))

for i in range(N):
    list_2.append(list(map(int,input().split())))
    list_3.append([x + y for x, y in zip(list_1[i], list_2[i])])

for row in list_3:
  print(' '.join(map(str, row)))


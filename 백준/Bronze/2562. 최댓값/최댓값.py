lst = []
for i in range(9):
  N = int(input())
  lst.append(N)

M = max(lst)
print(M)
print(lst.index(M)+1)


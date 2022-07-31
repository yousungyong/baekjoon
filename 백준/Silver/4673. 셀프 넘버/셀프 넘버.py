def d(n):
  d = n
  n = str(n)
  for i in range(len(n)):
    d += int(n[i])
  return d
  
lst = []
for i in range(10000):
  lst.append(i)
# print(lst)

for i in range(10000):
  # print(d(i))
  if d(i) in lst :
    lst.remove(d(i))

for i in lst:
  print(i)

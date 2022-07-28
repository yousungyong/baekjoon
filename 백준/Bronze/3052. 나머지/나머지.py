lst1 = []
count = 0

for i in range(10):
  A = int(input())
  lst1.append(A)

lst2 = [lst1[0]%42]
y = ""

for i in range(1,len(lst1)) :
  for j in lst2 :
    if j == lst1[i]%42 :
      y = "같은거 있음"
  if y != "같은거 있음" :
    lst2.append(lst1[i]%42)
  else :
    y = ""
  
print (len(lst2))
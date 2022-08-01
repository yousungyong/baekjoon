n2 = "ABC"
n3 = "DEF"
n4 = "GHI"
n5 = "JKL"
n6 = "MNO"
n7 = "PQRS"
n8 = "TUV"
n9 = "WXYZ"

TE = input()
time = 0

for i in TE :
  if i in n2 :
    time += 3
  elif i in n3 : 
    time += 4
  elif i in n4 : 
    time += 5
  elif i in n5 : 
    time += 6
  elif i in n6 : 
    time += 7
  elif i in n7 : 
    time += 8
  elif i in n8 : 
    time += 9
  else : 
    time += 10

print(time)

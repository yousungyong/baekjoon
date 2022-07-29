S,T = input().split()
RS = "".join(reversed(S))
RT = "".join(reversed(T))

if int(RS) > int(RT) :
  print(RS)
else :
  print(RT)
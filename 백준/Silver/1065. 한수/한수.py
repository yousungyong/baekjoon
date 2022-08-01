N = input()

def han(N) :  
  arr = []
  for i in range(len(N)):
    arr.append(int(N[i]))

  for i in range(len(arr)-1):
    arr[i] = arr[i+1] - arr[i]
  arr.pop()
  
  if len(N) <= 2 :
    return N
  else : 
    if len(list(set(arr))) == 1 :
      return N
    else :
      return None

count = 0
for i in range(1,int(N)+1):
  if han(str(i)) != None :
    count += 1

print (count)


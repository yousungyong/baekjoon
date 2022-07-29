S = input()
lst =[]
for i in range(26):
  count  = 0
  for j in S.lower():
    if j == chr(i+97):
      count += 1
  lst.append(count)
if lst.count(max(lst)) >= 2:
  print ("?")
else :
  print(chr(lst.index(max(lst))+65))
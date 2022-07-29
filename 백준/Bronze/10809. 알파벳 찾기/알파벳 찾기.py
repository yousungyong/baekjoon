S = input()
for j in range(26):
  for i in range(len(S)):
    print(S.find(chr(j+97)), end=" ")
    break
T = int(input())

for i in range(T):
  score = 0
  a = input()

  sp = a.split('X')
  sp_len = len(sp)
  for i in range(sp_len):
    for j in range(1,len(sp[i])+1):
      score += j
  print(score)


W = []
for i in range(5):
  W.append(list(str(input())))

R = []

for i in range(15):
  for j in range(5):
    try:
      value = W[j][i]
      R.append(W[j][i])
    except IndexError:
      pass
    
print(''.join(R))
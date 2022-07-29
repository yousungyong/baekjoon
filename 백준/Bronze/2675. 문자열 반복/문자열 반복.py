T = int(input())
for i in range(T):
  N,S = map(str,input().split())
  N = int(N)

  for i in range(len(S)):
    print(S[i]*N,end="")
  print()
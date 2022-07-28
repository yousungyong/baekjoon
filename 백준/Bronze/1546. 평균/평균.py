N = int(input())

score = list(map(int,input().split()))

max = max(score)
sum = 0
for i in range(len(score)):
  score[i] = score[i]/max*100
  sum += score[i]

print (sum/len(score))


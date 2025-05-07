A,B,V = map(int, input().split())
day = 0
# V <= (A - B)(day - 1) + A
# V - A <= (A - B)(day - 1)
# V - A <= (A - B)day - A + B
# V - B <= (A - B)day
# day >= (V - B)/(A - B)
# day는 (V - B)/(A - B)보다 크거나 같은 가장 작은 정수

if (V - B)/(A - B) == int((V - B)/(A - B)):
  day = int((V - B)/(A - B))
else:
  day = int((V - B)/(A - B)) + 1

print(day)
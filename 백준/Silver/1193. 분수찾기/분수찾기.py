X = int(input())

for i in range(5000):
  X -= i
  if X <= 0:
    n = i
    break

if n % 2 == 1:
    print(f"{-X+1}/{n+X}")
else:
    print(f"{n+X}/{-X+1}")
# 세 점을 입력받음
xs = []
ys = []

for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

# x 좌표 중 하나만 있는 값을 찾음
for x in xs:
    if xs.count(x) == 1:
        x4 = x

# y 좌표 중 하나만 있는 값을 찾음
for y in ys:
    if ys.count(y) == 1:
        y4 = y

print(x4, y4)

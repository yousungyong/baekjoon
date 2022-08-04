N = int(input())
count = N
for i in range(N):
    X = input()

    lst = [X[0]]
    tmp = X[0]

    for i in X :
        if tmp == i:
            pass
        else:
            if i in lst:
                count -= 1
                break
            else:
                lst.append(i)
                tmp = i
               

print(count)

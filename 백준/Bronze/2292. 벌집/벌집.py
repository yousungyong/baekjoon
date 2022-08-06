N = int(input())
room=1
count=1

while 1:
    if N > room :
        room += 6*count
        count += 1
        continue
    else :
        break

print(count)
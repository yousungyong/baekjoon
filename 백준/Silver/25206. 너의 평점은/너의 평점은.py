grade = []

for i in range(20):
    grade.append(list(map(str, input().split())))

col_2 = [row[1] for row in grade]
col_3 = [row[2] for row in grade]
sum = 0
credit = 0

for i in range(20):
    if col_3[i] == 'A+':
      col_3[i] = 4.5
    elif col_3[i] == 'A0':
      col_3[i] = 4.0
    elif col_3[i] == 'B+':
      col_3[i] = 3.5      
    elif col_3[i] == 'B0':
      col_3[i] = 3.0      
    elif col_3[i] == 'C+':
      col_3[i] = 2.5
    elif col_3[i] == 'C0':
      col_3[i] = 2.0
    elif col_3[i] == 'D+':
      col_3[i] = 1.5
    elif col_3[i] == 'D0':
      col_3[i] = 1.0
    elif col_3[i] == 'F':
      col_3[i] = 0
    else:
      col_2[i] = '0.0'
      col_3[i] = 0
      
    sum += int(float(col_2[i]))*col_3[i]
    credit += int(float(col_2[i]))

print(sum/credit)
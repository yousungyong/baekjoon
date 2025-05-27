a,b,c = 0,0,0
while True:
  nums = list(map(int,input().split()))
  nums.sort
  
  a = nums[0]
  b = nums[1]
  c = nums[2]

  if a == 0 and b == 0 and c == 0:
    break
  else:
    if a + b <= c:
      print("Invalid")
    elif a == b == c:
      print("Equilateral")
    elif a == b or b == c or c == a:
      print("Isosceles")
    else:
      print("Scalene")
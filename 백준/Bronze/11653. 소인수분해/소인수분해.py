import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())

if N == 1:
    pass
elif N < 4:
    print(N)
else :
  for i in range(2, int(math.sqrt(N)) + 1):
      while N % i == 0:
        print(i)
        N /= i
      else :
        if is_prime(N):
            print(int(N))
            break
        
    

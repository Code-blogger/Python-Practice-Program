def isPrime(n):
  if(n==1 or n==0):
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  return True
 
N = int(input("Enter The number :"))
for i in range(1,N+1):
  if(isPrime(i)):
    print(i,end=" ")

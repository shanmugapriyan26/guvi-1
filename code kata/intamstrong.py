s,t=map(int,input().split())
for x in range(s+1,t):
  sum =0
  temp =x
  while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
  if x==sum:
    print(x,end=' ')

s=int(input())
t=int(s/2)
for i in range(2,t+1):
  if (s%i==0):
    print("no")
    break
else:
    print("yes")

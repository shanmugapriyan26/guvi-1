s,t=map(int,input().split())
for m in range(s+1,t):
  if m>1:
    for l in range(2,m):
      if(m%l==0):
        break
    else:
      print(m,end=' ')

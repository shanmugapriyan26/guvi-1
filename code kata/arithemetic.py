s,p,u=map(int,input().split())
if(s>1 and s<=100000):
  i=int((s/2)*(2*p + (s-1)*u))
  print(i)

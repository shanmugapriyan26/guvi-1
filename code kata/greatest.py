x=int(input())
y=int(input())
z=int(input())
if(x>=y and x>=z):
  l=x
elif(y>=x and y>=z):
  l=y
else:
  l=z
print(l)

x=input()
x=x.lower()
v=("aeiou")
c=("bcdfghjklmnpqrstvwxyz")
if(x in v):
  print("Vowel")
elif(x in c):
  print("Consonant")
else:
  print("invalid")

a=int(input())
b=0
while a>0:
  d=a%10
  a=a//10
  b=b*10
  b=b+d
print(b)
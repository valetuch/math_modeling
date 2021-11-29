a=int(input('Первое число:'))
b=int(input('Второе число:'))
if b!=0:
  if a%b==0 :
    print ('делится',a/b)
  elif a%b!=0:
    x=a%b
    print ('не делится', x,a/b)
else:
    print ('на ноль делить нельзя')
a=float(input())
b=float(input())
c=float(input())
x1=a+b
x2=c+b
x3=a+c
if c==x1 or a==x2 or b==x3:
  print ("Треугольника не существует")
elif a==b and b==c: 
  print ("Равносторонний")
elif a==b or c==a or b==c and b!=a or a!=c or c!=b:
  print ("Равнобедренный")
else:
  print("разностронний")
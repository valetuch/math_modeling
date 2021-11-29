import math
print ("Выберите фигуру:")
o=int(input())
h=int(input()) 
a=int(input()) 
if o==1:
    def treyg (h,a):
         S=h*a/2
         return S
  elif o==2:
     def okr (a):
         S=2*a*math.pi
         return S
 elif o==3:
     def kv (h):
         S=h**2
         return S
print (treyg(h,a))
print (okr(h))
print (kv(h))

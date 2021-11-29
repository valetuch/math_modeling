m=int(input())
h=int(input())
v=int(input())
def otvet (m,v,h):
    g=10
    Ep=m*g*h
    Ek=(m*v**2)/2
    E=Ep+Ek
    return E
print (otvet(m,v,h))
f=int(input())
l=int(input())
typ=int(input("Тип линзы "))
if l>2*f and typ!=1:
  print ("изображение действительное, перевернутое, уменьшенное")
elif f < l < 2*f and typ!=1:
  print ("изображение действительное, перевернутое, увеличенное")
elif l<f and typ!=1:
  print ("изображение мнимое, прямое, увеличенное")
elif typ!=0:
  print ("изображение мнимое, прямое, уменьшенное")
else:
  print ("Изображения нет")
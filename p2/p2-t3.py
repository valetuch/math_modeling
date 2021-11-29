a=int(input())
if (a%4) and (a%100!=0) or (a%400!=0):
 print ('Високосный')
else:
 print ('обычный')
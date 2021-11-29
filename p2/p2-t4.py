fib1 = 1
fib2 = 1
 
n = int(input("Номер элемента ряда Фибоначчи: "))
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print("Значение этого элемента:", fib2)
    i = i + 1
 
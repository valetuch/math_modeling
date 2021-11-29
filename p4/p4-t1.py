from random import random
N = 10
def average(a):
    s = 0
    for i in range(N):
        s += a[i]
    return s/N
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
b = average(arr)
print(arr)
print(b)
import numpy as np
import matplotlib.pyplot as plt
import math

n = input('Enter the number of elements: ')
np.random.seed()
x = 2 + np.random.normal(2,1.5,int(n))
y = 2 + np.random.normal(2,1.5,int(n))
k = int(1.44*math.log(int(n))+1)
fig, ex = plt.subplots()
ex.hist(x, bins = k, linewidth = 0.5, edgecolor = "white")
plt.show()

sorted((x))
print(np.median(x))
i = len(x) - 1
e = 0
list = []
print(x)
for p in x:
    if x[e] > np.median(x):
        list.append("+")
    elif x[e] < np.median(x):
        list.append("-")
    else:
        list.append(" ")
    if e == i:
        break
    e = e + 1
print(list)

fig, ex = plt.subplots()
ex.scatter(x, y, int(n), c = 'deeppink')
plt.show()

q = math.sqrt(int(n) - 1)
amt = input('Enter the number of batches: ')
lenh = input('Enter the length for the longest series: ')
if int(amt) > 0.5*((int(n)+1-1.96*q)):
    if int(lenh) < math.log(n+1):
        print("Data are divided in the field of random selection (success)")
else:
    print("Data not divided by randomization area (failure)")
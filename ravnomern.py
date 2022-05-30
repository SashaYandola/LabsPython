import numpy as np
import matplotlib.pyplot as plt
import math

n = input('Enter amount of elements: ')
np.random.seed()
mas_ravn = np.random.random(int(n))
y = np.random.random(int(n))
a = input('Enter left border: ')
b = input('Enter right border: ')
mas_ravn_a_b = int(a) + (int(b) - int(a)) * mas_ravn
print(mas_ravn_a_b)
k = int(1.44 * math.log(int(n)) + 1)
fig, ex = plt.subplots()
ex.hist(mas_ravn_a_b, bins = k, linewidth = 0.5, edgecolor = "white")
plt.show()

sorted((mas_ravn))
print(np.median(mas_ravn))
i = len(mas_ravn) - 1
e = 0
list = []
print(mas_ravn)
for x in mas_ravn:
    if mas_ravn[e] > np.median(mas_ravn):
        list.append("+")
    elif mas_ravn[e] < np.median(mas_ravn):
        list.append("-")
    else:
        list.append(" ")
    if e == i:
        break
    e = e + 1
print(list)
bb = int(n)

fig, ex = plt.subplots()
ex.scatter(mas_ravn, y, int(n), c = 'deeppink')
plt.show()
amt = input('Enter amount of series: ')
lenh = input('Enter lenght for longest seria: ')
if(int(amt) > 0.5*(bb+1-1.96*math.sqrt(int(bb)-1))) & int(lenh) < math.log(bb+1):
    print("Data are separated in area of randomise (success)")
else:
    print("Data are not separated in area of randomise (failure)")
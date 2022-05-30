from statistics import median
import numpy as np
import matplotlib.pyplot as plt
import math

n = input('Enter amount of elements: ')
np.random.seed()
lambd = 0.5
mas_exp = np.random.random(int(n))
y = np.random.random(int(n))
mas_exp_lm = -(np.log(mas_exp))/lambd
k = int(1.44 * math.log(int(n)) + 1)
fig, ex = plt.subplots()
ex.hist(mas_exp_lm, bins = k, linewidth = 0.5, edgecolor = "white")
plt.title('Exponential:$\lambda$=%.2f' % lambd)
plt.show()

x = np.arange(0,15,0.1)
y = lambd * np.exp(-lambd * x)
plt.plot(x,y)
plt.title('Exponential:$\lambda$=%.2f' % lambd)
plt.xlabel('x')
plt.ylabel('Probability density')
plt.show()

sorted((mas_exp))
print(np.median(mas_exp))
i = len(mas_exp) - 1
e = 0
list = []
print(mas_exp)
for x in mas_exp:
    if mas_exp[e] > np.median(mas_exp):
        list.append("+")
    elif mas_exp[e] < np.median(mas_exp):
        list.append("-")
    else:
        list.append(" ")
    if e == i:
        break
    e = e + 1
print(list)
bb = int(n)
fig, ex = plt.subplots()

plt.show()
amt = input('Enter amount of series: ')
lenh = input('Enter lenght for longest seria: ')
if(int(amt) > 0.5 * (bb + 1 - 1.96 * math.sqrt(int(bb) - 1))) & int(lenh) < math.log(bb + 1):
    print("Data are separated in area of randomise (success)")
else:
    print("Data are not separated in area of randomise (failure)")
#data collected through client-server application 

import matplotlib
import matplotlib.pyplot as plt

no_of_workers=[10**(i) for i in range(3)]

#1 thread, 1 instance
a=[157.50400000000002, 1020.7839999999999, 10142.723]

#10 thread, 1 instance
b=[107.654, 108.06, 1115.817]

#20 thread, 1 instance
c=[108.459, 137.488, 598.222]

#50 thread, 1 instance
d=[127.78500000000001, 130.663, 587.3009999999999]

#100 thread, 1 instance
e = [117.763, 127.661, 617.8900000000001]

#1 thread, 3 instance
f=[105.47, 413.497, 3472.032]

#10 thread, 3 instance
g=[106.651, 115.842, 422.477]

# 20 threads, 3 instances
h=[107.795, 113.66, 305.535] 

#50 thread, 3 instance
i=[111.296, 134.768, 284.04699999999997]

#100 thread, 3 instance
j=[362.058, 123.019, 283.555]

plt.xlabel('number of parallel clients')
plt.ylabel('time taken in milliseconds')
plt.grid(True)

plt.title('number of parallel clients vs time taken for server parallel threads')

plt.plot(no_of_workers, a,'b',linestyle='--',marker='o')
plt.plot(no_of_workers, b,'g',linestyle='--',marker='o')
plt.plot(no_of_workers, c,'r',linestyle='--',marker='o')
plt.plot(no_of_workers, d,'c',linestyle='--',marker='o')
plt.plot(no_of_workers, e,'m',linestyle='--',marker='o')
plt.plot(no_of_workers, f,'b',linestyle='-',marker='o')
plt.plot(no_of_workers, g,'g',linestyle='-',marker='o')
plt.plot(no_of_workers, h,'r',linestyle='-',marker='o')
plt.plot(no_of_workers, i,'c',linestyle='-',marker='o')
plt.plot(no_of_workers, j,'m',linestyle='-',marker='o')
plt.show()



# pip install matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 4, 8, 16]
plt.plot(x,y,color='r')
plt.ylabel('mytest')
plt.savefig("ex2.png")

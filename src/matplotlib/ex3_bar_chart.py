# pip install matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
h = [1, 2, 4, 8, 16]
plt.bar(x,h)
#plt.ylabel('mybar')
plt.savefig("ex3_bar_chart.png")

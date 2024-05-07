# pip install matplotlib
import matplotlib.pyplot as plt

x = [20, 50, 30]
plt.pie(x, radius=1.5, labels=x)
#plt.ylabel('mybar')
plt.savefig("ex4_pie_chart.py")

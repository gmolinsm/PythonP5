from matplotlib import pylab as plt

series1 = []
series2 = []
series3 = []
series4 = []

for i in range(0, 30):
    series1.append(i)
    series2 += [i*i]
    series3 += [i**3]
    series4 += [i+1.5]

plt.figure("first")
plt.title("Linear")
plt.ylim(0, 100)
plt.xlabel("Series")
plt.ylabel("Linear progression")
plt.plot(list(range(0, 30)), series1)

plt.figure("second")
plt.title("Cuadratic")
plt.ylim(0, 500)
plt.xlabel("Series")
plt.ylabel("Progression")
plt.plot(list(range(0, 30)), series2)

plt.figure("third")
plt.title("Cubic")
plt.ylim(0, 3000)
plt.xlabel("Series")
plt.ylabel("Progression")
plt.plot(list(range(0, 30)), series3)

plt.figure("fourth")
plt.title("Constant")
plt.ylim(0, 30)
plt.xlabel("Series")
plt.ylabel("Linear progression")
plt.plot(list(range(0, 30)), series4)

plt.show()

import pandas
from matplotlib import pylab as plt
from numpy import *

df1 = pandas.read_csv("NVDA.csv")
print(df1)
df1['Date'] = pandas.to_datetime(df1.Date)


df2 = pandas.read_csv("AMD.csv")
print(df2)
df2['Date'] = pandas.to_datetime(df2.Date)

mean1 = df1["Close"].mean()
mean2 = df2["Close"].mean()

plt1 = df1.plot(x="Date", y="Close", style='g-', linewidth=0.6, label="Stock price, mean="+str(mean1), title="NVIDIA", figsize=(18, 9))
plt2 = df2.plot(x="Date", y="Close", style='r-', linewidth=0.6, label="Stock price, mean="+str(mean2), title="AMD", figsize=(18, 9))
plt.show()
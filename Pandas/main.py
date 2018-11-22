import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list("ABCD"))
df.describe()
print(df)

df2 = pd.DataFrame({"A": 1., "B": pd.Timestamp("20130102"),
                    "C": pd.Series(1, index=list(range(4))), "D": np.array([3] * 4, dtype="int32"),
                    "E": pd.Categorical(["test", "train", "test", "train"]),
                    "F": "foo"})
print(df2)


s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
print(s1)

df.at[dates[0], "A"] = 0
df.iat[0, 1] = 0

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import seaborn as sns 

sns.set()

year = np.array([2016, 2017, 2018, 2019, 2020])
friend1 = np.array([20, 21, 26, 28, 9])
friend2 = np.array([19, 23, 18, 22, 6])
me = np.array([21, 23, 30, 24, 7])

data = {
    "year": year,
    "friend1": friend1, 
    "friend2": friend2, 
    "me": me
}

df = pd.DataFrame(data)

plt.plot(df["year"], df["friend1"], color="yellow")
plt.plot(df["year"], df["friend2"], color="red")
plt.plot(df["year"], df["me"], color="blue")

plt.show()
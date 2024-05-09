# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv("insurance.csv")

print(df.tail(3))

subset = df[['age', 'bmi']].iloc[:2]
sub = df.iloc[(10)]


print(subset)
print(sub)
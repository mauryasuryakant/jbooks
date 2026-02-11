import pandas as pd

data = pd.read_csv("Data/data.csv")

print("Original DataFrame")
print(data.isnull().sum())

print("\n")

drop_null = data.dropna()

dropped = pd.DataFrame(drop_null)

dropped.to_csv("Data/data.csv", index = False)

print(data)

# data.dropna()
# data.isnull().sum()
import pandas as pd

data = {
"Name": ["Ayush", "Joy", "Prem", "Abhay", "Piyush"],
"Age": [18,13,17,17,21],
"City": ["Surat","Surat","Surat","Surat", "Surat"]
}

df = pd.DataFrame(data)

df.to_csv("Data/data.csv", index = False)
df.to_json("Data/data.json", index = False)
df.to_excel("Data/data.xlsx", index = False)
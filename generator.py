import pandas as pd

def generate():
    data = {
    "Name": ["Ayush", "Joy", "Prem", "Abhay", "Piyush"],
    "Age": [21,34,55,45,76],
    "City": ["Surat","Surat","Surat","Surat","Surat"]
    }

    df = pd.DataFrame(data)

    df.to_csv("Data/data.csv")
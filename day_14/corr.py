import pandas as pd

df=pd.read_csv("data22.csv")
df["Salary"]=df["Salary"].fillna(df["Salary"]).mean()

df=pd.get_dummies(df,columns=["City"])

print(df)

print("\n Correlation Matrix:\n")
print(df.corr())

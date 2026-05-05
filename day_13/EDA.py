import pandas as pd 
df=pd.read_csv("shigoto.csv")
'''print("Full Data:\n",df)'''

#getting the basic info of the following data

'''print("\nInfo:\n")
print(df.info())'''

#checking for the stastical summary of the data

print("\nStastical Data:\n")
print(df.describe())


#checking for the unique values

print("\nUnique Values:\n")
print(df["City"].unique())

#couting the data

print("\nCounting of the data:\n")
print(df["City"].value_counts())

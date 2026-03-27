import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

df= pd.read_csv("C:/Users/sandhya rajak/Downloads/Banking.csv")
print(df)
print(df.info())

# generate descriptive statistics for the dataframe
print(df.describe())# describe give you all the aggrigate value 

bins = [0, 100000, 300000, float("inf")]  # the inf is providing as infinite
labels=["low","med","high"]
df["Income band"] = pd.cut(df["Estimated Income"], bins=bins, labels=labels)
print(df[["Estimated Income", "Income band"]].head(10))
print(df["Income band"].value_counts())
df["Income band"].value_counts().plot(kind="bar")
plt.show()


# Examine the distribution of unique categories in categorical columns
categorical_col = df[["BRId","GenderId", "IAId","Amount of Credit Cards","Nationality","Occupation","Fee Structure","Loyalty Classification","Properties Owned","Risk Weighting","Income band"]].columns

for col in categorical_col:
    try:
       print(f"Value counts for '{col}':")
       print(df[col].value_counts())
       df[col].value_counts().plot(kind="bar")
       plt.show()
    except KeyError:
        print(f"Column '{col}' not found, skipping.")
        

# same analysis with univariate analysis

for i, predictor in enumerate(df[["BRId","GenderId", "IAId","Amount of Credit Cards","Nationality","Occupation","Fee Structure","Loyalty Classification","Properties Owned","Risk Weighting","Income band"]]):        
   plt.figure(i)
   sns.countplot(data=df,x=predictor)# bivariate (hue="any category" like genderId)
   plt.show()

# histplot of value counts for different occupation
for col in categorical_col:
    if col == "Occupation":
        continue
    sns.histplot(df[col])
    plt.xlabel(col)
    plt.ylabel("value count")
    plt.show()

# numerical analysis

numerical_col =["Estimated Income","Superannuation Savings","Credit Card Balance","Bank Loans","Bank Deposits","Checking Accounts","Saving Accounts","Foreign Currency Account","Business Lending"]

# univariate analysis and visualization 
plt.figure(figsize=(10,))
for i , col in enumerate(numerical_col):
    
    plt.subplot(4,3,i+1)
    sns.histplot(df[col],kde=True)
    plt.title("histogram plot")

plt.tight_layout()    
plt.show()


# Heatmaps 

numerical_col =["Estimated Income","Superannuation Savings","Credit Card Balance","Bank Loans","Bank Deposits","Checking Accounts","Saving Accounts","Foreign Currency Account","Business Lending"]

correlation_matix= df[numerical_col].corr()
plt.figure(figsize=(6,4))
sns.heatmap(correlation_matix,annot=True,cmap="crest",fmt=".2f")
plt.title("Correlation Matrix")
plt.show() 

# insights of EDA :
""" 1. The strongest positive correlation occure among "Bank Deposits" with "Checking Account" , "Saving Accounts" 
and Foreign Currency Account" indicating that customer who maintain high balances in one 
account type often hold substantial amount/funds across other account as well """



import pandas as pd

Border = "-"*50
##########################################################
# Step 1 : Load the dataset
##########################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "iris.csv" 

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")

print("Initial Entries from Dataset are : ")
print(df.head())

##########################################################
# Step 2 : Data Analysis (EDA)
##########################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing Values per column : ")
print(df.isnull().sum)

print("Class Distribution (species count) : ")
print(df["species"].value_counts())

print("Statistical report of dataset : ")
print(df.describe())

##########################################################
# Step 3 : Decide Independent and Dependent variables
##########################################################

print(Border)
print(" Step 3 : Decide Independent and Dependent variables")
print(Border)

# X : Independent variable / Features
# Y : Dependent Variable   / Labels

feature_cols = [
                    "sepal length (cm)",
                    "sepal width (cm)",
                    "petal length (cm)",
                    "petal width (cm)"
                ]

X = df[feature_cols]
Y = df["species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)
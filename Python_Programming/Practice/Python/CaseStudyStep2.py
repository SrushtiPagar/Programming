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
# Step 1 : Data Analysis (EDA)
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
# Pandas -  series (1D array)
#           DataFrane (2D array)
#           Panel     (3D array)  Removed from specific version

import pandas as pd

Border = "-"*50
##########################################################
# Step 1 : Load the dataset
##########################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "iris.csv"       #relative path

# df = data frame
df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")

print("Initial Entries from Dataset are : ")
print(df.head())
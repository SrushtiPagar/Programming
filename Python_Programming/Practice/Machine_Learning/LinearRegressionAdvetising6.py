import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousRegression(DataPath):
    Border = "-"*40
    # Step 1 : Load THE Data

    print(Border)
    print("Step 1 : Load THE Data")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head)

    # Step 2 : Rename Unwanted columns
    
    print(Border)
    print("Step 2 : Rename Unwanted columns")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    # Step 3 : Check missing values
        
    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Check missing values")
    print(Border)
    print(df.isnull().sum())
    print(Border)

    # Step 4 : Statistical Summary
            
    print(Border)
    print("Step 4 : Statistical Summary")
    print(Border)

    print(df.describe())

    # Step 5 : Correlation
            
    print(Border)
    print("Step 5 : Correlation")
    print(Border)

    print(df.corr())

    # Step 5 : Seperate independent and dependent variable
                
    print(Border)
    print("Step 5 : Seperate independent and dependent variable")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"] 

    print("Independent Variable : ")
    print(X.head())

    print("Dependent Variable : ")
    print(Y.head())

    # Step 7 : Split dataset
                
    print(Border)
    print("Step 7 : Split dataset")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data : ",X_train.shape)
    print("Testing Data : ",Y_train.shape)

def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()
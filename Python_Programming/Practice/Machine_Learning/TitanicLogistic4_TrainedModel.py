import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# Step 1 : Load Data

#---------------------------------------------------------------
#   Function Name : Load Data (Automic function)
#   Description :   Load the Data from csv
#   Input :         Name of csv file
#   Output :        Data Frame
#   Author :        Srushti Nitin Pagar
#   Data :          16-08-2026
#---------------------------------------------------------------
def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset Loaded Successfully")
    print(df.head())

    return df

# Step 2 : Data preprocessing

#---------------------------------------------------------------
#   Function Name : PreprocessData
#   Description :   It performs Data Analysis
#   Input :         Data Frame
#   Output :        Updated DataFrame
#   Author :        Srushti Nitin Pagar
#   Data :          16-08-2026
#---------------------------------------------------------------

def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors= "ignore"
    )

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert categorical to numeric data

    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )
    print(df.head())
    print("Data Preprocessing Completed")
    
    return df

# Step 3 : Spliting the Data

#---------------------------------------------------------------
#   Function Name : Split Data
#   Description :   It performs Splitting Activity
#   Input :         Data Frame
#   Output :        4 subsets for training and testing
#   Author :        Srushti Nitin Pagar
#   Data :          16-08-2026
#---------------------------------------------------------------

def SplitData(df):
    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Dataset splitting completed successfully")

    return X_train,X_test,Y_train,Y_test

# Step 4 : Trainig the model

#---------------------------------------------------------------
#   Function Name : TrainModel
#   Description :   It performs model training
#   Input :         Training features and labels
#   Output :        Trained model
#   Author :        Srushti Nitin Pagar
#   Data :          16-08-2026
#---------------------------------------------------------------

def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train,X_train)

    print("Model Trained successfully")

    return model

# Step 4 : Evaluate the model

#---------------------------------------------------------------
#   Function Name : EvaluateModel
#   Description :   It performs model testing
#   Input :         model, Testing data (features & labels)
#   Output :        None
#   Author :        Srushti Nitin Pagar
#   Data :          16-08-2026
#---------------------------------------------------------------

def EvaluateModel(model,X_test,Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",accuracy)

    print(confusion_matrix(Y_test,Y_pred))

#---------------------------------------------------------------
#   Function Name : main
#   Description :   Entry point function
#   Input :         None
#   Output :        None
#   Author :        Srushti Nitin Pagar
#   Data :          16-08-2026
#---------------------------------------------------------------
def main():
    # S1 
    df = LoadData("MarvellousTitanicDataset.csv")

    #S2
    df = PreprocessData(df)

    #S3
    X_train,X_test,Y_train,Y_test = SplitData(df)

    #S4
    model = TrainModel(X_train,Y_train) 

    #S5

    EvaluateModel(model,X_test,Y_test)

if __name__ == "__main__":
    main()
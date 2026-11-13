import pandas as pd
import joblib

def LoadModel(Filename):
    model = joblib.load(Filename)

    print("Model Loaded successfully")

    print(model.feature_names_in)

    return model

def PredictPassesnger(model):
    print("Enter the infromation")

    Pclass = int(input("Enter Pclass (1/2/3) : "))
    Sex = int(input("Enter Sex (0-M/1=F) : "))
    Age = int(input("Enter age : "))
    sibsp = int(input("Enter sibsp : "))
    Parch = int(input("Enter Parch : "))
    Fare = int(input("Enter Fare : "))
    Embarked = float(input("Enter embarked (0/1/2) : "))

    passenger = pd.DataFrame([{
        "Pclass" : Pclass,
        "Sex"    : Sex,
        "Age"   : Age,
        "sibsp" : sibsp,
        "Fare" : Fare,
        "Embarked_1.0" : Embarked
    }])

    passenger = passenger[model.feature_names_in_]

    result = model.predict(passenger)

    print(result)

def main():
    model = LoadModel("MarvellousTitanic.pkl")

    PredictPassesnger(model)

if __name__ == "__main__":
    main()
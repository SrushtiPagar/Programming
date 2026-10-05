import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

#----------------------------------------------------
#   S1 : Load the data
#----------------------------------------------------

df = pd.read_csv("california_housing.csv")
print("sHAPE OF dATASET : ",df.shape)

print("First few records : ",df.head())

#----------------------------------------------------
#   S2 : Seperate features and labels
#----------------------------------------------------

X = df.drop("target",axis=1) 
Y = df["target"]

print("Shape of X : ",X.shape)
print("Shape of Y : ",Y.shape)

#----------------------------------------------------
#   S3 : Split dataset for training and testing
#----------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#----------------------------------------------------
#   S4 : create the model
#----------------------------------------------------

model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

#----------------------------------------------------
#   S5 : Train the model
#----------------------------------------------------

model = model.fit(X_train,Y_train)

#----------------------------------------------------
#   S6 : Test the model
#----------------------------------------------------

Y_pred = model.predict(X_test)

#----------------------------------------------------
#   S7 : Evaluate the model
#----------------------------------------------------

print("MSE : ",mean_squared_error(Y_test,Y_pred))
print("R2 : ",r2_score(Y_test,Y_pred))
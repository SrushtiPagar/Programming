import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#-----------------------------------------
# s1 : Load the dataset
#-----------------------------------------

df = pd.read_csv("breast_cancer.csv")

print("Shape of the dataset is : ",df.shape)

print("First few records : ")
print(df.head())

#-----------------------------------------
# s2 : separate the features and labels
#-----------------------------------------

X = df.drop("target",axis=1)

Y = df["target"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

#-----------------------------------------
# s3 : Split the dataset into training and testing
#-----------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,
                                                 Y,
                                                 test_size=0.2,
                                                 random_state=42
                                                )


#-----------------------------------------
# s4 : Feature Scaling
#-----------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

#------------------------------------------
# s5 : Create the model
#------------------------------------------

model = LogisticRegression(max_iter=1000)

#------------------------------------------
# s6 : Train the model
#------------------------------------------

model = model.fit(X_train,Y_train)

#------------------------------------------
# s7 : Test the model
#------------------------------------------

Y_pred = model.predict(X_test)

#------------------------------------------
# s7 : Evaluate the model
#------------------------------------------

print("Accuracy : ",accuracy_score(Y_test,Y_pred))

print("Confusion matrix : ")
print(confusion_matrix(Y_test,Y_pred))
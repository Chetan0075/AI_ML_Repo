import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import os

print("\n\n--||------- Welcome To Semester Prediction System -------||--")


# Load Dataset
df = pd.read_csv("semester.csv")

# Define X and Y
x = df[["Sem1","Sem2","Sem3","Sem4","Sem5"]]
y = df["Sem6"]

# Train Test Split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# -------- Linear Regression Model --------
lr = LinearRegression()
lr.fit(x_train,y_train)

# -------- KNN Model --------
knn = KNeighborsRegressor(n_neighbors=1)
knn.fit(x_train,y_train)

# Prediction storage
prediction_file = "prediction_history.csv"


def prediction():

    print("\nEnter Marks of Previous Semesters\n")

    s1 = int(input("Sem1: "))
    s2 = int(input("Sem2: "))
    s3 = int(input("Sem3: "))
    s4 = int(input("Sem4: "))
    s5 = int(input("Sem5: "))

    data = pd.DataFrame([[s1,s2,s3,s4,s5]],
    columns=["Sem1","Sem2","Sem3","Sem4","Sem5"])


    # Predictions
    lr_pred = lr.predict(data)[0]
    knn_pred = knn.predict(data)[0]

    print("\n---------------- Prediction Result ----------------")

    print("Linear Regression Predicted Sem6 :", round(lr_pred,2))
    print("KNN Predicted Sem6 :", round(knn_pred,2))

    # Save prediction
    new_data = pd.DataFrame({
        "Sem1":[s1],
        "Sem2":[s2],
        "Sem3":[s3],
        "Sem4":[s4],
        "Sem5":[s5],
        "LR_Predicted_Sem6":[round(lr_pred,2)],
        "KNN_Predicted_Sem6":[round(knn_pred,2)]
    })

    if os.path.exists(prediction_file):
        new_data.to_csv(prediction_file,mode='a',header=False,index=False)
    else:
        new_data.to_csv(prediction_file,index=False)

    print("\nPrediction Saved Successfully")



def view_prediction():

    if os.path.exists(prediction_file):

        df = pd.read_csv(prediction_file)

        print("\n---------------- Prediction History ----------------\n")

        print(df)

    else:

        print("\nNo prediction history found.")



def exit_system():
    print("\n--||------- Thank You For Using Prediction System -------||--")
    exit()



def menu():

    print("\n1. Do Prediction")
    print("2. View Prediction")
    print("3. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        prediction()

    elif choice == "2":
        view_prediction()

    elif choice == "3":
        exit_system()

    else:
        print("Invalid Choice")

menu()

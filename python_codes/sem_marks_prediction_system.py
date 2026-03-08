import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score, accuracy_score
import warnings
warnings.filterwarnings("ignore")

print("\n\n\n--|*|------- Welcome To Semester Prediction System -------|*|--")

sem6_lr = None
sem6_knn = None


def prediction():

    global sem6_lr, sem6_knn

    sem1 = int(input("\n Enter Sem1 Marks: "))
    sem2 = int(input(" Enter Sem2 Marks: "))
    sem3 = int(input(" Enter Sem3 Marks: "))
    sem4 = int(input(" Enter Sem4 Marks: "))
    sem5 = int(input(" Enter Sem5 Marks: "))

    # Create training dataset from transitions
    X = np.array([[sem1],[sem2],[sem3],[sem4]])
    y = np.array([sem2,sem3,sem4,sem5])

    x_train = X
    y_train = y
    x_test = X
    y_test = y

    # -------- Linear Regression --------

    lr = LinearRegression()
    lr.fit(x_train,y_train)

    sem6_lr = lr.predict([[sem5]])

    y_pred_lr = lr.predict(x_test)

    lr_score = r2_score(y_test,y_pred_lr)

    # -------- KNN --------

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train,y_train)

    sem6_knn = knn.predict([[sem5]])

    y_pred_knn = knn.predict(x_test)

    knn_score = accuracy_score(y_test,y_pred_knn)

    print("\n || Prediction Completed ||")

    print("\n--------------------- Accuracy Results -------------------")

    print(" Linear Regression Accuracy :", round(lr_score*100,2),"%")

    print(" KNN Accuracy :", round(knn_score*100,2),"%")


def viewprediction():

    if sem6_lr is None:
        print("\n\n No prediction available. Run prediction first.")
    else:

        print("\n--------------------- Prediction Results -------------------")

        print("\n *||* Linear Regression Predicted Sem6 :", round(sem6_lr[0],2),"*||*")

        print("\n *||* KNN Predicted Sem6 :", sem6_knn[0],"*||*\n")


def exit_system():
    print("\n\n --||------- Thank You For Visiting Our Prediction System -------||--")
    exit()


def menu():

    while True:

        print("\n1. Prediction")
        print("2. View Prediction")
        print("3. Exit")

        op = input("\n Enter Your Choice : ")

        if op == "1":
            prediction()

        elif op == "2":
            viewprediction()

        elif op == "3":
            exit_system()

        else:
            print("Invalid Choice")


menu()

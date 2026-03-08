import numpy as np
from sklearn.linear_model import LinearRegression

print("\n\n\n--|*|------- Welcome To Semester Prediction System -------|*|--")

sem6 = None


def prediction():

    global sem6

    sem1 = int(input("Enter Sem1 Marks: "))
    sem2 = int(input("Enter Sem2 Marks: "))
    sem3 = int(input("Enter Sem3 Marks: "))
    sem4 = int(input("Enter Sem4 Marks: "))
    sem5 = int(input("Enter Sem5 Marks: "))

    X = np.array([[sem1],[sem2],[sem3],[sem4]])
    y = np.array([sem2,sem3,sem4,sem5])

    model = LinearRegression()
    model.fit(X,y)

    sem6 = model.predict([[sem5]])

    print("\n || Prediction Completed ||")


def viewprediction():

    if sem6 is None:
        print("\n\n\n No prediction available. Run prediction first.")
    else:
        print("\nPredicted Sem6 Marks:", round(sem6[0],2))


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

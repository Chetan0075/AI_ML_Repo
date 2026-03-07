import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings("ignore")
from sklearn.metrics import accuracy_score


salary = int(input("Enter Your Salary : "))
df = pd.read_csv("AI_ML_Workshop/User_Data.csv")
# print(df)
# df.info()

x = df.iloc[:,[3]] #salary
y = df.iloc[:,[4]] #house
# print(x,y)
# left side of (comma) means row number and right of (comma) means column number 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.2)




print("---------------------Using Logistical Regression-------------------")
lr = LogisticRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict([[salary]])

if y_pred == 0 :
    print("You Cannot Purchase House Your Salary is Low")

else :
    print("You Can purchase House You Have Enough Salary")

print("---------------------Accuracy of Logistical Regression -------------------")
y_pred2 = lr.predict(x_test)
score = accuracy_score(y_test,y_pred2)
print("Your Accuracy of Logistical Regression :",score)





print("---------------------Using KNN------------------------------------")
knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
knn_pred = knn.predict([[salary]])

if knn_pred == 0 :
    print("You Cannot Purchase House Your Salary is Low")

else :
    print("You Can purchase House You Have Enough Salary")

print("---------------------Accuracy of KNN-------------------")
knn_pred = lr.predict(x_test)
score2 = accuracy_score(y_test,y_pred2)
print("Your Accuracy of KNN :",score2)    

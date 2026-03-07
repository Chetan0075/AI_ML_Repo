import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

salary = int(input("Enter Your Salary : "))

df = pd.read_csv("AI_ML_Workshop/User_Data.csv")
print(df)
# df.info()


x = df.iloc[:,[3]] #salary
y = df.iloc[:,[4]] #house
# print(x,y)
# left side of (comma) means row number and right of (comma) means column number 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.2)

lr = LogisticRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict([[salary]])

if y_pred == 0 :
    print("You Cannot Purchase House Your Salary is Low")

else :
    print("You Can purchase House You Have Enough Salary")

print("Your Predicted House is : ",y_pred)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("AI_ML_Workshop\Boys_data.csv")
df.info()


x = df.iloc[:,[3]] #age
y = df.iloc[:,[5]] #class
# left side of (comma) means row number and right of (comma) means column number 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.2)

lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict([[17]])
print(y_pred)


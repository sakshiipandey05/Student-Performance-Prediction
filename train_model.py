import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    'Study_Hours':[2,3,4,5,6,7,8,9,10,11],
    'Attendance':[60,65,70,75,80,85,90,92,95,98],
    'Previous_Score':[50,55,60,62,68,70,75,80,85,90],
    'Final_Score':[52,58,63,68,72,78,83,88,92,96]
}

df = pd.DataFrame(data)

X = df[['Study_Hours','Attendance','Previous_Score']]
y = df['Final_Score']

model = LinearRegression()
model.fit(X,y)

pickle.dump(model, open('student_model.pkl','wb'))

print("Model Saved Successfully")
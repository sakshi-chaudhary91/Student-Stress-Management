import pickle
import pandas as pd
# dataset loading
df = pd.read_csv(r"E:\Student Stress Management\archive.csv")
print(df.head())
print(df.info())

# data cleaning

# missing value check
print(df.isnull().sum())
#missing value fill
df = df.fillna(df.mean(numeric_only=True))

df = pd.get_dummies(df)

# making model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#spliting data
x = df.drop('stress_level', axis=1)
y = df['stress_level']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#model train
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

#save model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model saved successfully.")
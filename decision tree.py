import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


data = pd.read_csv("customer_data.csv")

X = data.drop('will_buy', axis=1)
y = data['will_buy']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

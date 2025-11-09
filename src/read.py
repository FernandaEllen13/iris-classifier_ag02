import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import json

df = pd.read_csv("iris.csv")

df["species"] = df["species"].replace({
    "Iris-setosa": 1,
    "Iris-versicolor": 2,
    "Iris-virginica": 3
})

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=True, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))

acc_teste = accuracy_score(y_test, y_pred)
print("Acurácia (Teste):", acc_teste)

joblib.dump(model, "modelo_iris.pkl")
print("Modelo salvo com sucesso! 🎉")

metrics = {"accuracy": acc_teste}
with open("metrics.json", "w") as f:
    json.dump(metrics, f)
print("Métricas salvas com sucesso! 📊")
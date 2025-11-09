import streamlit as st
import pandas as pd
import joblib
import json
import os
from PIL import Image

st.title("🌸 Classificador de Flores Iris 🌸")

model = joblib.load("modelo_iris.pkl")
with open("metrics.json", "r") as f:
    metrics = json.load(f)

acc_teste = metrics["accuracy"]

script_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(script_dir,"img")

CLASS_MAP = {
    1: {
        "name": "Iris-setosa ⚜️",
        "image": os.path.join(img_dir, "iris-setosa.png")
    },
    2: {
        "name": "Iris-versicolor ⚜️",
        "image": os.path.join(img_dir, "iris-versicolor.png")
    },
    3: {
        "name": "Iris-virginica ⚜️",
        "image": os.path.join(img_dir, "iris-virginica.png")
    }
}

st.metric(label="🌿 Acurácia do Modelo", value=f"{acc_teste*100:.2f}%")
st.write("Insira as medidas abaixo e descubra qual espécie de flor é!")

sepal_length = st.number_input("Comprimento da sépala (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Largura da sépala (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Comprimento da pétala (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Largura da pétala (cm)", min_value=0.0, step=0.1)

if st.button("Prever Espécie"):
    input_data = {
        'sepal_length_cm': [sepal_length],
        'sepal_width_cm': [sepal_width],
        'petal_length_cm': [petal_length],
        'petal_width_cm': [petal_width]
    }
    input_df = pd.DataFrame(input_data)
    prediction = model.predict(input_df)[0]
    result = CLASS_MAP[prediction]
    result_name = result["name"]
    image_path = result["image"]

    try:
        image = Image.open(image_path)
        
        st.success(f"Espécie prevista: **{result_name}**")
        st.image(image, caption=result_name, width='stretch')

    except FileNotFoundError:
        st.error(f"Erro: A imagem '{os.path.basename(image_path)}' não foi encontrada na pasta 'src/img/'.")
        st.info("Verifique se você criou a pasta e nomeou os arquivos de imagem corretamente.")
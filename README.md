🌸 Classificador de Flores de Íris (AG02) 🌸
Este projeto é um aplicativo web interativo criado como parte da disciplina AG02. O objetivo é utilizar técnicas de Machine Learning para classificar três espécies diferentes de flores de Íris (Iris setosa, Iris versicolor e Iris virginica) com base nas medidas de suas sépalas e pétalas.

O aplicativo exibe a acurácia do modelo treinado e permite que o usuário insira medidas personalizadas para receber uma classificação em tempo real, que é exibida juntamente com uma imagem da espécie prevista.

🚀 Tecnologias Utilizadas
Linguagem: Python 3

Machine Learning: scikit-learn (usando DecisionTreeClassifier)

Interface Web: streamlit

Manipulação de Dados: pandas

Serialização: joblib e json (para salvar modelo e métricas)

📁 Estrutura do Projeto
O projeto é dividido em dois scripts principais para separar as responsabilidades, ambos localizados na pasta src/:

read.py: Script de treinamento. É responsável por ler o iris.csv, treinar o modelo, avaliar sua acurácia e salvar os artefatos (modelo_iris.pkl e metrics.json).

main.py: Script da aplicação web. É responsável por carregar os artefatos salvos, construir a interface com o Streamlit e realizar as previsões em tempo real.

🛠️ Como Executar o Projeto
Siga os passos abaixo para rodar o aplicativo em sua máquina local.

1. Clonar o Repositório
Bash

git clone [https://github.com/FernandaEllen13/iris-classifier_ag02.git](https://github.com/FernandaEllen13/iris-classifier_ag02.git)
cd iris-classifier_ag02
2. Criar e Ativar o Ambiente Virtual
Bash

# Crie o ambiente
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate
(Para Linux/macOS, o comando seria: source venv/bin/activate)

3. Instalar as Dependências
Bash

pip install -r requirements.txt
4. Treinar o Modelo (Apenas uma vez)
Antes de iniciar o app, você precisa treinar o modelo. Este comando gera os arquivos modelo_iris.pkl e metrics.json.

Bash

# Navegue para a pasta do código-fonte
cd src

# Execute o script de treinamento
python read.py
(Observação: Você só precisa fazer isso uma vez, ou quando quiser retreinar o modelo).

5. Iniciar o Aplicativo Streamlit
Ainda dentro da pasta src, inicie o servidor do Streamlit.

Bash

streamlit run main.py
O aplicativo abrirá automaticamente no seu navegador. Caso contrário, acesse http://localhost:8501.

📊 Resultado Final
Ao acessar o aplicativo, você verá a acurácia do modelo (calculada sobre os dados de teste) e quatro campos para inserir as medidas da flor.

Após inserir os valores e clicar em "Prever Espécie", o aplicativo exibirá o nome e uma imagem da flor classificada. ⚜️
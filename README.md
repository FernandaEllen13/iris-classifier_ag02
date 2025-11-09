🌸 Classificador de Flores de Íris (AG02) 🌸
Este projeto é um aplicativo web interativo criado como parte da disciplina AG02. O objetivo é utilizar técnicas de Machine Learning para classificar três espécies diferentes de flores de Íris (Iris setosa, Iris versicolor e Iris virginica) com base nas medidas de suas sépalas e pétalas.

O aplicativo exibe a acurácia do modelo treinado e permite que o usuário insira medidas personalizadas para receber uma classificação em tempo real, que é exibida juntamente com uma imagem da espécie prevista.

🚀 Tecnologias e Conceitos Utilizados
Linguagem: Python

Machine Learning: Scikit-learn (DecisionTreeClassifier para o modelo)

Aplicativo Web: Streamlit (para a interface interativa)

Manipulação de Dados: Pandas (para leitura e processamento do .csv)

Serialização: Joblib e JSON (para salvar o modelo treinado e as métricas)

Boas Práticas:

Uso de ambiente virtual (venv) para isolamento de dependências.

Arquivo requirements.txt para gerenciamento de pacotes.

Arquivo .gitignore para manter o repositório limpo.

Separação de responsabilidades:

read.py: Script para treinamento, avaliação e salvamento do modelo.

main.py: Script para carregar o modelo e rodar a aplicação web.

🛠️ Como Executar o Projeto
Para rodar este projeto em sua máquina local, siga os passos abaixo.

1. Pré-requisitos
Ter o Python (versão 3.9 ou superior) instalado.

Ter o Git instalado (para clonar o repositório).

2. Instalação
Clone o repositório:

Bash

git clone https://github.com/FernandaEllen13/iris-classifier_ag02.git
cd iris-classifier_ag02
Crie e ative um ambiente virtual:

Bash

# Criar o venv
python -m venv venv

# Ativar no Windows (CMD/PowerShell)
.\venv\Scripts\activate

# Ativar no Linux/macOS
# source venv/bin/activate
Instale as dependências: Com o ambiente ativo, instale todas as bibliotecas necessárias:

Bash

pip install -r requirements.txt
3. Execução
O projeto é dividido em duas etapas: treinar o modelo e iniciar o aplicativo.

Treine o Modelo (Apenas uma vez): Este script irá ler o iris.csv, treinar o modelo de Árvore de Decisão e salvar os arquivos modelo_iris.pkl e metrics.json dentro da pasta src.

Bash

# Navegue até a pasta src
cd src

# Execute o script de treinamento
python read.py
Obs: Se você estiver no Windows, pode precisar usar py em vez de python.

Inicie o Aplicativo Web: Após o treinamento, inicie o servidor do Streamlit.

Bash

# (Ainda dentro da pasta 'src')
streamlit run main.py
O Streamlit abrirá automaticamente uma aba no seu navegador. Caso não abra, acesse o http://localhost:8501 informado no terminal.

📊 Resultado Final
Ao acessar o aplicativo, você verá a acurácia do modelo (calculada sobre os dados de teste) e quatro campos para inserir as medidas da flor.

Após inserir os valores e clicar em "Prever Espécie", o aplicativo exibirá o nome e uma imagem da flor classificada. ⚜️
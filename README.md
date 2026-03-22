## Previsão de Risco de Defasagem Escolar

Este projeto foi desenvolvido no contexto de um Datathon da FIAP POSTECH com o objetivo de analisar dados educacionais e construir um modelo preditivo capaz de identificar alunos com risco de defasagem escolar.

A solução utiliza técnicas de análise de dados e Machine Learning para apoiar a tomada de decisão e permitir intervenções antecipadas.

## Objetivo do Projeto

O principal objetivo é prever, com base em indicadores educacionais e comportamentais, quais alunos possuem maior probabilidade de apresentar defasagem no futuro.

Com isso, a instituição pode:

- identificar alunos em risco de forma antecipada
- direcionar ações pedagógicas
- melhorar o desempenho acadêmico geral

## Base de Dados

A base contém informações de alunos ao longo de diferentes anos, incluindo:

- Indicadores acadêmicos
- Níveis de engajamento
- Aspectos psicossociais e psicopedagógicos
- Índice geral de desempenho

## Dicionário de Dados

| Coluna        | Descrição |
|--------------|----------|
| Nome         | Identificador anonimizado do aluno |
| Ano          | Ano da avaliação |
| Data de Nasc | Ano de nascimento |
| Idade        | Idade do aluno |
| Gênero       | Sexo do aluno |
| Pedra        | Fase educacional |
| INDE         | Índice geral de desempenho |
| IAN          | Índice de adequação de nível (defasagem) |
| IDA          | Desempenho acadêmico |
| IEG          | Engajamento |
| IAA          | Autoavaliação |
| IPS          | Indicador psicossocial |
| IPP          | Indicador psicopedagógico |
| IPV          | Indicador de ponto de virada |

---
## Análise Exploratória de Dados (EDA)

Durante a análise dos dados, foram identificados alguns padrões importantes:

- Existe forte relação entre desempenho acadêmico (IDA) e o índice geral (INDE)
- O engajamento (IEG) influencia diretamente o desempenho dos alunos
- Indicadores psicossociais apresentam impacto indireto nos resultados
- Alunos em risco tendem a apresentar menor engajamento e desempenho

## Engenharia de Features

Para melhorar a capacidade preditiva do modelo, foram criadas novas variáveis:

- Variação ao longo do tempo (DELTA_IDA, DELTA_IEG, DELTA_INDE)
- Interação entre variáveis (ENG_X_DESEMP = IEG × IDA)

Essas variáveis permitem capturar a evolução do aluno e padrões mais complexos.

## Modelo de Machine Learning
Modelo utilizado: Random Forest

Tipo de problema: Classificação binária

Objetivo: prever risco de defasagem futura

O modelo foi construído considerando o comportamento dos alunos ao longo do tempo, tornando a previsão mais realista.

## Desempenho do Modelo
Acurácia: aproximadamente 73%

Modelo ajustado para evitar overfitting

## Aplicação com Streamlit

Foi desenvolvida uma aplicação interativa utilizando Streamlit para permitir o uso prático do modelo.

Funcionalidades:
- Inserção dos indicadores do aluno
- Previsão de risco de defasagem
- Exibição da probabilidade de risco

## Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/student-risk-prediction.git
2. Instalar as dependências
pip install -r requirements.txt
3. Executar a aplicação
streamlit run app.py

## Principais Insights
- O engajamento é um dos principais fatores de sucesso acadêmico
- A combinação de múltiplos indicadores melhora a previsão
- A identificação precoce de risco permite ações preventivas

## Conclusão
Este projeto demonstra como dados e Machine Learning podem ser utilizados para apoiar decisões educacionais, permitindo identificar alunos em risco e melhorar os resultados de forma estratégica.

👩‍💻 Autora

Isabella Orlando - 
Data Analytics & Machine Learning

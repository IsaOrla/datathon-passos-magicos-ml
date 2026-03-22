import streamlit as st
import pickle
import pandas as pd

# carregar modelo
with open('modelo_risco.pkl', 'rb') as f:
    model = pickle.load(f)

# layout página
st.set_page_config(page_title="Risco de Defasagem", layout="centered")
st.title("📊 Previsão de Risco de Defasagem")
st.write("Simule o risco de um aluno com base nos indicadores educacionais")

# inputs
st.subheader("Insira os dados do aluno:")

IDA = st.slider("IDA (Desempenho Acadêmico)", 0.0, 10.0, 5.0)
IEG = st.slider("IEG (Engajamento)", 0.0, 10.0, 5.0)
IAA = st.slider("IAA (Autoavaliação)", 0.0, 10.0, 5.0)
IPS = st.slider("IPS (Psicossocial)", 0.0, 10.0, 5.0)
IPP = st.slider("IPP (Psicopedagógico)", 0.0, 10.0, 5.0)
IPV = st.slider("IPV (Ponto de Virada)", 0.0, 10.0, 5.0)
INDE = st.slider("INDE (Índice Geral)", 0.0, 10.0, 5.0)

# features extras
DELTA_IDA = st.number_input("Variação IDA", value=0.0)
DELTA_IEG = st.number_input("Variação IEG", value=0.0)
DELTA_INDE = st.number_input("Variação INDE", value=0.0)

ENG_X_DESEMP = IDA * IEG

# botão
if st.button("🔍 Prever Risco"):
    dados = pd.DataFrame([{
        'IDA': IDA,
        'IEG': IEG,
        'IAA': IAA,
        'IPS': IPS,
        'IPP': IPP,
        'IPV': IPV,
        'INDE': INDE,
        'DELTA_IDA': DELTA_IDA,
        'DELTA_IEG': DELTA_IEG,
        'DELTA_INDE': DELTA_INDE,
        'ENG_X_DESEMP': ENG_X_DESEMP
    }])

    pred = model.predict(dados)[0]
    prob = model.predict_proba(dados)[0][1]

    st.subheader("Resultado")
    if pred == 1:
        st.error(f"⚠️ Alto risco de defasagem ({prob:.2%})")
    else:
        st.success(f"✅ Baixo risco ({prob:.2%})")

    st.progress(int(prob * 100))

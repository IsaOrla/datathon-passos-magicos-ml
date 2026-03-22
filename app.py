import streamlit as st
import pickle
import pandas as pd

# ==========================
# CARREGAR MODELO
# ==========================
with open('modelo_risco.pkl', 'rb') as f:
    model = pickle.load(f)

# ==========================
# CONFIGURAÇÃO DA PÁGINA
# ==========================
st.set_page_config(page_title="Risco de Defasagem", layout="centered")
st.title("📊 Previsão de Risco de Defasagem")
st.markdown("Simule o risco de um aluno com base nos indicadores educacionais")
st.markdown("---")

# ==========================
# INPUTS EM COLUNAS
# ==========================
st.subheader("📥 Insira os dados do aluno:")

col1, col2, col3 = st.columns(3)

with col1:
    IDA = st.slider("IDA (Desempenho Acadêmico)", 0.0, 10.0, 5.0,
                    help="Indicador do desempenho do aluno nas avaliações")
    IPS = st.slider("IPS (Psicossocial)", 0.0, 10.0, 5.0,
                    help="Indicador de bem-estar e suporte psicossocial")
    DELTA_IDA = st.number_input("Variação IDA", value=0.0,
                                help="Alteração recente no desempenho acadêmico")

with col2:
    IEG = st.slider("IEG (Engajamento)", 0.0, 10.0, 5.0,
                    help="Indicador de participação e engajamento do aluno")
    IPP = st.slider("IPP (Psicopedagógico)", 0.0, 10.0, 5.0,
                    help="Avaliação do suporte pedagógico recebido")
    DELTA_IEG = st.number_input("Variação IEG", value=0.0,
                                help="Alteração recente no engajamento")

with col3:
    IAA = st.slider("IAA (Autoavaliação)", 0.0, 10.0, 5.0,
                    help="Como o aluno se avalia academicamente")
    IPV = st.slider("IPV (Ponto de Virada)", 0.0, 10.0, 5.0,
                    help="Momento crítico ou mudança no aprendizado")
    INDE = st.slider("INDE (Índice Geral)", 0.0, 10.0, 5.0,
                     help="Índice geral consolidado do aluno")
    DELTA_INDE = st.number_input("Variação INDE", value=0.0,
                                 help="Alteração recente no índice geral")

ENG_X_DESEMP = IDA * IEG  # feature extra

st.markdown("---")

# ==========================
# BOTÃO DE PREDIÇÃO
# ==========================
if st.button("🔍 Prever Risco"):

    # Criar DataFrame com os inputs
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

    # Fazer previsão
    pred = model.predict(dados)[0]
    prob = model.predict_proba(dados)[0][1]

    st.subheader("📈 Resultado da Previsão")

    # Exibir resultado com cores e estilo
    if pred == 1:
        st.markdown(f"""
        <div style='padding:20px; background-color:#FFCCCC; border-radius:10px; text-align:center'>
            <h2>⚠️ Alto risco de defasagem</h2>
            <p>Probabilidade: {prob:.2%}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='padding:20px; background-color:#CCFFCC; border-radius:10px; text-align:center'>
            <h2>✅ Baixo risco</h2>
            <p>Probabilidade: {prob:.2%}</p>
        </div>
        """, unsafe_allow_html=True)

    # Barra de progresso + gráfico
    st.progress(int(prob * 100))
    st.bar_chart(pd.DataFrame({'Risco (%)': [prob*100]}))

    st.markdown("---")
    st.info("📌 Interprete os resultados como indicação de risco com base nos indicadores. "
            "Use esta ferramenta para apoiar decisões pedagógicas e de acompanhamento do aluno.")

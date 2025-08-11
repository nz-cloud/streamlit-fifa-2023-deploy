import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.markdown("# FIFA 2023 OFFICAL DATASET! ⚽")
st.sidebar.markdown('Desenvolvido por [Nicolas Mendonça Lima](https://www.linkedin.com/in/nicolas-mendonca-lima)')

btn = st.link_button(
    "Acesse os dados no Kaggle",
    "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data"
)

st.markdown(
    """
    O conjunto de dados sobre jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores profissionais de futebol. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contratos e afiliações a clubes. 
    
    Com mais de **17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas, pesquisadores e entusiastas do futebol interessados em explorar vários aspectos do mundo do futebol, pois permite estudar os atributos dos jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento dos jogadores e desenvolvimento dos jogadores ao longo do tempo.

    """
)
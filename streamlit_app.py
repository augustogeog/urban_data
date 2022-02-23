#region IMPORTING PACKAGES
import streamlit as st
import plotly.express as px
st.set_page_config(layout="wide")
from plotly.subplots import make_subplots
import plotly.io as pio

#endregion importing packages

#region SIDEBAR
#df_territory = app.load_df_territory()
#uf = st.sidebar.selectbox(label='UF', options=df_territory.uf.unique())
#options = app.filter_municipalities_by_uf(uf=uf, df=df_territory)
#municipio = st.sidebar.selectbox(label='Município', options=options)
#cod_municipio = app.get_cod_municipio(df=df_territory, uf=uf, municipio=municipio)
#municipio_name = app.load_mun_name(cod_municipio=cod_municipio)
#endregion SIDEBAR


#region HEADER
st.markdown(f"<h1 style='text-align: right; color: black;'>Urban Trajectories</h1>", unsafe_allow_html=True)
#st.markdown(f'## {municipio}')
#endregion HEADER

file = 'plots/quartiles_percapita_gdp.json'
#fig = pio.read_json(file=file)

#st.plotly_chart(fig=fig, height=600, width=1400, use_container_width=True)

import plotly

st.write(plotly.__version__)



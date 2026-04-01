import pandas as pd
import streamlit as st
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTce46en4oO80s4P2Ep0yGCidjz3S5Ys6ibUtMAPArqRQy5-T-z6jor_Oi3Isci1ErBad3tHEalGwX1/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)
st.title("Monitoramento IoT")
st.line_chart(df[['temperatura', 'umidade']])
st.dataframe(df)


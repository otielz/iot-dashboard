app.py
import pandas as pd
import streamlit as st
url = "https://script.google.com/macros/s/AKfycbyGiCESu5WEgq8PYbEezEoUMaXnDzatD_OVEj4DPubVj2KYE0xgnTxTX-1QyoI5VzVH/exec"
df = pd.read_csv(https://script.google.com/macros/s/AKfycbyGiCESu5WEgq8PYbEezEoUMaXnDzatD_OVEj4DPubVj2KYE0xgnTxTX-1QyoI5VzVH/exec)
st.title("Monitoramento IoT")
st.line_chart(df[['temperatura', 'umidade']])
st.dataframe(df)
requirements.txt
streamlit
pandas

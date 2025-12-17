import os, requests, streamlit as st
from loguru import logger

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("FastIA Frontend")

value = st.number_input("Nombre", step=1)

if st.button("Calculer"):
    r = requests.post(f"{API_URL}/calcul", json={"value": int(value)})
    st.success(f"Résultat : {r.json()['result']}")

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Aprovação de HU", layout="centered")

CSV_FILE = "hus.csv"

# Função para carregar as HUs do arquivo CSV
def load_hus():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE).to_dict(orient="records")
    return []

# Carregar HUs ao iniciar
hus = load_hus()

# Obter o parâmetro de query 'id' da URL
hu_id = st.query_params.get("id", [None])[0]

if hu_id:
    # Procurar a HU com o ID fornecido
    hu = next((hu for hu in hus if hu["ID"] == hu_id), None)

    if hu:
        st.title(f"Aprovação de HU: {hu['ID']}")
        st.write(f"**Descrição:** {hu['Descrição']}")
        st.write(f"**Link Confluence:** {hu['Link Confluence']}")
        st.write(f"**Status:** {hu['Status']}")
        
        # Campos para aprovação
        approval = st.radio("Aprovação:", ("Aprovar", "Reprovar", "Aprovar com Observação", "Reprovar com Observação"))
        observation = st.text_area("Observação", "")
        
        if st.button("Enviar"):
            # Atualizar o status e observações
            if approval == "Aprovar":
                hu["Status"] = "Aprovada"
            elif approval == "Reprovar":
                hu["Status"] = "Reprovada"
            elif approval == "Aprovar com Observação" or approval == "Reprovar com Observação":
                hu["Status"] = "Observação"
                hu["Observação"] = observation
            
            # Salvar as alterações no arquivo CSV
            pd.DataFrame(hus).to_csv(CSV_FILE, index=False)
            st.success("✅ Status da HU atualizado!")
    else:
        st.error("❌ HU não encontrada!")
else:
    st.error("❌ ID da HU não fornecido!")

import streamlit as st
import pandas as pd
import os

# Configuração da página
st.set_page_config(page_title="Backoffice - Acompanhamento de HUs", layout="centered")

# Caminho do arquivo TSV
CSV_FILE = "hus.tsv"
# URL da página de aprovação no Streamlit Cloud
APPROVAL_URL = "https://aprovacaodehu.streamlit.app"

# Função para carregar as HUs do arquivo TSV
def load_hus():
    if not os.path.exists(CSV_FILE):
        return []  # Retorna lista vazia se o arquivo não existir
    try:
        df = pd.read_csv(CSV_FILE, sep="\t")
        if df.empty:
            return []  # Retorna lista vazia se o arquivo estiver vazio
        return df.to_dict(orient="records")
    except pd.errors.EmptyDataError:
        return []  # Retorna lista vazia se o arquivo estiver vazio
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return []

# Função para salvar as HUs no arquivo TSV
def save_hus(hus):
    if not hus:  # Se a lista de HUs estiver vazia
        df = pd.DataFrame(columns=["ID", "Descrição", "Link Confluence", "Link Aprovação", "Status", "Observação"])
    else:
        df = pd.DataFrame(hus)
    df.to_csv(CSV_FILE, index=False, sep="\t")

# Carregar HUs ao iniciar
if "hus" not in st.session_state:
    st.session_state.hus = load_hus()

# Título da página
st.title("📌 Acompanhamento de HUs e Aprovação")

# Formulário para adicionar HUs
with st.form("nova_hu"):
    hu_id = st.text_input("ID da HU")
    descricao = st.text_area("Descrição da HU")
    link_confluence = st.text_input("Link do Confluence")
    submit = st.form_submit_button("Adicionar HU")

    if submit:
        if hu_id and descricao and link_confluence:
            link_aprovacao = f"{APPROVAL_URL}/?id={hu_id}"  # Gera o link de aprovação
            nova_hu = {
                "ID": hu_id,
                "Descrição": descricao,
                "Link Confluence": link_confluence,
                "Link Aprovação": link_aprovacao,
                "Status": "Pendente",
                "Observação": ""
            }
            st.session_state.hus.append(nova_hu)
            save_hus(st.session_state.hus)
            st.success("✅ HU adicionada com sucesso!")
        else:
            st.error("⚠️ Todos os campos são obrigatórios!")

# Exibição das HUs cadastradas
st.write("## 📜 Histórias de Usuário Cadastradas")
if st.session_state.hus:
    for hu in st.session_state.hus:
        st.write(f"**ID:** {hu['ID']}")
        st.write(f"**Descrição:** {hu['Descrição']}")
        st.markdown(f"[🔗 Link Confluence]({hu['Link Confluence']})")
        st.markdown(f"[📝 Link para Aprovação]({hu['Link Aprovação']})")
        st.write(f"**Status:** {hu['Status']}")
        st.write("---")
else:
    st.info("Nenhuma HU cadastrada ainda.")

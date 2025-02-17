import streamlit as st
import pandas as pd
import os
from urllib.parse import urlparse, parse_qs

CSV_FILE = "hus.tsv"

# Função para carregar os dados das HUs
def load_hus():
    if not os.path.exists(CSV_FILE):
        st.warning("Arquivo hus.tsv não encontrado!")
        return []
    try:
        df = pd.read_csv(CSV_FILE, sep="\t", dtype=str)
        df = df.dropna(how="all")
        st.write(f"Dados carregados: {df}")
        return df.to_dict(orient="records")
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return []

# Função para capturar parâmetros da URL
def get_query_params():
    try:
        # Tenta capturar os parâmetros usando st.query_params (funciona no Streamlit Cloud)
        query_params = st.query_params
        if query_params:
            return query_params
    except Exception:
        pass

    # Se st.query_params não funcionar (rodando localmente), captura os parâmetros da URL manualmente
    try:
        from streamlit.web.server.websocket_headers import _get_websocket_headers
        headers = _get_websocket_headers()
        if headers and "Referer" in headers:
            url = headers["Referer"]
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            return {k: v[0] for k, v in query_params.items()}
    except Exception:
        pass

    return {}

# Captura o ID da HU da URL
query_params = get_query_params()
st.write(f"Parâmetros da URL: {query_params}")  # Depuração
hu_id = query_params.get("id", "").strip()
st.write(f"ID capturado: {hu_id}")  # Depuração

# Carregar HUs
hus = load_hus()

# Buscar HU pelo ID
st.write(f"Buscando HU com ID: {hu_id}")  # Depuração
hu = next((item for item in hus if str(item["ID"]).strip() == hu_id), None)
st.write(f"HU encontrada: {hu}")  # Depuração

# Layout da página
st.title("📝 Aprovação de HU")

if not hu_id:
    st.warning("⚠️ ID da HU não fornecido!")
elif not hu:
    st.error("❌ HU não encontrada!")
else:
    st.subheader(f"📌 {hu['ID']} - {hu['Descrição']}")
    st.write(f"🔗 [Link para o Confluence]({hu['Link Confluence']})")

    # Iframe para exibir o Confluence
    st.write("### Visualização do Confluence")
    st.markdown(f'<iframe src="{hu["Link Confluence"]}" width="100%" height="600"></iframe>', unsafe_allow_html=True)

    # Botões de status
    st.write("### Status da HU")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✅ Aprovar"):
            status = "Aprovado"
    with col2:
        if st.button("🟡 Aprovar com Observação"):
            status = "Aprovado com observação"
    with col3:
        if st.button("❌ Reprovar"):
            status = "Reprovado"

    # Observação (se necessário)
    observacao = st.text_area("📝 Observação", value=hu.get("Observação", ""))

    # Botão de salvar atualização
    if st.button("💾 Salvar Alterações"):
        for h in hus:
            if h["ID"].strip() == hu_id:
                h["Status"] = status
                h["Observação"] = observacao
                break
        pd.DataFrame(hus).to_csv(CSV_FILE, index=False, sep="\t")
        st.success("✅ Status atualizado com sucesso!")

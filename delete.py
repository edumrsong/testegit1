import streamlit as st
import os
import shutil

st.set_page_config(page_title="Apagar Pasta", layout="centered")

st.title("🗂️ Apagar Pasta Local")

st.write("Selecione qualquer arquivo dentro da pasta que deseja apagar.")

uploaded_file = st.file_uploader("Escolha um arquivo da pasta", type=None)

folder_path = None

if uploaded_file is not None:
    # Caminho temporário onde o Streamlit salva o arquivo
    temp_file_path = uploaded_file.name

    # Extrair a pasta
    folder_path = os.path.dirname(temp_file_path)

    st.success(f"Pasta detectada: **{folder_path}**")

    # Guardar caminho da pasta para usar depois
    st.session_state["selected_folder"] = folder_path

# Verificar se já existe pasta salva em sessão
if "selected_folder" in st.session_state:
    folder_path = st.session_state["selected_folder"]

    st.write("---")
    st.write(f"📁 **Pasta selecionada:** `{folder_path}`")

    # Botão de confirmação
    if st.button("❌ Apagar pasta COMPLETA"):
        st.session_state["confirm"] = True

    if st.session_state.get("confirm", False):
        st.error("Tem certeza? Esta ação é IRREVERSÍVEL!")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Sim, apagar!"):
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
                    st.success("Pasta apagada com sucesso! ✔")
                    st.session_state.clear()
                else:
                    st.error("A pasta não existe mais.")
        with col2:
            if st.button("Cancelar"):
                st.session_state["confirm"] = False
                st.info("Cancelado.")

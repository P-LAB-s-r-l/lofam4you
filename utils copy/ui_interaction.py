import streamlit as st
import os
from utils.file_management import create_folder

def language_selector():
    languages_list = ['Italiano', 'English', 'Español', 'Français', 'Deutsch', '中文 (Chinese)']
    old_selected_language = st.session_state.get('selected_language', None)
    old_selected_language_index = languages_list.index(old_selected_language) if old_selected_language else 0

    selected_language = st.selectbox("Seleziona la lingua per la documentazione:", languages_list, index=old_selected_language_index, key="language_box")

    if selected_language and old_selected_language is None:
        st.session_state.selected_language = selected_language

    return selected_language

def choose_file():
    uploaded_file = st.file_uploader("Seleziona un file zip", type="zip", accept_multiple_files=False)
    if uploaded_file is not None:
        create_folder("/tmp")
        temp_file_path = os.path.join("/tmp", uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File caricato: {uploaded_file.name}")
        return temp_file_path
    return None

    

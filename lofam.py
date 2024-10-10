import streamlit as st
from utils.ui_interaction import choose_file, language_selector
from utils.analysis_and_anon import analyze_and_anonimize_code, generate_documentation, generate_migration_documentation
from utils.file_management import write_file_content
from utils.constants import CODE_EXTENSIONS, DOCUMENTATION_FOLDER_PATH
import os
import shutil
import pypandoc


def lofam():
    st.set_page_config(page_title="LOFAM", layout="centered")
    st.title("LOFAM - Legacy Optimization Framework Analysis and Migration")

    with st.status("Configurazione iniziale", expanded=True, state="running") as initial_configuration_expander:
        initialize_session_state()
        selected_language = language_selector()
        provider, model, api_key = select_provider_model_and_api()
        selected_file_path = choose_file()
        update_session_state(selected_file_path, selected_language, api_key)
        
        if st.session_state.selected_file_path:
            st.write(f"File selezionato: {st.session_state.selected_file_path}")
    
    # Update the button state based on inputs
    if all([
        st.session_state.selected_file_path,
        provider,
        model,
        st.session_state.selected_language,
        st.session_state.api_key
    ]):
        st.session_state.start_button_disabled = False
    else:
        st.session_state.start_button_disabled = True

    initial_configuration_expander.update(label="Configurazione iniziale", expanded=True, state="running")
    
    # Button enabled/disabled logic based on conditions
    start_button = st.button("Inizia analisi", disabled=st.session_state.start_button_disabled)
    
    if start_button:
        initial_configuration_expander.update(label="Configurazione iniziale", expanded=False, state="complete")
        bar = st.progress(0, "Avvio in corso...")
        perform_analysis(bar, provider, model, api_key)

def initialize_session_state():
    if 'selected_file_path' not in st.session_state:
        st.session_state.selected_file_path = None
    if 'selected_language' not in st.session_state:
        st.session_state.selected_language = None
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None  # Initialize API key state
    if 'start_button_disabled' not in st.session_state:
        st.session_state.start_button_disabled = True  # Start as disabled

def update_session_state(selected_file_path, selected_language, api_key):
    if selected_file_path:
        st.session_state.selected_file_path = selected_file_path
    if selected_language:
        st.session_state.selected_language = selected_language
    if api_key:
        st.session_state.api_key = api_key  # Update API key

def select_provider_model_and_api():
    provider = st.selectbox(
        "Provider",
        ("Google", "OpenAI"),
        disabled=False,
    )

    model = None
    api_key = None  # Initialize API key

    if provider == "OpenAI":
        model = st.selectbox(
            "Modello",
            ("gpt-4o-mini", "gpt-4o"),
            disabled=False,
        )
    elif provider == "Google":
        model = st.selectbox(
            "Modello",
            ("gemini-1.5-flash", "gemini-1.5-pro"),
            disabled=False,
        )

    api_key = st.text_input("Inserisci la tua API key", type="password")  

    return provider, model, api_key 

def perform_analysis(bar, provider, model, api_key):
    all_unused_variables, analyze_directory = analyze_and_anonimize_code(
        zip_file_path=st.session_state.selected_file_path,
        bar=bar,
        code_extensions=CODE_EXTENSIONS
    )

    if all_unused_variables:
        unused_variables_content = '\n'.join([f"File: {file} - Variabile '{variable}' non utilizzata alla riga {line_number}"
                                              for file, variable, line_number in all_unused_variables])
        st.expander("Variabili non utilizzate trovate:", expanded=False).text_area("", unused_variables_content, height=200)
    else:
        st.expander("Variabili non utilizzate trovate:", expanded=False).info("Nessuna variabile non utilizzata trovata")

    documentation = generate_documentation(
        analyze_directory=analyze_directory,
        selected_language=st.session_state.selected_language,
        code_extensions=CODE_EXTENSIONS,
        bar=bar,
        documentation_directory=DOCUMENTATION_FOLDER_PATH,
        provider=provider,
        model=model,
        api_key=api_key
    )
    
    with st.expander("Documentazione completa", expanded=False):
        st.markdown(documentation)
        
    write_file_content(os.path.join(DOCUMENTATION_FOLDER_PATH, "documentazione_completa.md"), documentation)
    
    fullPath = os.path.join(DOCUMENTATION_FOLDER_PATH, "documentazione_completa.md")
    fullPathDocx = os.path.join(DOCUMENTATION_FOLDER_PATH, "documentazione_completa.docx")

    pypandoc.ensure_pandoc_installed()
    pypandoc.convert_file(fullPath, 'docx', outputfile=fullPathDocx)
    print(f"File convertito con successo e salvato come: {fullPathDocx}")

    migration_documentation = generate_migration_documentation(
        documentation_directory=DOCUMENTATION_FOLDER_PATH,
        bar=bar,
        selected_language=st.session_state.selected_language,
        provider=provider,
        model=model,
        api_key=api_key
    )
    
    with st.expander("Documentazione di migrazione", expanded=False):
        st.markdown(migration_documentation)
    
    write_file_content(os.path.join(DOCUMENTATION_FOLDER_PATH, "documentazione_migrazione_completa.md"), migration_documentation)
    
    fullPath = os.path.join(DOCUMENTATION_FOLDER_PATH, "documentazione_migrazione_completa.md")
    fullPathDocx = os.path.join(DOCUMENTATION_FOLDER_PATH, "documentazione_migrazione_completa.docx")

    pypandoc.ensure_pandoc_installed()
    pypandoc.convert_file(fullPath, 'docx', outputfile=fullPathDocx)
    print(f"File convertito con successo e salvato come: {fullPathDocx}")

    shutil.rmtree(analyze_directory)
    bar.progress(100, "Analisi completata!")
    st.success("Analisi completata!")

    with open(fullPathDocx, "rb") as file:
        st.download_button(
            label="Scarica documentazione e riavvia il processo",
            data=file,
            file_name="Documentazione.docx",
            mime="application/docx",
        )

if __name__ == "__main__":
    lofam()

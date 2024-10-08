import re
import os
import tempfile
import shutil
import math
import streamlit as st
from utils.file_management import read_file_content, write_file_content, estrai_zip, comprimi_zip, has_code_extension, get_zip_structure
from utils.config import analyze_content

def analizza_utilizzo_variabili(file_content):
    #VERSIONE BASE CHE CREA FILE CON VARIABILI E NUMERO DI RIGA DOVE SI TROVANO
    unused_variables = []
    used_variables = set()
    variable_map = {}

    # Ricostruisci il codice come stringa unica
    file_lines = file_content.split("\n")

    # Step 1: Find all string variable declarations (assuming they are initialized with an empty string)
    variable_declarations = []
    for i, line in enumerate(file_lines):
        matches = re.findall(r'\bstring\b\s+(\w+)\s*=\s*\"\"', line)
        for match in matches:
            variable_declarations.append((match, i + 1))  # (variabile, numero di riga)

    # Step 2: Track variable usages
    for variable_name, _ in variable_declarations:
        is_used_directly = re.search(rf'\b{variable_name}\b', file_content)

        if is_used_directly:
            used_variables.add(variable_name)

    # Step 3: Track variable assignments
    assignments = re.findall(r'(\w+)\s*=\s*(\w+)', file_content)

    for left_side, right_side in assignments:
        if left_side not in variable_map:
            variable_map[left_side] = right_side

    # Step 4: Propagate variable usage
    for left_variable, right_variable in variable_map.items():
        if right_variable in used_variables:
            used_variables.add(left_variable)

    # Step 5: Identify unused variables
    for variable_name, line_number in variable_declarations:
        if variable_name not in used_variables and variable_name not in variable_map:
            unused_variables.append((variable_name, line_number))  # Aggiungi variabile e riga

    # Step 6: Check for variables initialized as empty strings but never modified
    for variable_name, line_number in variable_declarations:
        if re.search(rf'\b{variable_name}\s*=\s*\"\"', file_content):
            unused_variables.append((variable_name, line_number))  # Aggiungi variabile e riga

    return unused_variables

def anonimizza_contenuto(file_content):
    # Esempi di regex per trovare parole sensibili
    file_lines = file_content.split("\n")

    contenuto = ""
    for line in file_lines:
        if(re.match(r'^\s{0,}//+?[a-zA-Z0-9_ \[\]",.#;<>\*\/+\-=\\@{}()]{0,}$',line) or re.match(r'^(?!\[WebService)[a-zA-Z0-9 \[\]",.#;<>+-=\\@].*//+?[a-zA-Z0-9 \[\]",.#;<>+-=\\@].*$',line)):
            continue
        if(re.match(r'^\s{0,}\-\-.{0,}$',line)):
            continue
        contenuto += line + "\n"

    # elimino tutti i commenti di tipo /**/
    pattern = r'/\*.*?\*/'
    contenuto = re.sub(pattern, "", contenuto, flags=re.DOTALL)
    
    return contenuto


# Funzione per l'analisi delle variabili inutilizzate e anonimizzazione
def analyze_and_anonimize_code(zip_file_path, bar, code_extensions):
    bar.progress(10, "Inizio l'analisi del file ZIP...")

    # Directory di output per i file ZIP
    original_dir = os.path.dirname(zip_file_path)
    output_zip_codeonly_path = os.path.join(original_dir, os.path.splitext(os.path.basename(zip_file_path))[0] + "_solo_codice.zip")
    output_zip_codeonly_anonymous_path = os.path.join(original_dir, os.path.splitext(os.path.basename(zip_file_path))[0] + "_solo_codice_anonimizzato.zip")

    # Estrazione e creazione dello zip solo codice
    bar.progress(20, "Creo lo zip con solo il codice...")
    if not os.path.isfile(output_zip_codeonly_path):
        extraction_directory = tempfile.mkdtemp()
        estrai_zip(zip_file_path, extraction_directory)
        comprimi_zip(output_zip_codeonly_path, extraction_directory)
        shutil.rmtree(extraction_directory)

    zip_structure = get_zip_structure(output_zip_codeonly_path)
    with st.expander("File da analizzare", expanded=False):
        for item in zip_structure:
            st.write(item)

    bar.progress(30, "Anonimizzazione del codice...")
    if not os.path.isfile(output_zip_codeonly_anonymous_path):
        code_anonymization_directory = tempfile.mkdtemp()
        estrai_zip(output_zip_codeonly_path, code_anonymization_directory)

        for root, dirs, files in os.walk(code_anonymization_directory):
            for file in files:
                file_path = os.path.join(root, file)
                contenuto = read_file_content(file_path)
                contenuto_anonimo = anonimizza_contenuto(contenuto)
                write_file_content(file_path, contenuto_anonimo)

        comprimi_zip(output_zip_codeonly_anonymous_path, code_anonymization_directory)
        shutil.rmtree(code_anonymization_directory)

    bar.progress(40, "Analisi delle variabili non utilizzate...")
    analyze_directory = tempfile.mkdtemp()
    estrai_zip(output_zip_codeonly_anonymous_path, analyze_directory)

    all_unused_variables = []
    for root, dirs, files in os.walk(analyze_directory):
        for file in files:
            if has_code_extension(file, code_extensions):
                file_path = os.path.join(root, file)
                contenuto = read_file_content(file_path)
                unused_variables = analizza_utilizzo_variabili(contenuto)
                all_unused_variables.extend([(file, variable, line_number) for variable, line_number in unused_variables])

    return all_unused_variables, analyze_directory

# Funzione per la generazione della documentazione
def generate_documentation(analyze_directory, selected_language, code_extensions, bar, documentation_directory, provider, model, api_key):
    documentation_content = ""
    count = 0
    for root, dirs, files in os.walk(analyze_directory):
        for file in files:
            if has_code_extension(file, code_extensions):
                file_path = os.path.join(root, file)
                count += 1
                bar.progress(50, f"Generazione della documentazione per il file {file}...")
                filename = os.path.basename(file_path)
                filecontent = read_file_content(file_path)
                documentation = analyze_content(filename, filecontent, selected_language, provider, model, api_key)
                with st.expander("Documentazione per il file " + file):
                    st.markdown(documentation)
                write_file_content(os.path.join(documentation_directory, file + ".md"), documentation)
                documentation_content += documentation + "\n\n"

    return documentation_content

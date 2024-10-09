import os
import zipfile
from utils.constants import CODE_EXTENSIONS, TO_EXCLUDE

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Funzione per leggere il contenuto di un file
def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            return file.read()

# Funzione per scrivere contenuto in un file
def write_file_content(file_path, content):
    folder_path = os.path.dirname(file_path)  # Ottieni il percorso della cartella
    create_folder(folder_path)  # Crea la cartella se non esiste
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Funzione per filtrare i file di codice
def has_code_extension(file_name, code_extensions):
    estensione = os.path.splitext(file_name)[1]
    return estensione in code_extensions

# Funzione per escludere i file
def exclude_file(file_name):
    return any(exclusion in str(file_name).lower() for exclusion in TO_EXCLUDE)

# Funzione per estrarre file ZIP in una cartella
def estrai_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Funzione per creare un nuovo ZIP solo con i file di codice
def comprimi_zip(output_zip_path, source_directory):
    with zipfile.ZipFile(output_zip_path, 'w') as new_zip:
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                if has_code_extension(file, CODE_EXTENSIONS):
                    file_path = os.path.join(root, file)
                    new_zip.write(file_path, os.path.relpath(file_path, source_directory))

# Funzione per ottenere la struttura di un file ZIP
def get_zip_structure(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        return zip_ref.namelist()

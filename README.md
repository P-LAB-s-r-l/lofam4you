# Lofam

- per eseguire il codice è necessario inserire nella directory principale un file .env con la seguente struttura:

LANGCHAIN_TRACING_V2={{bool}}
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="{{apikey}}"
LANGCHAIN_PROJECT="{{projectname}}"
OPENAI_API_KEY="{{openApiKey}}"

## esecuzione dell'applicazione

- lanciare il comando make all'interno della folder di progetto
- questo lancerà uno script python tk per la selezione del file e successivamente uno script py streamlit per la visualizzazione degli step
- all'avvio viene richiesto di selezionare la lingua con la quale verrà prodotta la documentazione

VEDERE [TODO](/TODO)

## creazione dell'eseguibile
```
cxFreeze --script utils/create_executable.py --target-name lofam.exe
```

## creazione docx
```bash
pandoc -o output.docx -f markdown -t docx .\documentation\input.md
```

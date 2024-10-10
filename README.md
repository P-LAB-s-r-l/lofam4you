# LOFAM MVP - LOFAM4YOU

[Visita l'MVP su Streamlit](https://lofam4you.streamlit.app/)

## Caratteristiche Principali

L'MVP è basato sulla piattaforma Streamlit e permette di utilizzare due provider di intelligenza artificiale (AI):

- **Google Gemini 1.5** (versione flash e versione pro)
- **OpenAI GPT-4o** e **GPT-4o-mini**

L'utente può scegliere liberamente quale provider utilizzare; entrambi sono supportati dalla piattaforma.

## Prerequisiti

1. Preparare un file archivio con estensione `.zip` (dimensione massima di 200MB) per permettere l'elaborazione completa dell'app legacy da parte del tool.
2. Le chiavi API di OpenAI e Gemini utilizzate per la demo sono private. È necessario disporre delle proprie API key per utilizzare i provider di AI.

## Utilizzo

1. Accedere via browser all'MVP utilizzando uno qualsiasi dei seguenti browser: Edge, Chrome, Firefox, ecc.
   - [https://lofam4you.streamlit.app/](https://lofam4you.streamlit.app/)

2. Caricare in input il file `.zip` dell'applicazione legacy.

3. Cliccare sul pulsante **Inizia Analisi**.

4. L'analisi verrà eseguita file per file, con informazioni visibili sulla pagina. In alto a destra, si può monitorare il caricamento e l'esecuzione di LOFAM.

5. Attendere il completamento dell'elaborazione. Il tempo di analisi può variare a seconda delle dimensioni del file `.zip` e del numero di file contenuti. Indicativamente, l'analisi di un centinaio di file può richiedere circa mezz'ora, anche a causa del numero di richieste inviate all'AI.

6. Al termine dell'elaborazione, scorrere fino in fondo alla pagina utilizzando la scrollbar e cliccare sul pulsante per il download della documentazione prodotta.

7. La documentazione generata comprende due documenti:
   - **Analisi profonda dell'AS-IS**
   - **Proposta di migrazione ad un nuovo stack tecnologico moderno**

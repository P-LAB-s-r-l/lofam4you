DOCUMENTATION_STYLE = 'markdown'
DOCUMENTATION_FOLDER_PATH = 'documentation'
CODE_EXTENSIONS = ['.py', '.java', '.js', '.cpp', '.c', '.cs', '.php', '.html', '.rb', '.go', '.ts', '.kt', '.asp', '.cshtml', '.cbl', '.cpy', '.sql']
SELECTED_PATH_FILE = 'selected_file.txt'
DOCUMENTATION_SYSTEM_PROMPT = '''

Fornisci una descrizione tradotta in {language} completa e dettagliata del codice presentato. 
Assicurati di coprire il suo scopo, le principali funzionalità e il contesto generale in cui viene utilizzato. 
Spiega come le diverse componenti del codice interagiscono tra loro.

il titolo deve essere: # Documentazione {filename}

## Funzioni e Classi
Per ogni funzione o classe nel codice:
- **[Nome funzione/classe]**: Descrivi in dettaglio lo scopo della funzione o classe, elencando i principali parametri e il loro significato, oltre al tipo di ritorno. Se applicabile, illustra anche eventuali eccezioni gestite. Esplora il flusso logico interno della funzione/classe, evidenziando i passaggi principali.

## Identificazione di Problemi e Vulnerabilità
Analizza il codice cercando possibili problemi o vulnerabilità. Identifica:
- Vulnerabilità di sicurezza
- Problemi di performance
- Errori logici
- Altre problematiche potenziali

## Miglioramenti e Ottimizzazioni
Suggerisci possibili ottimizzazioni o miglioramenti del codice:
- **Ottimizzazioni di performance**: Modifiche che potrebbero migliorare la velocità o ridurre l'uso di risorse.
- **Refactoring**: Miglioramenti nella struttura del codice per aumentare la leggibilità o manutenibilità.
- **Enhancement funzionali**: Aggiunte che potrebbero ampliare o migliorare le funzionalità esistenti.

## Best Practice e Conformità agli Standard
Valuta la conformità del codice rispetto alle best practice di programmazione e agli standard di sicurezza o qualità:
- **Codice pulito**: Verifica la chiarezza e la leggibilità (ad es. nomi di variabili significativi, funzioni ben definite e commentate).
- **Gestione degli errori**: Esamina la robustezza della gestione degli errori (ad es. eccezioni, codice di ritorno).
- **Conformità a standard di sicurezza o qualità**: Controlla se il codice segue linee guida di sicurezza, come l'OWASP, o altri standard pertinenti.

## Test e Validazione
Se non sono presenti, suggerisci possibili casi di test per verificare la correttezza del codice e identificare eventuali malfunzionamenti. 
Valuta:
- **Copertura dei test**: L’adeguatezza dei test presenti (unitari, di integrazione, ecc.).
- **Validazione**: Come il codice potrebbe essere validato con dati di esempio o scenari reali.

Codice:
{code}
'''
DOCUMENTATION_STYLE = 'markdown'
DOCUMENTATION_FOLDER_PATH = 'documentation'
CODE_EXTENSIONS = ['.py', '.java', '.js', '.cpp', '.c', '.cs', '.php', '.html', '.rb', '.go', '.ts', '.kt', '.asp', '.cshtml', '.cbl', '.cpy', '.sql']
TO_EXCLUDE = ['bootstrap','.min.js','jquery','/properties','modernizr','/obj', 'fullcalendar']
SELECTED_PATH_FILE = 'selected_file.txt'
DOCUMENTATION_SYSTEM_PROMPT = '''

Fornisci:
1) una descrizione tradotta in {language} completa e dettagliata del codice presentato. 
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

DOCUMENTATION_MIGRATION_SYSTEM_PROMPT = '''

Il tuo compito è generare una proposta tecnica di migrazione architetturale a partire dalla documentazione tecnica fornita riguardante un'applicazione esistente.
Considera l'applicativo nel sua complessità non solo dal punto di vista del codice, ma anche delle infrastrutture e delle tecnologie coinvolte.
Devi fornire una nuova architettura per l'applicativo nella sua totalità, non solo file per file 
La lingua che dovrai utilizzare è {language}.
La tua risposta deve includere i seguenti elementi fondamentali:

1. **Analisi dell'architettura attuale:**
   - Fornisci una panoramica dell'architettura attuale dell'applicazione complessiva (tecnologie utilizzate, linguaggi ecc).
   - Descrivi in modo dettagliato l'architettura corrente, le sue componenti principali, i pattern utilizzati e la loro interazione.
   - Metti in evidenza i punti deboli e i limiti dell'architettura attuale (es. colli di bottiglia delle performance, scalabilità ridotta, difficoltà di manutenzione, problemi di sicurezza, etc.).
   - Identifica eventuali problematiche ricorrenti nell'implementazione o nella gestione del codice (es. complessità del codice, dipendenze troppo forti, mancanza di modularità o flessibilità).

2. **Proposta di nuova architettura:**
   - Presenta una nuova soluzione architetturale che affronti in modo specifico i punti deboli identificati.
   - Spiega come la nuova architettura migliora aspetti come la scalabilità, la resilienza, la facilità di manutenzione, la sicurezza e le prestazioni.
   - Illustra i pattern architetturali che proponi (es. microservizi, event-driven architecture, serverless, containerizzazione) e il loro impatto positivo.
   - Descrivi le tecnologie o gli strumenti aggiuntivi che saranno introdotti e come integrano la nuova architettura.

3. **Impatto sulla migrazione:**
   - Fornisci una roadmap o strategia per la migrazione graduale dalla vecchia alla nuova architettura.
   - Definisci le fasi principali del processo di migrazione (es. creazione di microservizi, migrazione database, containerizzazione, etc.).
   - Indica i potenziali rischi associati alla migrazione e come mitigarli.

4. **Valutazione e metriche:**
   - Suggerisci metriche chiave per misurare l'efficacia della nuova architettura rispetto a quella attuale (es. tempi di risposta, throughput, costi operativi, tempi di downtime).
   - Indica come monitorare il successo della migrazione durante e dopo la sua implementazione.

5. **Best Practices e raccomandazioni:**
   - Fornisci raccomandazioni di best practices da seguire durante l'implementazione della nuova architettura.
   - Sottolinea eventuali decisioni tecniche che dovrebbero essere prese con attenzione (es. trade-off di design, scelte di infrastruttura).

Ecco la documentazione tecnica del codice dell'applicazione esistente.
{documentation}
'''
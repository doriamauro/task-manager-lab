# Task Manager Lab

Repository didattico per il corso **Git e GitHub per lo sviluppo collaborativo Agile**.

## Primo giorno: solo Git locale

Clona il repository una sola volta:

```bash
git clone https://github.com/doriamauro/task-manager-lab.git
cd task-manager-lab
```

Dopo il clone lavora in locale: **non eseguire push**, non creare Pull Request e non modificare il repository remoto.

## Requisiti e avvio

- Python 3.10 o successivo (nessuna libreria esterna)
- Git e VS Code (estensione Git Graph consigliata)

Dalla radice del progetto:

```bash
python -m app.main
python -m unittest discover -s tests -v
```

Su Windows, se `python` non è disponibile, prova `py`.

## Moduli

- `app/task.py`: modello del task, con spazio per priorità e scadenza.
- `app/task_service.py`: gestione dei task, con funzioni da completare.
- `app/task_filter.py`: ricerca e filtri.
- `app/task_report.py`: riepiloghi e statistiche.
- `app/main.py`: esempio eseguibile.
- `tests/`: test iniziali con `unittest`.

Il codice è volutamente semplice e parzialmente sviluppato. Gli esercizi dettagliati sono forniti dal docente separatamente; non è necessario completare tutti i TODO prima di iniziare il corso.

**Importante:** durante gli esercizi di reset, clean e reflog usa solo la tua copia locale.

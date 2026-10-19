"""Riepiloghi base; pronto per esercizi di modifica e cherry-pick."""
from .task import Task


def riepilogo(tasks: list[Task]) -> dict[str, int]:
    completati = sum(1 for task in tasks if task.completato)
    return {
        "totali": len(tasks),
        "completati": completati,
        "aperti": len(tasks) - completati,
    }


# TODO (esercizio): aggiungere percentuali e statistiche per priorita.

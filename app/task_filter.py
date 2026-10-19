"""Filtri semplici da ampliare durante le esercitazioni."""
from .task import Task


def filtra_per_stato(tasks: list[Task], completato: bool) -> list[Task]:
    return [task for task in tasks if task.completato == completato]


def cerca_per_titolo(tasks: list[Task], testo: str) -> list[Task]:
    """Ricerca senza distinzione tra maiuscole e minuscole."""
    query = testo.lower()
    return [task for task in tasks if query in task.titolo.lower()]


# TODO (esercizio): introdurre filtri per priorita.

"""Operazioni sui task. Alcune funzioni sono volutamente semilavorate."""
from .task import Task


def aggiungi_task(tasks: list[Task], titolo: str) -> Task:
    """Aggiunge un task con identificativo progressivo."""
    nuovo_id = max((task.id for task in tasks), default=0) + 1
    task = Task(id=nuovo_id, titolo=titolo)
    tasks.append(task)
    return task


def completa_task(tasks: list[Task], task_id: int) -> bool:
    """Segna un task come completato, se presente."""
    for task in tasks:
        if task.id == task_id:
            task.completato = True
            return True
    return False


def elimina_task(tasks: list[Task], task_id: int) -> bool:
    """TODO: implementare l'eliminazione di un task per ID."""
    return False

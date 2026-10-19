"""Demo eseguibile senza dipendenze esterne."""
from .task_service import aggiungi_task, completa_task
from .task_filter import filtra_per_stato
from .task_report import riepilogo


def main() -> None:
    tasks = []
    aggiungi_task(tasks, "Studiare git status")
    aggiungi_task(tasks, "Creare un branch")
    aggiungi_task(tasks, "Provare git merge")
    completa_task(tasks, 1)

    print("TASK MANAGER LAB")
    for task in tasks:
        stato = "OK" if task.completato else "DA FARE"
        print(f"[{stato}] {task.id}: {task.titolo}")
    print("Riepilogo:", riepilogo(tasks))
    print("Task aperti:", len(filtra_per_stato(tasks, False)))


if __name__ == "__main__":
    main()

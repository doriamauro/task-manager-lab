"""Test iniziali con unittest, senza pacchetti aggiuntivi."""
import unittest

from app.task import Task
from app.task_service import aggiungi_task, completa_task
from app.task_filter import filtra_per_stato, cerca_per_titolo
from app.task_report import riepilogo


class TaskManagerTests(unittest.TestCase):
    def test_aggiungi_task(self):
        tasks = [Task(2, "Esistente")]
        nuovo = aggiungi_task(tasks, "Nuovo")
        self.assertEqual(nuovo.id, 3)
        self.assertEqual(len(tasks), 2)

    def test_completa_task(self):
        tasks = [Task(1, "Studiare")]
        self.assertTrue(completa_task(tasks, 1))
        self.assertTrue(tasks[0].completato)
        self.assertFalse(completa_task(tasks, 99))

    def test_filtri(self):
        tasks = [Task(1, "Git Graph", True), Task(2, "git log")]
        self.assertEqual(len(filtra_per_stato(tasks, False)), 1)
        self.assertEqual(len(cerca_per_titolo(tasks, "GIT")), 2)

    def test_riepilogo(self):
        tasks = [Task(1, "A", True), Task(2, "B")]
        self.assertEqual(riepilogo(tasks), {"totali": 2, "completati": 1, "aperti": 1})


if __name__ == "__main__":
    unittest.main()

"""Modello dati minimale: estendibile negli esercizi Git."""
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    titolo: str
    completato: bool = False
    # TODO (esercizio): aggiungere priorita e scadenza.

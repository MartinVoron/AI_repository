# Prototype d'agent de développement IA

Ce repository initialise une base minimale pour construire progressivement un agent de développement logiciel piloté par GitHub.

## Objectif

Le but de ce projet est de préparer une architecture simple et extensible qui permettra ensuite d'implémenter un agent capable de :

1. comprendre un repository ;
2. analyser une tâche décrite en langage naturel ;
3. proposer un plan ;
4. modifier le code ;
5. créer ou modifier des tests ;
6. exécuter les tests ;
7. corriger les problèmes ;
8. ouvrir une Pull Request ;
9. faciliter la revue humaine.

> Cette étape **n'implémente pas** l'agent IA lui-même.

## Architecture initiale

```text
.
├── src/
│   └── ai_dev_agent_demo/
│       ├── __init__.py
│       └── app.py
├── tests/
│   └── test_app.py
└── .github/
    ├── copilot-instructions.md
    └── workflows/
        └── tests.yml
```

- `src/ai_dev_agent_demo/app.py` : mini application de démonstration exécutable (inclut `add(a, b)` pour additionner deux nombres).
- `tests/test_app.py` : test automatisé minimal.
- `.github/workflows/tests.yml` : exécution automatique des tests sur Pull Request.
- `.github/copilot-instructions.md` : consignes générales pour Copilot sur ce repository.

## Prérequis

- Python 3.11+ (ou version compatible avec `unittest` standard)

## Installation

Aucune dépendance externe n'est requise pour ce prototype.

```bash
git clone https://github.com/MartinVoron/AI_repository.git
cd AI_repository
```

## Exécuter l'application de démonstration

```bash
PYTHONPATH=src python -m ai_dev_agent_demo.app
```

## Lancer les tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

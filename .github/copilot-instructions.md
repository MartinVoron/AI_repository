# Instructions Copilot pour ce repository

## Contexte

Ce repository sert de base pour un futur agent IA de développement logiciel.

## Règles de contribution

1. Garder l'architecture simple et extensible.
2. Implémenter des changements petits et ciblés.
3. Ajouter ou mettre à jour les tests pour chaque changement fonctionnel.
4. Vérifier localement les tests avant de proposer une Pull Request.
5. Ne pas ajouter de dépendances inutiles.
6. Ne jamais ajouter de secrets ou clés API dans le code.
7. Maintenir une documentation à jour dans `README.md`.

## Commandes utiles

- Exécuter l'application de démonstration :
  - `PYTHONPATH=src python -m ai_dev_agent_demo.app`
- Exécuter les tests :
  - `PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v`

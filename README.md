# Study-chatbot
# StudyBot - Assistant d'Étude IA

StudyBot est un chatbot intelligent conçu pour aider les étudiants dans leur apprentissage. Il peut répondre à des questions à partir d'une base de FAQ prédéfinie et analyser des documents fournis par l'utilisateur pour répondre à des questions spécifiques.

## Fonctionnalités

- Réponses aux questions fréquemment posées (FAQ)
- Analyse de documents personnalisés
- Interface en ligne de commande simple
- Support du français
- Utilisation du modèle DistilBERT pour l'analyse de texte

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez le dépôt :
   ```bash
git clone [url-du-repo]
cd Study-chatbot

2. Installez les dépendances :
  ```bash
   pip install -r requirements.txt

## Utilisation

1. Lancez le bot :
   ```bash
     python main.py

2. Commandes disponibles :
- `upload` : Pour ajouter un document à analyser
- `quit` ou `END` : Pour quitter le programme
- Tapez simplement votre question pour obtenir une réponse

### Exemple d'utilisation :
```CSV
  Vous : Qu'est-ce que l'IA ?
  StudyBot : L'intelligence artificielle (IA) est la simulation de l'intelligence humaine par des machines, en particulier des systèmes informatiques.
  Vous : upload
  Entrez votre texte (tapez 'END' pour terminer) :
  L'eau est une ressource précieuse qu'il faut préserver.
  La pollution de l'eau est un problème majeur dans notre société.
  END
  Vous : Quel est le problème majeur mentionné ?
  StudyBot : La pollution de l'eau est un problème majeur dans notre société.

## Structure du projet

- `main.py` : Point d'entrée du programme
- `chatbot.py` : Classe principale du chatbot
- `faqs.json` : Base de données des questions fréquentes
- `requirements.txt` : Liste des dépendances

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

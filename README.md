# Data Pipeline Météo : Collecte et Stockage de Données Météorologiques

## Introduction

Bienvenue dans le projet **Data Pipeline Météo**, une solution simple et efficace conçue pour automatiser la collecte de données météorologiques en temps réel et leur stockage dans une base de données relationnelle.

Ce pipeline, développé en Python, utilise l'API populaire d'OpenWeatherMap pour extraire des informations clés sur la météo de plusieurs villes prédéfinies, puis les insère dans une base de données MySQL. Il s'agit d'un excellent exemple de pipeline **ETL (Extract, Transform, Load)** léger et fonctionnel.

L'objectif de ce projet est de fournir une base solide pour quiconque souhaite :
1.  Apprendre les fondamentaux de l'intégration de données.
2.  Mettre en place un système de surveillance météorologique personnalisé.
3.  Disposer d'un jeu de données historique pour des analyses ultérieures.

---

## Fonctionnement du Pipeline

Le script `main.py` exécute les étapes suivantes :

| Étape | Description | Outil / Technologie |
| :--- | :--- | :--- |
| **1. Extraction (E)** | Le script se connecte à l'API OpenWeatherMap pour chaque ville de la liste. Il récupère les données brutes (température, pression, vent, humidité, description) en utilisant les unités métriques et la langue française. | `requests` (Python), OpenWeatherMap API |
| **2. Transformation (T)** | Les données JSON reçues sont analysées, les champs pertinents sont extraits et la date/heure actuelle est ajoutée pour l'horodatage. | Python |
| **3. Chargement (L)** | Les données structurées sont insérées dans la table `meteo_data` de la base de données MySQL. | `mysql.connector` (Python), MySQL |

## Prérequis

Avant de pouvoir exécuter ce pipeline, vous devez disposer des éléments suivants :

1.  **Python 3.x** installé sur votre système.
2.  Un accès à un serveur **MySQL** (local ou distant).
3.  Une **clé d'API OpenWeatherMap** (gratuite ou payante).

## Installation et Configuration

Suivez ces étapes pour mettre en place le projet.

### 1. Cloner le Dépôt

```bash
git clone https://github.com/hbadir-habinou/Data_Pipeline_Meteo.git
cd Data_Pipeline_Meteo
```

### 2. Installer les Dépendances Python

Le script nécessite deux bibliothèques Python : `requests` pour les appels API et `mysql-connector-python` pour la connexion à la base de données.

```bash
pip install requests mysql-connector-python
```

### 3. Configuration des Accès (Fichier `config.py`)

Pour des raisons de sécurité, les identifiants de connexion et la clé d'API sont stockés dans un fichier séparé, `config.py`, qui n'est pas inclus dans le dépôt.

Créez un fichier nommé `config.py` à la racine du projet et ajoutez-y les informations suivantes, en remplaçant les valeurs par vos propres identifiants :

```python
# Configuration de la Base de Données MySQL
DB_HOST = "votre_hote_mysql"
DB_USER = "votre_utilisateur_mysql"
DB_PASSWORD = "votre_mot_de_passe_mysql"
DB_NAME = "votre_base_de_donnees"

# Clé d'API OpenWeatherMap
API_KEY = "votre_cle_api_openweathermap"
```

### 4. Configuration de la Base de Données

Vous devez créer la table `meteo_data` dans votre base de données MySQL pour que le script puisse y insérer les données.

Voici le schéma SQL recommandé (à adapter si nécessaire) :

```sql
CREATE TABLE meteo_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ville VARCHAR(100) NOT NULL,
    date_releve DATETIME NOT NULL,
    temperature DECIMAL(5, 2),
    humidite INT,
    pression INT,
    vitesse_vent DECIMAL(5, 2),
    description VARCHAR(255)
);
```

## Utilisation

Une fois la configuration terminée, vous pouvez exécuter le pipeline en lançant le script principal :

```bash
python main.py
```

Le script va alors :
1.  Se connecter à la base de données.
2.  Parcourir la liste des villes.
3.  Afficher les données collectées dans la console.
4.  Insérer les données dans la table `meteo_data`.
5.  Se déconnecter de la base de données.

## Personnalisation

Le script est conçu pour être facilement modifiable :

| Élément | Fichier | Ligne(s) | Commentaire |
| :--- | :--- | :--- | :--- |
| **Villes** | `main.py` | Ligne 16 | Modifiez la liste `villes` pour inclure les emplacements de votre choix. |
| **Paramètres API** | `main.py` | Ligne 19 | Vous pouvez ajuster les paramètres `units` (métrique, impérial) ou `lang` (langue de la description) dans l'URL de l'API. |
| **Schéma de la Table** | `main.py` | Ligne 44 | Si vous modifiez le schéma de votre table MySQL, assurez-vous d'ajuster la requête `INSERT INTO` en conséquence. |

## Structure du Projet

```
Data_Pipeline_Meteo/
├── main.py             # Le script principal du pipeline
└── config.py           # Fichier de configuration (à créer par l'utilisateur)
└── README.md           # Ce document
```




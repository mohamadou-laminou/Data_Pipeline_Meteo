# Pipeline ETL Météo & Analyse Touristique

Ce projet est un pipeline de données (ETL) conçu pour automatiser la surveillance des conditions climatiques de cinq villes clés pour une analyse touristique : **Montpellier, Paris, Yaoundé, Maroua et Québec**.

Il a été réalisé dans le cadre d'un projet personnel en Data Engineering afin de mettre en pratique les concepts d'ingestion de données via API, de stockage relationnel et de Business Intelligence.

---

## Objectifs du Projet

L'objectif n'est pas uniquement l'affichage de la météo, mais la construction d'une architecture logicielle capable de :

- **Récupérer automatiquement** des données météorologiques en temps réel via une API externe.
- **Traiter et nettoyer** ces données (Parsing JSON, standardisation des unités).
- **Stocker l'historique** dans une base de données relationnelle structurée (MySQL).
- **Visualiser les indicateurs clés** (Température, Humidité, Vent) via un tableau de bord interactif Power BI.

---

## Architecture Technique

Le projet repose sur une architecture locale automatisée, composée de trois briques distinctes :

### Base de Données (MySQL)
Stockage persistant des données.  
Une table unique `meteo_data` centralise l'historique des relevés pour toutes les villes ciblées.

### ETL (Python)
Script responsable du cycle de vie de la donnée :

- **Extraction** : Connexion à l'API **OpenWeatherMap** (Endpoint Current Weather).
- **Transformation** : Sélection des métriques pertinentes et nettoyage avec **Pandas**.
- **Chargement** : Insertion sécurisée des données dans MySQL via `mysql-connector`.

### Dashboard (Power BI)
Interface de visualisation connectée directement à la base MySQL pour l'analyse comparative des villes.

---

## Stack Technique

- **Python 3.x** : Langage principal pour le script d'automatisation.
- **MySQL** : Système de gestion de base de données relationnelle (SGBD) pour l'historisation.
- **Pandas** : Bibliothèque utilisée pour la manipulation et le nettoyage des données brutes.
- **Requests** : Gestion des appels API HTTP.
- **Power BI Desktop** : Outil de Business Intelligence pour la dataviz.
- **Task Scheduler (Windows)** : Assure l'orchestration et l'exécution périodique du script.

---

## Installation et Démarrage

### Prérequis

- Python 3.10+
- Serveur MySQL (local ou distant)
- Power BI Desktop
- Git

---

### 1. Cloner le dépôt

```bash
git clone https://github.com/mohamadou-laminou/Data_Pipeline_Meteo.git
cd Data_Pipeline_Meteo


---

### 2. Configuration

Créer un fichier `config.py` à la racine du projet (non inclus dans le dépôt par sécurité) pour définir vos clés :

```python
API_KEY = "VOTRE_CLE_OPENWEATHER"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "votre_mot_de_passe"
DB_NAME = "projet_meteo"



```markdown
---

### 3. Installation des dépendances

```bash
pip install -r requirements.txt

```markdown
---

### 4. Lancement

Exécutez le script pour initier la première collecte de données :

```bash
python main.py


```markdown
---

### 5. Visualisation

Ouvrez le fichier `Dashboard.pbix` avec Power BI et cliquez sur "Actualiser" pour charger les données depuis votre base MySQL locale.

---

## Pistes d'amélioration (Roadmap)

Ce projet constitue une première version fonctionnelle. Les évolutions suivantes sont envisagées :

- Conteneurisation : Migration vers Docker pour ne plus dépendre de l'environnement local.
- Orchestration : Remplacement du planificateur Windows par un outil dédié comme Apache Airflow.
- Alerting : Mise en place de notifications (Email / Discord) en cas de conditions météo extrêmes.

---

## Auteur

Laminou Mohamadou  
Étudiant Ingénieur à l'EPF Montpellier









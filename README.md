# 🧪 Automatisation des tests de la plateforme Vocodata

Projet d'automatisation des tests fonctionnels de la plateforme web **Vocodata**, développé en **Python** avec **Selenium** et **Pytest**.

> Projet réalisé dans le cadre d'un **stage de fin d'études** chez **Smart Creative Solutions** (Marrakech), à distance, du **17 avril 2025 au 3 juin 2025**.

---

## 📋 Table des matières

- [Contexte](#-contexte)
- [Objectifs](#-objectifs)
- [La plateforme Vocodata](#-la-plateforme-vocodata)
- [Scénarios de test](#-scénarios-de-test)
- [Technologies et outils](#-technologies-et-outils)
- [Structure du projet](#-structure-du-projet)
- [Gestion des données de test (Excel)](#-gestion-des-données-de-test-excel)
- [Installation](#-installation)
- [Données de test et identifiants](#-données-de-test-et-identifiants)
- [Lancer les tests](#-lancer-les-tests)
- [Auteur](#-auteur)

---

## 📖 Contexte

Les tests de la plateforme Vocodata étaient effectués **manuellement** : c'était long, coûteux en ressources et sujet aux erreurs ou aux oublis, surtout après chaque mise à jour.

**Solution :** mettre en place une suite de tests automatisés qui vérifie rapidement et de façon reproductible les fonctionnalités principales de la plateforme.

## 🎯 Objectifs

- Automatiser les **tests fonctionnels** et de **régression**
- Gagner du temps lors des phases de validation et des mises à jour
- Étendre la couverture des tests avec un large éventail de scénarios
- Renforcer la stabilité de la plateforme grâce à des tests fréquents et systématiques

## 🎙️ La plateforme Vocodata

Vocodata est une plateforme de gestion et d'analyse des enregistrements vocaux. Ses principales fonctionnalités :

- **Espace membre** : gestion des utilisateurs et de leurs permissions
- **Grille d'évaluation** : critères d'évaluation personnalisés
- **Qualification des appels** : transformation des appels en données exploitables
- **Tableau de bord** : vue d'ensemble des performances
- **Contenu sensible** : détection de mots et contenus sensibles (liste noire)
- **Paiement en ligne** : transactions sécurisées

Deux profils d'utilisateurs : **Super Administrateur** (droits étendus) et **utilisateur standard** (droits limités).

## ✅ Scénarios de test

### 1. Navigation, connexion et authentification
- Navigation entre les pages publiques
- Création d'un compte avec des données valides
- Création d'un compte avec des données déjà utilisées
- Connexion avec une adresse e-mail incorrecte
- Récupération du mot de passe oublié
- Connexion réussie

### 2. Compte Super Administrateur
- Création, modification et suppression d'utilisateurs
- Gestion des entreprises (modification, validation, suppression)
- Export des logs au format Excel
- Navigation dans les sections d'administration
- Validation des opérations critiques

### 3. Compte utilisateur standard
- Connexion et navigation dans l'espace personnel
- Ajout, modification et suppression de grilles, compétences et mots
- Gestion des doublons (ajout d'un mot déjà existant)
- Paiements par lien et par carte bancaire
- Chargement et analyse de fichiers audio

## 🛠️ Technologies et outils

| Outil | Rôle |
|---|---|
| **Python** | Langage des scripts d'automatisation |
| **Selenium WebDriver** | Simulation des actions utilisateur dans le navigateur |
| **ChromeDriver** | Pilote du navigateur Google Chrome |
| **Pytest** | Organisation et exécution des tests |
| **pytest-html** | Génération de rapports HTML |
| **openpyxl** | Lecture et écriture des fichiers Excel |
| **Anaconda** | Gestion de l'environnement virtuel (`test_project`) |
| **Visual Studio Code** | Éditeur de code |
| **GitHub Actions** | Intégration continue |

**Méthodes de test :** tests fonctionnels, tests de régression, test en boîte noire, approche orientée données (*data-driven*) et design pattern **Page Object Model (POM)**.

## 📁 Structure du projet

```
test_vocodata/
├── all_tests/            # Fichiers de tests automatisés (par fonctionnalité)
├── assets/               # Ressources : fichier Excel de scénarios, images, audio
├── drivers/              # WebDriver (ChromeDriver)
├── pages_Sofia/          # Page Objects : utilisateur standard
├── pages_super_admin/    # Page Objects : Super Administrateur
├── rapport_tests.html    # Rapport de tests généré
├── .gitignore            # Fichiers exclus du dépôt (identifiants, rapports...)
└── README.md
```

**Page Object Model :** chaque page de l'application est représentée par une classe Python qui regroupe ses éléments (champs, boutons, messages) et les actions possibles. Si l'interface change, il suffit de mettre à jour la classe concernée.

## 📊 Gestion des données de test (Excel)

Les scénarios et les données de test sont centralisés dans un fichier Excel lu avec **openpyxl**. Chaque ligne est un cas de test :

| Colonne | Contenu |
|---|---|
| `id` | Identifiant du cas (ex. `TC003`) |
| `name` | Type d'action (inscription, login...) |
| `input` | URL cible et données d'entrée |
| `Process` | Objectif du test |
| `output` | Informations récupérées sur la plateforme |
| `expected output` | Résultat attendu |
| `validation` | `ok` ou `ko` après comparaison automatique |

Cela permet d'ajouter ou de modifier des scénarios **sans toucher au code**.

> ⚠️ Le fichier Excel réel contient des identifiants de comptes : il n'est **pas publié**. Utilisez un fichier d'exemple avec des données fictives.

## 🚀 Installation

### Prérequis
- Python 3.9 ou plus
- Google Chrome et le **ChromeDriver** correspondant à sa version
- (Recommandé) Anaconda

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/hassna1mezouara/test_vocodata.git
cd test_vocodata

# 2. Créer l'environnement virtuel
conda create -n test_project python=3.11
conda activate test_project

# 3. Installer les dépendances
pip install selenium pytest pytest-html openpyxl
```

Placez ensuite le **ChromeDriver** dans le dossier `drivers/`.

## 🔐 Données de test et identifiants

Les identifiants des comptes de test (Super Administrateur, utilisateur standard, données d'inscription) sont lus **depuis le fichier Excel** de scénarios. Ce fichier contient de vrais comptes : il n'est **pas publié** sur GitHub (voir `.gitignore`).

Pour lancer les tests, il faut donc :

1. Créer votre propre fichier Excel dans le dossier `assets/`, en suivant la structure décrite ci-dessus (colonnes `id`, `name`, `input`, `Process`, `output`, `expected output`, `validation`).
2. Y renseigner **vos propres** identifiants de test.

Un fichier modèle avec des données fictives (`*.example.xlsx`) peut être fourni dans `assets/`.

## ▶️ Lancer les tests

```bash
# Tous les tests, avec rapport HTML
pytest all_tests --html=rapport_tests.html --self-contained-html

# Un seul fichier de tests
pytest all_tests/nom_du_fichier.py -v
```

## 👩‍💻 Auteur

**Hassna Mezouara**
Étudiante en Informatique décisionnelle et science des données
École Supérieure de Technologie d'Essaouira, Université Cadi Ayyad

**Encadrants :** M. Issam Sahraoui et M. Faysal Naciri

---

📌 Projet à but pédagogique réalisé lors d'un stage de fin d'études.

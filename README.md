# 📚 Système de Gestion de Bibliothèque - Django

Application web complète de gestion de bibliothèque développée avec Django, permettant de gérer des livres, auteurs et emprunts avec une interface moderne et intuitive.

## 🚀 Fonctionnalités

### 📖 Gestion des Livres
- **Liste des livres** avec pagination (10 livres/page)
- **Recherche avancée** : par titre, ISBN, auteur
- **Filtres** : par catégorie et par auteur
- **Détails complets** : ISBN, catégorie, année, éditeur, disponibilité, statistiques d'emprunt
- **Gestion du stock** : suivi des exemplaires disponibles/total

### ✍️ Gestion des Auteurs
- **Liste des auteurs** avec pagination (10 auteurs/page)
- **Recherche** : par nom ou prénom
- **Profil détaillé** : biographie, nationalité, dates de naissance/décès, site web
- **Liste des livres** de chaque auteur

### 📋 Gestion des Emprunts
- **Liste des emprunts actifs**
- **Détection automatique des retards**
- **Historique complet** avec recherche par nom d'emprunteur
- **Création d'emprunt** avec validation (uniquement livres disponibles)
- **Retour de livre** avec mise à jour automatique du stock
- **Durée par défaut** : 14 jours

### 🎨 Interface Utilisateur
- **Design moderne** avec Tailwind CSS
- **Navigation intuitive** : header avec toutes les sections
- **Responsive** : s'adapte aux mobiles, tablettes et desktop
- **Messages de feedback** : succès, erreurs, confirmations

### ⚙️ Interface d'Administration Django
- **Gestion des livres** :
  - Affichage : titre, auteur, ISBN, catégorie, disponibilité
  - Filtres : catégorie, auteur, année
  - Recherche : titre, ISBN, auteur
  - Actions : marquer comme indisponible
  - Inlines : voir les emprunts actifs
  - Validation : available_copies ≤ total_copies

- **Personnalisation** :
  - Header customisé : "Administration de la Bibliothèque"
  - Messages de confirmation personnalisés
  - Badges colorés pour la disponibilité

### 📄 Pages Statiques
- **Page d'accueil** : statistiques, derniers livres ajoutés
- **À propos** : mission, services, horaires
- **Contact** : coordonnées, formulaire

---

## 📦 Installation

### Prérequis
- Python 3.8+
- pip
- virtualenv (recommandé)

### Étapes d'installation

1. **Cloner le projet**
```bash
cd "Python avancée"
```

2. **Créer un environnement virtuel**
```bash
python -m venv Bibiloteque
source Bibiloteque/bin/activate  # Linux/Mac
# ou
Bibiloteque\Scripts\activate  # Windows
```

3. **Installer les dépendances**
```bash
pip install django pillow
```

4. **Configurer la base de données**

Copier le fichier de configuration :
```bash
cp core/settings_local.py.example core/settings_local.py
```

Éditer `core/settings_local.py` et configurer selon vos besoins (la config par défaut avec SQLite fonctionne directement).

5. **Appliquer les migrations**
```bash
python manage.py migrate
```

6. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```
Suivez les instructions pour créer votre compte admin.

7. **Lancer le serveur**
```bash
python manage.py runserver
```

L'application est accessible à : **http://127.0.0.1:8000/**

---

## 🔑 Accès à l'Administration

### URL d'administration
http://127.0.0.1:8000/admin/

### Identifiants
Utilisez les identifiants créés lors de l'étape `createsuperuser`.

---

## 📖 Guide d'utilisation

### Navigation

#### En tant qu'utilisateur

1. **Page d'accueil** (`/`)
   - Vue d'ensemble des statistiques
   - Derniers livres ajoutés
   - Accès rapide aux fonctionnalités

2. **Livres** (`/book/`)
   - Parcourir tous les livres
   - Utiliser la recherche pour trouver un livre spécifique
   - Filtrer par catégorie ou auteur
   - Cliquer sur un livre pour voir ses détails

3. **Auteurs** (`/author/`)
   - Parcourir tous les auteurs
   - Rechercher par nom ou prénom
   - Cliquer sur un auteur pour voir sa biographie et ses livres

4. **Emprunts** (`/loan/`)
   - Voir les emprunts actifs
   - Consulter les emprunts en retard
   - Accéder à l'historique complet

#### En tant qu'administrateur

1. **Connexion** : Allez sur `/admin/` et connectez-vous

2. **Ajouter un livre** :
   - Cliquez sur "Livres" → "Ajouter"
   - Remplissez les informations obligatoires (titre, ISBN, auteur, catégorie, année)
   - Définissez le nombre d'exemplaires
   - Sauvegardez

3. **Ajouter un auteur** :
   - Cliquez sur "Auteurs" → "Ajouter"
   - Entrez prénom, nom, date de naissance, nationalité
   - Ajoutez une biographie (optionnel)
   - Sauvegardez

4. **Créer un emprunt** :
   - Depuis `/loan/create/`
   - Sélectionnez un livre disponible
   - Entrez les informations de l'emprunteur
   - La date de retour est automatiquement fixée à +14 jours
   - Validez

5. **Retourner un livre** :
   - Allez sur `/loan/`
   - Cliquez sur "Retourner" pour l'emprunt concerné
   - Confirmez le retour
   - Le stock est automatiquement mis à jour

---

## 🗂️ Structure du Projet

```
Python avancée/
├── core/                          # Configuration Django
│   ├── settings.py               # Paramètres principaux
│   ├── settings_local.py         # Paramètres sensibles (non versionné)
│   └── urls.py                   # URLs principales
│
├── book/                         # Application Livres
│   ├── models/
│   │   ├── book.py              # Modèle Book
│   │   ├── category.py          # Modèle Category
│   │   └── loan.py              # Modèle Loan
│   ├── admin.py                 # Configuration admin
│   ├── views.py                 # Vues livres
│   ├── loan_views.py            # Vues emprunts
│   ├── static_views.py          # Vues pages statiques
│   ├── forms.py                 # Formulaires
│   ├── urls.py                  # URLs livres
│   ├── loan_urls.py             # URLs emprunts
│   ├── static_urls.py           # URLs pages statiques
│   └── templates/
│       ├── base.html            # Template de base
│       ├── index.html           # Liste des livres
│       ├── details.html         # Détails d'un livre
│       ├── loan/                # Templates emprunts
│       └── static/              # Pages statiques
│
├── author/                       # Application Auteurs
│   ├── models.py                # Modèle Author
│   ├── admin.py                 # Configuration admin
│   ├── views.py                 # Vues auteurs
│   ├── urls.py                  # URLs auteurs
│   └── templates/author/
│       ├── index.html           # Liste des auteurs
│       └── author_detail.html   # Détails d'un auteur
│
└── static/                       # Fichiers statiques
    └── css/
        └── style.css            # Styles CSS (backup)
```

---

## 🎨 Technologies Utilisées

- **Backend** : Django 6.0
- **Frontend** : Tailwind CSS (via CDN)
- **Base de données** : SQLite (par défaut, configurable pour PostgreSQL/MySQL)
- **Gestion d'images** : Pillow

---

## ⚙️ Configuration

### Fichier `settings_local.py`

Le fichier `core/settings_local.py` contient les configurations sensibles :

- `SECRET_KEY` : Clé secrète Django
- `DEBUG` : Mode debug (True en développement, False en production)
- `ALLOWED_HOSTS` : Hôtes autorisés
- `DATABASES` : Configuration de la base de données

**Important** : Ce fichier n'est pas versionné pour des raisons de sécurité. Utilisez `settings_local.py.example` comme template.

### Génération d'une nouvelle SECRET_KEY

```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

---

## 📊 Modèles de Données

### Book (Livre)
- **Champs principaux** : title, isbn, publication_year, author, category
- **Gestion stock** : total_copies, available_copies
- **Métadonnées** : description, language, pages, publisher, cover_image

### Author (Auteur)
- **Informations** : first_name, last_name, birth_date, death_date, nationality
- **Contenu** : biography, website, photo
- **Propriété** : `name` (nom complet calculé)

### Loan (Emprunt)
- **Relations** : book, borrower_name, borrower_email, library_card_number
- **Dates** : loan_date, due_date, return_date
- **Statut** : active, returned, overdue
- **Commentaires** : librarian_comments

### Category (Catégorie)
- **Champs** : name, description, image

---

## 🔒 Sécurité

- **Validation des formulaires** : Vérification des données côté serveur
- **Protection CSRF** : Activée sur tous les formulaires
- **Gestion des permissions** : Interface admin protégée par authentification
- **Configuration sensible** : Séparée dans `settings_local.py` (non versionné)

---

## 🐛 Dépannage

### Erreur "settings_local.py is missing"
Copiez `settings_local.py.example` vers `settings_local.py` :
```bash
cp core/settings_local.py.example core/settings_local.py
```

### Erreur de migration
Supprimez la base de données et recréez-la :
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Images non affichées
Vérifiez que le dossier `media/` existe et est accessible en mode DEBUG.

---

## 📝 Licence

Projet éducatif - Formation Django

---

## 👥 Auteur

Projet réalisé dans le cadre du TP Django - Système de Gestion de Bibliothèque

---

## 🎯 Améliorations Futures

- [ ] Système d'authentification utilisateurs
- [ ] Notifications par email pour les retards
- [ ] Statistiques avancées avec graphiques
- [ ] API REST
- [ ] Export des données (CSV, PDF)
- [ ] Système de réservation
- [ ] Notes et avis sur les livres

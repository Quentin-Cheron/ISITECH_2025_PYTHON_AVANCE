from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Book, Category
from author.models import Author


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    
    # Récupérer les paramètres de recherche depuis l'URL
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    author_id = request.GET.get('author', '')
    
    # Filtrer si une recherche est active
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__first_name__icontains=search_query) |
            Q(author__last_name__icontains=search_query) |
            Q(isbn__icontains=search_query)
        )
    
    # Filtrer par catégorie si sélectionnée
    if category_id:
        books = books.filter(category_id=category_id)
    
    # Filtrer par auteur si sélectionné
    if author_id:
        books = books.filter(author_id=author_id)
    
    return render(request, "index.html", {
        "books": books,
        "categories": categories,
        "authors": authors
    })


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "details.html", {"book": book})


def search(request):
    return render(request, "book/search.html")

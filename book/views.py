from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Book


def index(request):
    books = Book.objects.all()

    # Récupérer le paramètre de recherche depuis l'URL
    search_query = request.GET.get("search")

    # Filtrer si une recherche est active
    if search_query:
        books = books.filter(Q(title__icontains=search_query))

    return render(request, "index.html", {"books": books})


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "details.html", {"book": book})


def search(request):
    return render(request, "book/search.html")

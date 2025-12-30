from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from author.models import Author

from .models import Book, Category


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()

    # Récupérer les paramètres de recherche depuis l'URL
    search_query = request.GET.get("search", "")
    category_id = request.GET.get("category", "")
    author_id = request.GET.get("author", "")

    # Filtrer si une recherche est active
    if search_query:
        books = books.filter(Q(title__icontains=search_query))

    # Filtrer par catégorie si sélectionnée
    if category_id:
        books = books.filter(category_id=category_id)

    # Filtrer par auteur si sélectionné
    if author_id:
        books = books.filter(author_id=author_id)

    # Pagination - 10 livres par page
    paginator = Paginator(books, 2)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "index.html",
        {
            "page_obj": page_obj,
            "books": page_obj,
            "categories": categories,
            "authors": authors,
        },
    )


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "details.html", {"book": book})


def search(request):
    return render(request, "book/search.html")

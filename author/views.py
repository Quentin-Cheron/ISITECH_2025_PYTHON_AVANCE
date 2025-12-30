from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Author


def author_list(request):
    authors = Author.objects.all()

    # Récupérer le paramètre de recherche
    search_query = request.GET.get("search", "")

    # Filtrer par nom ou prénom
    if search_query:
        authors = authors.filter(
            Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
        )

    # Pagination - 10 auteurs par page
    paginator = Paginator(authors, 10)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "author/index.html",
        {
            "page_obj": page_obj,
            "authors": page_obj,
        },
    )


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()  # Tous les livres de cet auteur

    return render(
        request,
        "author/author_detail.html",
        {
            "author": author,
            "books": books,
        },
    )

from django.contrib import admin

from book.models import Book

from .models import Author


class BookInline(admin.TabularInline):
    """Affiche les livres de l'auteur dans l'interface d'édition"""

    model = Book
    extra = 0  # Pas de ligne vide par défaut
    can_delete = False  # Empêche la suppression depuis ici

    fields = (
        "title",
        "isbn",
        "category",
        "publication_year",
        "available_copies",
        "total_copies",
    )
    readonly_fields = (
        "title",
        "isbn",
        "category",
        "publication_year",
        "available_copies",
        "total_copies",
    )

    verbose_name = "Livre de l'auteur"
    verbose_name_plural = "Livres de l'auteur"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("get_full_name", "nationality", "birth_date")

    list_filter = ("nationality",)

    search_fields = ("last_name", "first_name")

    # Inlines pour visualiser les livres de l'auteur
    inlines = [BookInline]

    def get_full_name(self, obj):
        """Affiche le nom complet de l'auteur"""
        return (
            f"{obj.first_name} {obj.last_name}"
            if obj.first_name and obj.last_name
            else "-"
        )

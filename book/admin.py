from django import forms
from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .models import Book, Category, Loan


# ========================================
# Formulaire personnalisé pour Book
# ========================================
class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        available_copies = cleaned_data.get("available_copies")
        total_copies = cleaned_data.get("total_copies")

        if available_copies is not None and total_copies is not None:
            if available_copies > total_copies:
                raise ValidationError(
                    _(
                        "Le nombre d'exemplaires disponibles (%(avail)s) ne peut pas dépasser le nombre total (%(total)s)."
                    ),
                    code="available_gt_total",
                    params={"avail": available_copies, "total": total_copies},
                )

        return cleaned_data


# ========================================
# Inline pour afficher les emprunts actifs
# ========================================
class ActiveLoanInline(admin.TabularInline):
    """Affiche les emprunts actifs pour un livre"""

    model = Loan
    extra = 0
    can_delete = False
    fields = ("borrower_name", "borrower_email", "loan_date", "due_date", "status")
    readonly_fields = (
        "borrower_name",
        "borrower_email",
        "loan_date",
        "due_date",
        "status",
    )

    def get_queryset(self, request):
        """N'affiche que les emprunts actifs ou en retard"""
        qs = super().get_queryset(request)
        return qs.filter(Q(status="active") | Q(status="overdue"))

    verbose_name = "Emprunt actif"
    verbose_name_plural = "Emprunts actifs"


# ========================================
# Admin pour Book
# ========================================
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Utiliser le formulaire personnalisé
    form = BookAdminForm

    # Affichage en liste : titre, auteur, ISBN, catégorie, exemplaires disponibles
    list_display = (
        "title",
        "author",
        "isbn",
        "category",
        "available_copies",
    )

    # Filtres latéraux par catégorie, auteur, année
    list_filter = (
        "category",
        "author",
        "publication_year",
    )

    # Barre de recherche sur titre, ISBN, auteur
    search_fields = (
        "title",
        "isbn",
        "author__name",
    )

    # Configuration des champs en lecture seule
    readonly_fields = ("added_date",)

    # Inlines pour visualiser les emprunts actifs
    inlines = [ActiveLoanInline]

    # Actions personnalisées pour marquer des livres comme indisponibles
    actions = ["mark_as_unavailable"]

    # Pagination
    list_per_page = 25

    # Tri par défaut
    ordering = ("title",)

    # ========================================
    # Actions personnalisées
    # ========================================

    @admin.action(description="Marquer comme indisponible")
    def mark_as_unavailable(self, request, queryset):
        """Marque les livres sélectionnés comme indisponibles"""
        updated = queryset.update(available_copies=0)
        self.message_user(
            request,
            f"{updated} livre(s) marqué(s) comme indisponible(s).",
            level=messages.SUCCESS,
        )

    # ========================================
    # Messages de confirmation personnalisés
    # ========================================

    def save_model(self, request, obj, form, change):
        """Messages de confirmation après sauvegarde"""
        super().save_model(request, obj, form, change)

        # Message de confirmation personnalisé
        if change:
            messages.success(
                request, f'Le livre "{obj.title}" a été modifié avec succès.'
            )
        else:
            messages.success(
                request, f'Le livre "{obj.title}" a été ajouté avec succès.'
            )


# ========================================
# Admin pour Category
# ========================================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Configuration simple avec recherche
    list_display = ("name", "get_books_count")
    search_fields = ("name", "description")
    list_per_page = 25

    # ========================================
    # Comptage du nombre de livres par catégorie
    # ========================================

    @admin.display(description="Nombre de livres")
    def get_books_count(self, obj):
        """Compte le nombre de livres dans cette catégorie"""
        if obj.pk:
            return obj.books.count()
        return 0


# ========================================
# Admin pour Loan
# ========================================
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "borrower_name", "loan_date", "due_date", "status")
    list_per_page = 25


# ========================================
# Personnalisation du titre et header de l'admin
# ========================================
admin.site.site_header = "Administration de la Bibliothèque"
admin.site.site_title = "Bibliothèque Admin"
admin.site.index_title = "Bienvenue dans l'administration de la bibliothèque"

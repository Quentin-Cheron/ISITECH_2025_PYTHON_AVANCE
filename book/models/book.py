from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    isbn = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="ISBN-13",
        help_text="Code ISBN au format ISBN-13 (13 caractères)",
    )
    publication_year = models.IntegerField(
        verbose_name="Année de publication",
        validators=[MinValueValidator(1450), MaxValueValidator(2100)],
    )

    author = models.ForeignKey(
        "author.Author",
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Auteur",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
        verbose_name="Catégorie",
    )

    total_copies = models.PositiveIntegerField(
        verbose_name="Nombre total d'exemplaires"
    )
    available_copies = models.PositiveIntegerField(
        verbose_name="Exemplaires disponibles"
    )

    description = models.TextField(blank=True, verbose_name="Description")
    language = models.CharField(
        max_length=50, default="Français", verbose_name="Langue"
    )
    pages = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Nombre de pages"
    )

    publisher = models.CharField(
        max_length=200, blank=True, verbose_name="Maison d'édition"
    )

    cover_image = models.ImageField(
        upload_to="book_covers/",
        null=True,
        blank=True,
        verbose_name="Image de couverture",
    )

    added_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'ajout au catalogue"
    )

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        ordering = ["title"]

    def __str__(self) -> str:
        return str(self.title)

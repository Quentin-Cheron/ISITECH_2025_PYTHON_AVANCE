from django.db import models

from book.models import Book


class Loan(models.Model):
    LOAN_STATUS_CHOICES = [
        ("active", "Actif"),
        ("returned", "Retourné"),
        ("overdue", "En retard"),
    ]

    book = models.ForeignKey(
        "Book", on_delete=models.PROTECT, related_name="loans", verbose_name="Livre"
    )

    borrower_name = models.CharField(
        max_length=255, verbose_name="Nom complet de l'emprunteur"
    )
    borrower_email = models.EmailField(verbose_name="Email de contact")
    library_card_number = models.CharField(
        max_length=50, verbose_name="Numéro de carte de bibliothèque"
    )

    loan_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Date et heure de l'emprunt"
    )
    due_date = models.DateField(verbose_name="Date limite de retour")
    return_date = models.DateTimeField(
        null=True, blank=True, verbose_name="Date et heure de retour effectif"
    )

    status = models.CharField(
        max_length=20,
        choices=LOAN_STATUS_CHOICES,
        default="active",
        verbose_name="Statut de l'emprunt",
    )
    librarian_comments = models.TextField(
        blank=True, verbose_name="Commentaires du bibliothécaire"
    )

    class Meta:
        verbose_name = "Emprunt"
        verbose_name_plural = "Emprunts"
        ordering = ["-loan_date"]

    def __str__(self) -> str:
        return f"{self.borrower_name} - {str(Book.title)} ({self.status})"

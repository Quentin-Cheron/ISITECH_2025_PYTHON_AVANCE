from django.core.exceptions import ValidationError
from django.db import models


class Author(models.Model):
    """Représente un écrivain ou contributeur"""

    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom de famille")
    birth_date = models.DateField(verbose_name="Date de naissance")
    death_date = models.DateField(null=True, blank=True, verbose_name="Date de décès")
    nationality = models.CharField(max_length=100, verbose_name="Nationalité")
    biography = models.TextField(blank=True, verbose_name="Biographie")
    website = models.URLField(blank=True, verbose_name="Site web ou URL de référence")
    photo = models.ImageField(
        upload_to="author_photos/",
        null=True,
        blank=True,
        verbose_name="Photo de l'auteur",
    )

    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        ordering = ["last_name", "first_name"]
        unique_together = ["first_name", "last_name"]

    def __str__(self):
        return self.name

    def clean(self):
        """Validation des contraintes métier"""
        super().clean()

        if self.death_date and self.birth_date > self.death_date:
            raise ValidationError(
                "La date de décès doit être après la date de naissance."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def name(self):
        """Retourne le nom complet de l'auteur"""
        return f"{self.first_name} {self.last_name}"

    def is_deceased(self):
        """Vérifie si l'auteur est décédé"""
        return self.death_date is not None

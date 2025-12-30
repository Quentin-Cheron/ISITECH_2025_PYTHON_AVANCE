from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200, unique=True, verbose_name="Nom de la catégorie"
    )
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(
        upload_to="category_images/",
        null=True,
        blank=True,
        verbose_name="Image représentative",
    )

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

from django.db import models


class Company(models.Model):
    # implizit wird ein id-Feld erstellt, autoincrement primary key
    name = models.CharField(max_length=100)  # Varchar 100

    # null=True => darf in der DB NULL sein (d.h. optionales Feld)
    # blank=True => darf im HTML-Formular leer sein (opitional)
    description = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        """<Company: Tigersoft>"""
        return self.name

# D
# Aufgabe: makemigrations und migrate ausführen (5 minuten zeit)

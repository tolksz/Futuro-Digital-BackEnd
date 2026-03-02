from django.db import models

class Marca(models.TextChoices):
    PORSCHE = 'Porsche', 'Porsche'
    FERRARI = 'Ferrari', 'Ferrari'
    FORD = 'Ford', 'Ford'
    LAMBORGHINI = 'Lamborghini', 'Lamborghini'
    TESLA = 'Tesla', 'Tesla'
    BUGATTI = 'Bugatti', 'Bugatti'
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class AbstractRateableModel(models.Model):
    class Meta:
        abstract = True

    class Rating(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

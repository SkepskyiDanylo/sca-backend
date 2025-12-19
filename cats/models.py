from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from base import BaseModel


class Cat(BaseModel):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(20)
        ]
    )
    breed = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100_000),
            MinValueValidator(1_000),
        ]
    )

    class Meta:
        verbose_name_plural = "Cats"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}| {self.breed} ({self.years_of_experience})"
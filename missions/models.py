from django.db import models

from base import BaseModel


class Target(BaseModel):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    mission = models.ForeignKey("Mission", on_delete=models.CASCADE, related_name="targets")
    complete_state = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "targets"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} | {self.country} ({self.complete_state})"


class Mission(BaseModel):
    cat = models.ForeignKey("cats.Cat", on_delete=models.SET_NULL, null=True, blank=True)
    complete_state = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "missions"

    def __str__(self):
        return f"{self.cat} Mission | {self.complete_state}"

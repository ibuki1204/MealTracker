from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Create your models here.

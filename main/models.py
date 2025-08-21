from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    calories = models.FloatField(default=0)
    protein = models.FloatField(default=0)  # タンパク質
    fat = models.FloatField(default=0)      # 脂質
    carbs = models.FloatField(default=0)    # 炭水化物

    def __str__(self):
        return self.name


# Create your models here.

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum, Max, Count


class Product(models.Model):
  manufacturer = models.CharField(max_length=50, default=False)
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  group = models.CharField(max_length=50)
  risk = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

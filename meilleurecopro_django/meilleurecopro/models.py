from django.db import models

# Create your models here.
class Estate(models.Model):
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    dept_code = models.CharField(max_length=200)
    condominium_expenses = models.FloatField(default=0)
    ad_url = models.CharField(max_length=200)

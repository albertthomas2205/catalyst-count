from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255, null=True, blank=True) 
    year_founded = models.IntegerField(null=True, blank=True)  # Allow null values
    industry = models.CharField(max_length=255, null=True, blank=True)
    size_range = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)  # Allow null values
    country = models.CharField(max_length=255, null=True, blank=True)  # Allow null values
    linkedin_url = models.URLField(max_length=2000, null=True, blank=True)
    current_employee_estimate = models.IntegerField(null=True, blank=True)  # Allow null values
    total_employee_estimate = models.IntegerField(null=True, blank=True)  

    def __str__(self):
        return self.name
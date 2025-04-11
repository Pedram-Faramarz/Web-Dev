from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.IntegerField()
    company = models.ForeignKey(Company,related_name = "vacancies", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.company}"
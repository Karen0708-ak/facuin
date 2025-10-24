from django.db import models

# Create your models here.
class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=100)
    dean_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    year_foundation = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name} ({self.acronym})"
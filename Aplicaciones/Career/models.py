from django.db import models
from Aplicaciones.Faculty.models import Faculty

# Create your models here.
class Career(models.Model):
    id_career = models.AutoField(primary_key=True)
    career_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=20, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, db_column='id_fac')
    career_code = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    modality = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id_career} - {self.career_name}"
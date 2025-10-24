from django.db import models
from Aplicaciones.Career.models import Career  

class Teacher(models.Model):
    professor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    career = models.ForeignKey(
        Career,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        db_column='id_career'
    )
    specialty = models.CharField(max_length=100, null=True, blank=True)
    academic_degree = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'professor'  

    def __str__(self):
        return f"{self.professor_id} - {self.first_name} {self.last_name}"

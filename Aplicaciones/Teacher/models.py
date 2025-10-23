from django.db import models

# Create your models here.

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='teachers/', null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.id_number}"

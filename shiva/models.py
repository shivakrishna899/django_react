from django.db import models

# Create your models here.
class Shiva(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    
    def __str__(self):
        return f"{self.name}-{self.age} years old"
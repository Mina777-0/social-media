from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    first_name= models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, null=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Face(models.Model):
    image = models.ImageField(null= False, blank= False, upload_to="images/")

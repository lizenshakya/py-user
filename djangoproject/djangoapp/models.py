from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'custom_table_name'
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

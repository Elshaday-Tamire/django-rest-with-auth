from django.db import models

# Create your models here.
class EqubType(models.Model):
    equb_Type_name=models.CharField(max_length=100,unique=True)
class Equb(models.Model):
    equb_name=models.CharField(max_length=100,unique=True)
    equb_type=models.ForeignKey(EqubType,on_delete=models.CASCADE)

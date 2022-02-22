from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
# custom user settings

class Cause(models.Model):   # It acts  like a category eg Orphans, Children and youth
    cause_name  = models.CharField(max_length=256)
    cause_slug  = models.SlugField(max_length=256)

class Charity(models.Model):
    owner       = models.ForeignKey(CustomUser,on_delete=models.CASCADE)  
    cause_name  = models.ForeignKey(Cause,on_delete=models.CASCADE)
    charity_name = models.CharField(max_length=256)
    description  = models.TextField()

class  Quick_Fundriser(models.Model):   # For quick fundraisers
    cause_name            = models.CharField(max_length=256)
    quick_fundriser_name = models.CharField(max_length=256)
    user                  = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Portifolio(models.Model):
    user         = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    cause_name   = models.ForeignKey (Cause,on_delete=models.CASCADE)
    charity_name = models.ForeignKey (Charity,on_delete=models.CASCADE)

class Payment(models.Model):
    charity_name           = models.ForeignKey (Charity,on_delete=models.CASCADE)
    quick_fundriser_name   = models.ForeignKey (Quick_Fundriser,on_delete=models.CASCADE)
    user                   = models.ForeignKey(CustomUser,on_delete=models.CASCADE)


"""
home
signup
signin
logout
charitiy_creattion
fundriser creation
"""



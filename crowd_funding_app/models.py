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

class  Quick_Fundariser(models.Model):   # For quick fundraisers
    cause_name            = models.CharField(max_length=256)
    quick_fundariser_name = models.CharField(max_length=256)
    user                  = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Portifolio(models.Model):
    user         = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    cause_name   = models.ForeignKey (Cause,on_delete=models.CASCADE)
    charity_name = models.ForeignKey (Charity,on_delete=models.CASCADE)

class Payment(models.Model):
    charity_name           = models.ForeignKey (Charity,on_delete=models.CASCADE)
    quick_fundariser_name  = models.ForeignKey (Quick_Fundariser,on_delete=models.CASCADE)
    user         = models.ForeignKey(CustomUser,on_delete=models.CASCADE)


# quick_fundariser_name (foreign  key)
# user (foreign  key)






# Charity
# user (foreign_key)
# cause_name (foreign  key)
# charity_name

# user (foreign_key)
# cause_name (foreign  key)
# charity_name

# Quick Fundariser
# cause_name (foreign  key)
# quick_fundariser_name 
# user (foreign_key)



# Portifolio
# charity_name (foreign  key)
# quick_fundariser_name (foreign  key)
# user (foreign  key)

# Payment
# charity_name (foreign  key)
# quick_fundariser_name (foreign  key)
# user (foreign  key)

# Quick FundariserCharity
# user (foreign_key)
# cause_name (foreign  key)
# charity_name

# Quick Fundariser
# cause_name (foreign  key)
# quick_fundariser_name 
# user (foreign_key)



# Portifolio
# charity_name (foreign  key)
# quick_fundariser_name (foreign  key)
# user (foreign  key)

# Payment
# charity_name (foreign  key)
# quick_fundariser_name (foreign  key)
# user (foreign  key)

# cause_name (foreign  key)
# quick_fundariser_name 
# user (foreign_key)



# Portifolio
# charity_name (foreign  key)
# quick_fundariser_name (foreign  key)
# user (foreign  key)

# Payment
# charity_name (foreign  key)
# quick_fundariser_name (foreign  key)
# user (foreign  key)

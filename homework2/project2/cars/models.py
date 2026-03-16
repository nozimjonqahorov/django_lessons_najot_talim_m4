from django.db import models

class Cars(models.Model):
    make = models.CharField(verbose_name="Make", max_length=120)
    brand = models.CharField(verbose_name="Brand", max_length=100)
    country = models.CharField(verbose_name="Davlati", max_length=100)
    year = models.IntegerField(verbose_name="Chiqarilgan yili")
    price = models.DecimalField(verbose_name="Narxi",max_digits=10, decimal_places=2)
    stock  = models.IntegerField(verbose_name="Soni")
    color = models.CharField(verbose_name="Rangi", max_length=100)
    
    
        
    def __str__(self):
        return self.brand
    

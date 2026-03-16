from django.db import models

class Dorilar(models.Model):
    title = models.CharField(verbose_name="Nomi", max_length=120)
    brand = models.CharField(verbose_name="Brand", max_length=100)
    country = models.CharField(verbose_name="Davlati", max_length=100)
    year = models.IntegerField(verbose_name="Chiqarilgan yili")
    price = models.DecimalField(verbose_name="Narxi",max_digits=10, decimal_places=2)
    stock  = models.IntegerField(verbose_name="Soni")
    AGES = (
        ("0+", "0+"),
        ("12+", "12+"),
        ("18+", "18+"),
        )
    age = models.CharField(max_length=20, choices=AGES)

    def __str__(self):
        return self.title
    

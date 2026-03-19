from django.db import models

class Notebooks(models.Model):
    brand = models.CharField(verbose_name="Brendi", max_length=100)
    model_name = models.CharField(verbose_name="Model nomi", max_length=120)
    processor = models.CharField(verbose_name="Protsessori (CPU)", max_length=100)
    ram = models.CharField(verbose_name="Operativ xotira (RAM)", max_length=50)
    storage = models.CharField(verbose_name="Doimiy xotira (SSD/HDD)", max_length=100)
    price = models.DecimalField(verbose_name="Narxi", max_digits=12, decimal_places=2)
    stock = models.IntegerField(verbose_name="Soni (Omborda)")

    def __str__(self):
        return f"{self.brand} {self.model_name}"

    class Meta:
        verbose_name = "Noutbuk"
        verbose_name_plural = "Noutbuklar"
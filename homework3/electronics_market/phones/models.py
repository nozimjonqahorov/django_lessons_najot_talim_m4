from django.db import models

class Phones(models.Model):
    brand = models.CharField(verbose_name="Brendi", max_length=100)
    model_name = models.CharField(verbose_name="Model nomi", max_length=120)
    memory = models.CharField(verbose_name="Xotirasi (RAM/ROM)", max_length=100)
    color = models.CharField(verbose_name="Rangi", max_length=100)
    price = models.DecimalField(verbose_name="Narxi", max_digits=12, decimal_places=2)
    stock = models.IntegerField(verbose_name="Soni (Omborda)")
    description = models.TextField(verbose_name="Qisqacha ma'lumot", blank=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"

    class Meta:
        verbose_name = "Telefon"
        verbose_name_plural = "Telefonlar"
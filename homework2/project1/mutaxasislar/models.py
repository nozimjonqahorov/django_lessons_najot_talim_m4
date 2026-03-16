from django.db import models

class Mutaxasislar(models.Model):
    first_n = models.CharField(verbose_name="Ismi", max_length=120)
    last_n = models.CharField(verbose_name="Familiya", max_length=100)
    age  = models.IntegerField(verbose_name="Yoshi")
    country = models.CharField(verbose_name="Davlati", max_length=100)
    experience = models.IntegerField(verbose_name="Tajriba")
    prof = models.CharField(verbose_name="Sohasi",max_length = 100)
    salary = models.IntegerField(verbose_name="Maoshi")
    

    def __str__(self):
        return f"Ismi: {self.first_n}, tajriba: {self.experience}, sohasi: {self.prof}"
    

from django.db import models

class News(models.Model):
    title = models.CharField(verbose_name="Sarlavha", max_length=120)
    author = models.CharField(verbose_name="Muallif", max_length=100)
    country = models.CharField(verbose_name="Davlati", max_length=100)
    desc = models.TextField(verbose_name="Matni")
    
    
        
    def __str__(self):
        return self.title
    

from django.db import models
from acc.models import User

class Book(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.TextField()
    site_con = models.TextField()
    impo = models.BooleanField(default=False)
    maker = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.site_name
# Create your models here.


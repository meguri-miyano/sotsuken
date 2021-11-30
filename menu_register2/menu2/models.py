from django.db import models

# Create your models here.
class Menudata(models.Model):
  menuname = models.CharField(max_length=100)
  menuingredients = models.CharField(max_length=100)

  def __str__(self):
      return self.menuname

from django.db import models

class Vegie(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.CharField(max_length=500)
    recipe_image = models.ImageField(upload_to="recipe/images/",default="")
    is_active = models.SmallIntegerField(default=1)

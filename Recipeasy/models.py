from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    ingredients = models.ManyToManyField(Ingredient)
    description = models.TextField()
    instructions = models.TextField()
    owner = models.ForeignKey(User, related_name='recipes')
    favorited_by = models.ManyToManyField(User, related_name='favorites')

    def __unicode__(self):
        return self.name

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    ingredients = models.ManyToManyField(Ingredient)
    description = models.TextField(default="No description has been entered yet", null=True)
    instructions = models.TextField(default="No instructions have been entered yet", null=True)
    owner = models.ForeignKey(User, related_name='recipes')

    def __unicode__(self):
        return self.name

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserSignup(models.Model):
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    created_date = datetime.now()

    def __str__(self):
        return self.email


class PubSignup(models.Model):
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    created_date = datetime.now()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.ForeignKey(UserSignup, unique=True)
    full_name = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True)
    books_wrote = models.TextField(null=True)
    journal_wrote = models.TextField(null=True)
    address = models.TextField(max_length=2000, null=True)
    website = models.CharField(max_length=2000, null=True)


    def __str__(self):
        return self.user

    @receiver(post_save, sender=UserSignup)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            # instance.profile.save()

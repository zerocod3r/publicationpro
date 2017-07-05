from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
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


# def update_filename_user(instance, filename):
#     path = 'user/images/'
#     format = instance.user + instance.file_extension
#     return os.path.join(path, format)


class UserProfile(models.Model):
    user = models.OneToOneField(UserSignup, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    photo = models.FileField(upload_to='user/images/', blank=True)
    birth_date = models.DateField(null=True)
    books_wrote = models.TextField(null=True)
    journal_wrote = models.TextField(null=True)
    experience = models.TextField(max_length=2000, null=True)
    address = models.TextField(max_length=2000, null=True)
    phoneno = models.CharField(max_length=12, null=True)

    # def __str__(self):
    #     return self.user

    @receiver(post_save, sender=UserSignup)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            #         instance.profile.save()
            # @receiver(post_save, sender=User)
            # def save_user_profile(sender, instance, **kwargs):
            #     UserProfile.objects.save(user=instance)


# def update_filename_publisher(instance, filename):
#     path = 'publisher/images/'
#     format = instance.user + instance.file_extension
#     return os.path.join(path, format)


class PublisherProfile(models.Model):
    user = models.OneToOneField(PubSignup, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    photo = models.FileField(upload_to='publisher/images/', blank=True)
    cmpny_name = models.CharField(max_length=200, null=True)
    cmpny_website = models.CharField(max_length=2000, null=True)
    cmpny_address = models.TextField(max_length=2000, null=True)
    aboutcmpny = models.TextField(max_length=2000, null=True)
    phoneno = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.user.email
    # def get_absolute_url(self):
    # return reverse('submit', args=([str(self.slug)]))
    # return ('submit', None, {'slug': self.slug})
    # return reverse('submit', kwargs={'slug': self.slug})

    @receiver(post_save, sender=PubSignup)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            PublisherProfile.objects.create(user=instance)
            #         instance.profile.save()
            # @receiver(post_save, sender=User)
            # def save_user_profile(sender, instance, **kwargs):
            #     PublisherProfile.objects.save(user=instance)


class Manuscript(models.Model):
    publisher = models.OneToOneField(PublisherProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    mtitle = models.TextField(max_length=1000, null=True, blank=True)
    mabstract = models.TextField(max_length=2000, null=True, blank=True)
    mdocfile = models.FileField(upload_to='upload/', blank=True)
    status = models.CharField(default="Pending", max_length=12)

    def __str__(self):
        return self.title

    @receiver(post_save, sender=PublisherProfile)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Manuscript.objects.create(publisher=instance)

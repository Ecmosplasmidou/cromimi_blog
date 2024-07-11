from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

# Create your models here.

STATUS = ((0, "DRAFT"), (1, "PUBLISHED"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    
    class Meta:
        ordering = ["-created_on"] # on ordonne les posts par date de création les plus recents au début
    
    def __str__(self):
        return self.title
    
@receiver(pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image: 
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
        else:
            print("L'image n'existe pas")
            

class Publicite(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to="publicites/")
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.titre
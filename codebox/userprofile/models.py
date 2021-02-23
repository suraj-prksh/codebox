from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True,unique=False,null=True)
    phone = models.CharField(max_length=12,blank=True,unique=False,null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)


################################## SIGNALS ################################################

def create_pofile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_pofile,sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()

post_save.connect(update_profile, sender=User)

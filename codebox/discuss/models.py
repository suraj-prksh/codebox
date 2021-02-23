from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField()
    tags = models.CharField(max_length=50,help_text="For exapmle: #python,#django,etc.",blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,max_length=50,on_delete=models.CASCADE)
    text = RichTextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.post)

    def get_success_url(self):
        return reverse('post-detail',kwargs={'pk':self.post.pk})

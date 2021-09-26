from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

<<<<<<< HEAD
    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)
=======
    created_at = models.DateField(auto_now_add=True, null=True)
>>>>>>> 2fe9341110580d82e91025b11ca99860b6875add

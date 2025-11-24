from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class About(models.Model):
    """
    About model stores a single comment entry
    related to auth user model and blog post model.
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()


def __str__(self):
    return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"

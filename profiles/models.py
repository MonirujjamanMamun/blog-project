from django.db import models
from author.models import Author

# Create your models here.


class Profiles(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    author = models.OneToOneField(
        Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

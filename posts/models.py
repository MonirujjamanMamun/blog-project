from django.db import models
from author.models import Author
from categores.models import Categores

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categores = models.ManyToManyField(Categores)

    def __str__(self) -> str:
        return self.title

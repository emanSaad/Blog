from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# Author model, author can write multiple posts
class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}" 


# Post Model to store title and content in DB
 # auto_now_add make the date is saved automatically when creating the object
class Post(models.Model):
    status = (
        ("published", "Published"),
        ("draft", "Draft"))

    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=150)
    publish_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=CASCADE, related_name="posts", blank=True)
    status = models.CharField(choices=status, max_length=20, default="draft", blank=True)

    def __str__(self):
        return f"{self.title}: {self.content}"
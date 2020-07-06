from django.db import models
# Create your models here.
from django.urls import reverse
class Aricle(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
     return reverse("articles:article",kwargs={'slug': self.slug})

    def __str__(self):
     return self.title

    def snippet(self):
     return self.body[:50]
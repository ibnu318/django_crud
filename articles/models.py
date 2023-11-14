from django.conf import settings
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
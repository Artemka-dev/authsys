from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Название поста", max_length=100)
    body = models.TextField("Описание")

    date_pub = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
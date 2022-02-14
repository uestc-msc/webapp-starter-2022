from django.db import models


# Create your models here.
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    image = models.URLField()

    def __str__(self):
        return self.title

from django.db import models

class Text(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return f'{self.pk} | {self.name}'
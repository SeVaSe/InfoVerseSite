from django.db import models


class Command(models.Model):
    command = models.CharField(max_length=10000000)
    descr = models.CharField(max_length=10000000)

    def __str__(self):
        return self.command  # Или какое-то другое представление объекта



from django.db import models

class CommandDescr(models.Model):
    command = models.CharField(max_length=500)
    text_descr = models.TextField(blank=True)
    text_osob1 = models.TextField(blank=True)
    text_osob2 = models.TextField(blank=True)
    text_osob3 = models.TextField(blank=True)


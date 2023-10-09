from django.db import models

class Champion(models.Model):
    name = models.CharField('Champion name', max_length=50)
    difficulty = models.IntegerField('Champion difficulty')
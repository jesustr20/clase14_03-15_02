from django.db import models

# Create your models here.

class Paradigm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='Null')
    languages = models.ManyToManyField(language)

    def __str__(self):
        return self.name
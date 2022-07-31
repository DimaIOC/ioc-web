from django.db import models
from django.shortcuts import reverse
from datetime import datetime
from django.utils.translation import gettext as _

class Questions(models.Model):
    questiontext = models.CharField(max_length=255)
    published = models.DateTimeField(default=datetime.now)
    backgrouncolor = models.CharField(max_length=20, default="5cc7ff")
    answer = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.questiontext}"


class PartnersImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='partners/')
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class News(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='news/',  null=True, blank=True)
    newstext = models.TextField(max_length=10000)
    published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('landing:single_news', kwargs={'pk': self.id})

    def get_clean_date(self):
        clean_date = self.published.strftime("%d.%m.%Y")
        return clean_date

    class Meta:
        ordering = ['-published']


class Documents(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='documents/')
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Statics(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='statics/', null=True, blank=True)
    metric = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title


class TeamMember(models.Model):

    number = models.IntegerField(null=True, blank=True)
    memberfullname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    position = models.CharField(max_length=255)
    stage = models.IntegerField(null=True, blank=True)
    mail = models.EmailField()

    def __str__(self):
        return self.memberfullname

class Report(models.Model):
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class SubtypeReporting(models.Model):
    title = models.CharField(max_length=500,  null=True, blank=True)
    reports = models.ManyToManyField(Report, related_name='reports')

    def __str__(self):
        return self.title


class TypeReporting(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    subtypereport = models.ManyToManyField(SubtypeReporting, related_name='subtypereport')

    def __str__(self):
        return self.title


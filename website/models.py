from django.db import models
from django.utils import timezone


class Solution(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=80)
    Hint = models.CharField(max_length=1000)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Tutorial(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=80)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

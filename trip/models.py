from django.conf import settings
from django.db import models
from django.utils import timezone


class Trip(models.Model):
    country = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    town = models.CharField(max_length=200)
    monuments = models.TextField()
    transport = models.TextField()
    price = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

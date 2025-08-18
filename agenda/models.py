from django.db import models
from django.conf import settings


class Event(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True) # Nom de la personne ou du rendez-vous
    phone_number = models.CharField(max_length=20)  # Numéro de téléphone (format E.164 max 15)
    start = models.DateTimeField()
    end = models.DateTimeField()
    reserved = models.BooleanField(default=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events"
    )

    def __str__(self):
        return f"{self.name} ({self.start.strftime('%Y-%m-%d %H:%M')} - {self.end.strftime('%H:%M')})"

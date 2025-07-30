from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

BLOOD_TYPE_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]
phone_regex = RegexValidator(
    regex=r'^\+213(5|6|7)[0-9]{8}$',
    message="Le numéro doit commencer par +2135, +2136 ou +2137 et contenir 9 chiffres après"
)

class CustomUser(AbstractUser):
    # Champs supplémentaires
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, unique=True)
    birth_date = models.DateField(null=False, blank=False,)
    is_donor = models.BooleanField(default=False)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True)
    wilaya = models.CharField(max_length=200)

    def __str__(self):
        return self.username
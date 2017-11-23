from django.db import models
from django.core.exceptions import ValidationError

class Member(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('regular', 'Regular'),
    )

    """This class represents the Team member model."""
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20, null=False)
    role = models.CharField(max_length=100, null=False, choices=ROLE_CHOICES)

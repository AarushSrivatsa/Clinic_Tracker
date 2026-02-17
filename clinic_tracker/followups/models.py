from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    clinic_code = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE
        )
    def __str__(self):
        return self.user.username

class FollowUp(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("done", "Done"),
    ]
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("hi", "Hindi"),
    ]
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    notes = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    public_token = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.patient_name

class PublicViewLog(models.Model):
    followup = models.ForeignKey(
        FollowUp,
        on_delete=models.CASCADE
    )
    viewed_at = models.DateTimeField(
        auto_now_add=True
    )
    user_agent = models.TextField(
        blank=True
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )
    def __str__(self):
        return f"{self.followup.patient_name} viewed at {self.viewed_at}"

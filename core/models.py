import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Registros com este campo preenchido são considerados excluídos logicamente.",
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()

    @property
    def is_deleted(self):
        return self.deleted_at is not None
    

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"
    
    def __repr__(self):
        return f"{self.email}"

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default = uuid.uuid4, 
    )
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username' ]

    objects = UserManager()

    def __str__(self):
        return f"{self.email} {self.username}"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
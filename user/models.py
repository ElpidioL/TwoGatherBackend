from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import uuid

# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    STATUS = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=64)
    email = models.EmailField('E-mail', max_length=128, unique=True)
    photo = models.TextField('Photo', null=True, blank=True)
    password = models.CharField('Password', max_length=255)
    description = models.TextField('Description', null=True, blank=True)
    status = models.IntegerField('status', choices=STATUS)
    lastActive = models.DateTimeField(null=True, blank=True)
    idRole = models.ForeignKey('user.Role', blank=True, null=True, on_delete=models.SET_NULL)
    isAdmin = models.BooleanField(default=False)
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Users"


class Role(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=128, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Roles"
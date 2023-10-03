from django.db import models
import uuid

# Create your models here.

class User(models.Model):
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
    status = models.CharField('Escritório base', max_length=255, choices=STATUS)
    lastActive = models.DateTimeField()
    idRole = models.ForeignKey('user.Role', blank=True, null=True, on_delete=models.SET_NULL)
    isAdmin = models.BooleanField(default=False)

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
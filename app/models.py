from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Room(models.Model):
    class ViewChoice(models.TextChoices):
        SEA = 'sea'
        MOUNTAIN = 'mountain'
        FOREST = 'forest'
        DESERT = 'desert'

    image = models.ImageField(upload_to='room/%Y/%m/%d')
    image2 = models.ImageField(upload_to='room/%Y/%m/%d')
    image3 = models.ImageField(upload_to='room/%Y/%m/%d')
    booking = models.URLField()
    title = models.CharField(max_length=155)
    text = models.TextField()
    price = models.PositiveIntegerField()
    person = models.PositiveIntegerField(default=1, validators=[
        MaxValueValidator(3)
    ])
    view = models.CharField(max_length=10,
                            choices=ViewChoice.choices,
                            default=ViewChoice.SEA)

    def __str__(self):
        return self.title


class Instagram(models.Model):
    image = models.ImageField(upload_to="instagram/")


class Feedback(models.Model):
    name = models.CharField(null=True, max_length=100)
    email = models.CharField(default='none', null=False, max_length=100)
    subject = models.CharField(null=True, max_length=100)
    feed = models.TextField(null=True)

    def __str__(self):
        return self.email


class Blog(BaseModel):
    image = models.ImageField(upload_to='blog/%Y/%m/%d')
    title = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(to='app.User', on_delete=models.CASCADE, related_name='comments',
                             related_query_name='comments')
    blog = models.ForeignKey(to='app.Blog', on_delete=models.CASCADE, related_name='comments',
                             related_query_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.text


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    phone_validator = RegexValidator(
        regex=r'^\+?\d{1,15}$',
        message="Yaroqsiz telefon raqam !")
    phone_number = models.CharField(max_length=25,
                                    validators=[phone_validator],
                                    null=True,
                                    blank=True,
                                    unique=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

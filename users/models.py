from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from config.settings import (PHONE_NUMBER_DEFAULT_REGION,
                             PHONE_NUMBER_LENGTH,
                             INVITE_CODE_LENGTH)


class User(AbstractUser):
    username = None
    email = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(region=PHONE_NUMBER_DEFAULT_REGION, max_length=PHONE_NUMBER_LENGTH,
                                    validators=[MinLengthValidator(PHONE_NUMBER_LENGTH)], unique=True)
    invite_code = models.CharField(max_length=INVITE_CODE_LENGTH,
                                   validators=[MinLengthValidator(INVITE_CODE_LENGTH)], unique=True)
    invited_code = models.CharField(max_length=INVITE_CODE_LENGTH,
                                    validators=[MinLengthValidator(INVITE_CODE_LENGTH)], null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

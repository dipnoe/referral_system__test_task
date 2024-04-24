from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from config.settings import (PHONE_NUMBER_DEFAULT_REGION,
                             PHONE_NUMBER_LENGTH,
                             INVITE_CODE_LENGTH,
                             AUTH_CODE_LENGTH)


class User(AbstractUser):
    username = None
    email = None
    auth_code = models.CharField(max_length=AUTH_CODE_LENGTH, unique=True, blank=True, null=True,
                                 validators=[MinLengthValidator(AUTH_CODE_LENGTH)])
    phone_number = PhoneNumberField(region=PHONE_NUMBER_DEFAULT_REGION, unique=True)
    personal_invite_code = models.CharField(max_length=INVITE_CODE_LENGTH, null=True, blank=True,
                                            validators=[MinLengthValidator(INVITE_CODE_LENGTH)])
    invited_by_code = models.CharField(max_length=INVITE_CODE_LENGTH, null=True, blank=True,
                                       validators=[MinLengthValidator(INVITE_CODE_LENGTH)])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

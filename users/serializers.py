import phonenumbers
from django.core.validators import MinLengthValidator
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from config.settings import PHONE_NUMBER_LENGTH, AUTH_CODE_LENGTH, PHONE_NUMBER_DEFAULT_REGION
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(region=PHONE_NUMBER_DEFAULT_REGION)

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'personal_invite_code', 'invited_by_code']
        hidden_fields = ['personal_invite_code', 'invited_by_code']


class VerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=PHONE_NUMBER_LENGTH)
    auth_code = serializers.CharField(max_length=AUTH_CODE_LENGTH)

    def validate(self, data):
        phone_number = data['phone_number']
        auth_code = data['auth_code']
        try:
            user = User.objects.get(phone_number=phone_number, auth_code=auth_code)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid phone number or verification code.")
        return user


class UserRetrieveSerializer(serializers.ModelSerializer):
    invited_users = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'personal_invite_code', 'invited_by_code', 'invited_users']
        read_only_fields = ['personal_invite_code', 'invited_users']

    def get_invited_users(self, obj):
        invited_users = User.objects.filter(invited_by_code=obj.personal_invite_code)
        return [str(invited_user.phone_number) for invited_user in invited_users]

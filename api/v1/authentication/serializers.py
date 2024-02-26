from six import text_type
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import F
from django.conf import settings as SETTINGS
from django.utils.translation import ugettext_lazy as _

from posts.models import Post


User = get_user_model()


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)
        return token

    def validate(cls, attrs):
        data = super(UserTokenObtainPairSerializer, cls).validate(attrs)

        refresh = cls.get_token(cls.user)
        data['access'] = text_type(refresh.access_token)
        data['refresh'] = text_type(refresh)
        return data

from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()
    first_name= serializers.CharField(required=False)
    last_name= serializers.CharField(required=False)
    email= serializers.EmailField(required=False)

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")

        try:
            validate_password(password=password)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        username = data.get('username')
        # For case sensitive Username
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("This username is already in use.")

        return data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['creator', 'updater','date_added','date_updated', 'auto_id', 'is_deleted', ]
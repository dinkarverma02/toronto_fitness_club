from rest_framework import serializers
from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2', 'phone_number', 'avatar')

        # don't display password in response
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    # create custom user
    def create(self, validated_data):
        # user = User.objects.create_user(
        #             first_name = validated_data['first_name'],
        #             last_name = validated_data['last_name'],
        #             # etc ...
        #         )
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'token')


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'avatar')

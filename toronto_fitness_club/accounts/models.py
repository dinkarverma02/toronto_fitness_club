from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import jwt


class MyUserManager(UserManager):

    def _create_user(self, first_name, last_name, username, email, password, password2, phone_number, avatar, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not first_name:
            raise ValueError('please provide first_name')

        if not last_name:
            raise ValueError('please provide last_name')

        if not username:
            raise ValueError('please provide username')

        if not email:
            raise ValueError('please provide email')

        if not password:
            raise ValueError('please provide password')

        if not password2:
            raise ValueError('please provide password2')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(first_name=first_name, last_name=last_name, username=username, email=email,
                          password=password, password2=password2, phone_number=phone_number, avatar=avatar)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, username, email, password, password2, phone_number, avatar, **extra_fields):
        # extra_fields.setdefault("is_staff", False)
        # extra_fields.setdefault("is_superuser", False)
        return self._create_user(first_name, last_name, username, email, password, password2, phone_number, avatar, **extra_fields)

    def create_superuser(self, first_name, last_name, username, email, password, password2, phone_number, avatar, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        #
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        user = self._create_user(first_name, last_name, username, email, password, password2, phone_number, avatar, **extra_fields)

        # give access to admin panel
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    first_name = models.CharField(_('first_name'), blank=False, max_length=200)
    last_name = models.CharField(_('last_name'), blank=False, max_length=200)
    username = models.CharField(_('username'), blank=False, max_length=200, unique=True)
    email = models.EmailField(_('email'), blank=False, unique=True)
    password = models.CharField(_("password"), blank=False, max_length=200)
    password2 = models.CharField(_("password2"), default='', blank=False, max_length=200)
    phone_number = models.CharField(_("phone_number"), blank=False, max_length=200)
    avatar = models.ImageField(_("avatar"), upload_to='avatars', blank=False, default='')

    # fields necessary for admin access
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password', 'password2',
                       'phone_number', 'avatar']

    @property
    def token(self):
        return jwt.encode(
            {'first_name': self.first_name, 'last_name': self.last_name, 'username': self.username, 'email': self.email,
             'phone_number': self.phone_number, 'avatar': str(self.avatar)},
            "secret", algorithm="HS256")

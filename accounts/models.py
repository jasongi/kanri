from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class KanriUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password = None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password
        )

        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using = self._db)
        return user


class KanriUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length = 254,
        blank = False,
        unique = True,
    )
    
    first_name = models.CharField(
        max_length = 30,
        blank = False,
    )

    last_name = models.CharField(
        max_length = 30,
        blank = False,
    )

    phone_number = models.CharField(
        max_length = 10,
    )

    is_active = models.BooleanField(
        default = True
    )

    is_staff = models.BooleanField(
        default = False
    )

    objects = KanriUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return "%s %s" % (self.first_name, self.last_name[0])

    def __unicode__(self):
        return self.get_full_name()

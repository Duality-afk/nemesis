from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# Don't forget to register model in admin page

class MyAccountManager(BaseUserManager):
        def create_user(self,email, username, address, password=None,):
                if not email:
                        raise ValueError('Email is require')
                if not username:
                        raise ValueError('Username is required')

                user = self.model(
                        email = self.normalize_email(email),
                        username = username,
                        address=address,
                        
                )
                user.set_password(password)
                user.save(using = self._db)
                return user

        def create_superuser(self,email, username, password):
                user = self.create_user(
                        email = self.normalize_email(email),
                        password = password,
                        username = username,
                )
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save(using = self._db)
                return user



class Account(AbstractBaseUser):
        username = models.CharField(max_length=30, unique=True, null=True)
        email = models.EmailField(unique=True)
        password = models.CharField(max_length=255)
        address = models.CharField(max_length=250, blank=True, null=True)

        last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
        date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
        is_admin = models.BooleanField(default = False)
        is_staff = models.BooleanField(default = False)
        is_active = models.BooleanField(default = True)
        is_superuser = models.BooleanField(default = False)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']
        objects = MyAccountManager()

        def __str__(self):
                return self.email
        
        def has_perm(self,perm, obj = None):
                return self.is_admin
                
        def has_module_perms(self, app_label) :
            return True

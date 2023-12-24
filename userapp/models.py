import uuid
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.utils.translation import gettext_lazy as _

# from product.models import RefferalLink

# Create your models here.

UPGRADATION_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]


class UserManager(BaseUserManager):
    use_in_migration = True
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        return self.create_user(email, password, **extra_fields)
    

class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=_('groups'),
    #     blank=True,
    #     help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
    #     related_name='user_data_groups',  # <-- Change this line
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=_('user permissions'),
    #     blank=True,
    #     help_text=_('Specific permissions for this user.'),
    #     related_name='user_data_user_permissions',  # <-- Change this line
    # )




class UserDetails(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='user_details')
    phone = models.CharField(max_length =15, null = True, blank = True)
    house_number=models.CharField(max_length=50,null = True, blank = True)
    land_mark = models.CharField(max_length=500,null = True, blank = True)
    user_refferal_link = models.URLField(default = '1')


class UserRequestingforUpgradingToOrganiser(models.Model):
    user = models.ForeignKey(UserData, on_delete = models.CASCADE)
    user_refferal_link = models.ForeignKey('product.RefferalLink', on_delete = models.CASCADE, default ='0')
    request_status = models.CharField(max_length= 50, choices=UPGRADATION_STATUS_CHOICES, default='Pending')
    description = models.CharField(max_length =700, null = True, blank = True)


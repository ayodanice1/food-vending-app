from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator

from .managers.userManager import UserManager


phone_regex = RegexValidator(
    regex=r'\d{4}-\d{3}-\d{4}',
    message="Phone number format must look like '0810-566-3990'"
)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=20)
    first_name = models.CharField( max_length=150, blank=True, null=True )
    last_name = models.CharField( max_length=150, blank=True, null=True )
    business_name = models.CharField( max_length=150, blank=True, null=True ) 
    date_joined = models.DateTimeField(auto_now_add=True)
    outstanding = models.DecimalField( max_digits=8, decimal_places=2, default=0.00 )
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    

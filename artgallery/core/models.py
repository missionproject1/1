from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.utils import timezone
from django.core.validators import validate_email
from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


# class ArtistProfile(AbstractUser):
#     bio = models.TextField()
#     groups = models.ManyToManyField(Group, related_name='artist_profiles')
#     user_permissions = models.ManyToManyField(Permission, related_name='artist_profiles')

#     def __str__(self):
#         return self.username

class YourModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission

# class UserProfileManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, username, password, **extra_fields)

# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     id = models.BigAutoField(primary_key=True)
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True)
#     user_type = models.CharField(max_length=10, choices=[('member', 'Member'), ('artist', 'Artist')], default='member')

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     # REQUIRED_FIELDS should include 'username' in addition to 'email'
#     REQUIRED_FIELDS = ['email']
#     USERNAME_FIELD = 'username'

#     objects = UserProfileManager()

#     def __str__(self):
#         return self.username

# class UserProfileGroup(models.Model):
#     user_profile = models.ForeignKey(UserProfile, related_name='user_groups', on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)

# class UserProfilePermission(models.Model):
#     user_profile = models.ForeignKey(UserProfile, related_name='user_profile_permissions', on_delete=models.CASCADE)
#     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
# class Artwork(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='artwork_images/')
#     is_for_sale = models.BooleanField(default=False)
#     price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     is_for_auction = models.BooleanField(default=False)
#     artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class AuctionItem(models.Model):
#     artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='auctions')
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     current_bid = models.DecimalField(max_digits=10, decimal_places=2)
#     current_bid_user = models.ForeignKey(ArtistProfile, on_delete=models.SET_NULL, null=True, blank=True)
    
#     def __str__(self):
#         return f"{self.artwork.title} - {self.current_bid}"

#     @property
#     def is_active(self):
#         return self.end_time > timezone.now()

#     @property
#     def time_remaining(self):
#         return (self.end_time - timezone.now()).total_seconds()

# class UserProfile(models.Model):
    # username = models.CharField(max_length=255, unique=True)
    # email = models.EmailField(unique=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # user_type = models.CharField(max_length=10, choices=[('member', 'Member'), ('artist', 'Artist')], default='member')

    # def __str__(self):
    #     return self.user.username
    
from django.contrib.auth.models import AbstractUser
from django.db import models
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     user_type = models.CharField(max_length=10, choices=[('member', 'Member'), ('artist', 'Artist')], default='member')
#     groups = models.ManyToManyField(Group, related_name='user_profiles_groups')
#     user_permissions = models.ManyToManyField(Permission, related_name='user_profiles_permissions')

#     def __str__(self):
#         return self.user.username
# class UserProfile(models.Model):
#     user_type = models.CharField(max_length=10, choices=[('member', 'Member'), ('artist', 'Artist')], default='member')
#     member_groups = models.ManyToManyField(Group, related_name='member_profiles')
#     member_permissions = models.ManyToManyField(Permission, related_name='member_profiles')

#     def __str__(self):
#         return self.username



# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     is_artist = forms.BooleanField(required=False, initial=False)

#     class Meta:
#         model = UserProfile
#         fields = ['username', 'password', 'email', 'is_artist']

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if UserProfile.objects.filter(email=email).exists():
#             raise ValidationError("This email is already in use.")
#         return email

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.password = make_password(self.cleaned_data['password'])
#         user.is_artist = self.cleaned_data['is_artist']
#         if commit:
#             user.save()
#             UserProfile.objects.create(user=user, username=user.username, password=user.password, email=user.email, user_type=user.is_artist)

#         return user


#neww
    
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
from django import forms
from django.contrib.auth.hashers import make_password

class ArtistProfile(AbstractUser):
    bio = models.TextField()
    groups = models.ManyToManyField(Group, related_name='artist_profiles_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='artist_profiles_permissions')

    def __str__(self):
        return self.username


class Artwork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='artwork_images/')
    is_for_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_for_auction = models.BooleanField(default=False)
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    watchers = models.ManyToManyField(User, related_name="watchlist", blank=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class AuctionItem(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='auctions')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid_user = models.ForeignKey(ArtistProfile, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.artwork.title} - {self.current_bid}"

    @property
    def is_active(self):
        return self.end_time > timezone.now()

    @property
    def time_remaining(self):
        return (self.end_time - timezone.now()).total_seconds()
    

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
        # date_of_birth = models.DateField(_('date of birth'))
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField()
    profile_type = models.CharField(
        _('profile type'),
        max_length=10,
        choices=(
            ('artist', 'Artist'),
            ('member', 'Member'),
        ),
        default='member',
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']


    def __str__(self):
        return f"{self.user.username}'s Profile"

# for user in User.objects.all():
#     UserProfile.objects.get_or_create(user=user)

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def update_artist_status(sender, instance, created, **kwargs):
    """
    Signal handler to automatically update the is_artist field.
    You can define your own logic to determine if a user is an artist or not.
    """
    if created:
        # Newly created user, update the is_artist field based on some criteria.
        # For example, check if the user's email ends with "@artist.com".
        instance.is_artist = instance.email.endswith("@artist.com")
        instance.save()

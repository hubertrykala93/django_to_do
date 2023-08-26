from django.db.models.signals import post_save
from .models import User, Profile
from django.dispatch.dispatcher import receiver


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

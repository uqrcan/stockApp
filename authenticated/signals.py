from django.contrib.auth.models import UserData
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken

@receiver(post_save, sender=UserData)
def create_jwt_token(sender, instance=None, created=False, **kwargs):
    if created:
        refresh = RefreshToken.for_user(instance)
        instance.auth_token = str(refresh.access_token)
        instance.save()

# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from account.models import Profile
#
#
# @receiver(post_save, sender=Profile)
# def create_or_update_user_profile(instance: Profile, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.save()

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import BookMark
# from .parser import parse_and_save
#
#
# @receiver(post_save, sender=BookMark)
# def webpage_post_save(sender, instance, created, **kwargs):
#     if created and instance.Link:
#         parse_and_save(instance.Link)

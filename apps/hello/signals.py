from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.hello.models import Entry


@receiver(post_save)
def model_save_handler(sender, created, **kwargs):
    class_name = sender.__name__
    if class_name == "Entry":
        return
    action = "create" if created else "edit"
    Entry.objects.create(model=class_name, action=action).save()


@receiver(post_delete)
def model_delete_handler(sender, **kwargs):
    class_name = sender.__name__
    Entry.objects.create(model=class_name, action="delete").save()

from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(*, recipient, actor, verb, target):
    """
    recipient: user receiving the notification
    actor: user who did the action
    verb: short text like "liked your post" / "commented on your post" / "started following you"
    target: the object that was acted on (Post, Comment, User, etc.)
    """
    ct = ContentType.objects.get_for_model(target.__class__)
    return Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=ct,
        target_object_id=target.pk,
    )

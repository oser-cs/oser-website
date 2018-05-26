"""Visits app signals."""

from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from .models import Participation
from .notifications import Accepted, Rejected

accepted_changed = Signal()


@receiver(post_save, sender=Participation)
def fire_accepted_changed(sender, instance: Participation, **kwargs):
    """Fire an event if the participation status has changed."""
    if instance.accepted_changed():
        accepted_changed.send(sender=sender, instance=instance)


@receiver(accepted_changed, sender=Participation)
def notify_participation(sender, instance: Participation, **kwargs):
    """Send notification to user depending on their participation status.

    The notification is only sent if the participation status has changed.
    """
    if instance.accepted is True:
        Accepted(user=instance.user, visit=instance.visit).send()
    elif instance.accepted is False:
        Rejected(user=instance.user, visit=instance.visit).send()

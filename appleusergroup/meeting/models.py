from __future__ import unicode_literals

from django.db import models
from django.utils import formats, timezone
from django.utils.translation import ugettext_lazy as _


class MeetingManager(models.Manager):
    def upcoming_meeting(self):
        """
        Returns the next upcoming meeting.

        :return: either the upcoming meeting or None if no meeting was found.
        """
        now = timezone.now()

        try:
            meeting = self.filter(start__gte=now)[0:1].get()
        except Meeting.DoesNotExist:
            meeting = None

        return meeting


class Meeting(models.Model):
    """
    The meeting model represents a single meeting. It contains
    the basic information associated with a meeting.
    """
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.ForeignKey("Location", on_delete=models.PROTECT)

    objects = models.Manager()
    meetings = MeetingManager()

    def __unicode__(self):
        month = self.start.strftime("%B")
        short_datetime = formats.date_format(self.start, 'SHORT_DATETIME_FORMAT')

        return _("Meeting in %(month)s (%(short_datetime)s)") % {'month': month, 'short_datetime': short_datetime}

class Location(models.Model):
    # meta data
    name = models.CharField(max_length=100)

    # address
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="Dresden")
    postcode = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name
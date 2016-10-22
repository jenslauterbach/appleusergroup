from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .models import Meeting


class MeetingTestCase(TestCase):

    def test_upcoming_meeting(self):
        """
        Tests if the correct meeting is found if there are multiple meetings. The meetings are in the past as well
        in the future.
        """
        now = timezone.now()

        # Create meeting 10 days in the past:
        Meeting.objects.create(start=now - timedelta(days=10))

        # Create meeting 10 and 20 days in the future:
        expected = Meeting.objects.create(start=now + timedelta(days=10))
        Meeting.objects.create(start=now + timedelta(days=20))

        actual = Meeting.meetings.upcoming_meeting()
        self.assertIsNotNone(actual, "The found upcoming meeting should not be 'None'!")
        self.assertEqual(expected, actual, "The found upcoming meeting is wrong!")

    def test_upcoming_meeting_with_no_upcoming_meetings(self):
        actual = Meeting.meetings.upcoming_meeting()
        self.assertIsNone(actual, "The upcoming meeting should be 'None'!")

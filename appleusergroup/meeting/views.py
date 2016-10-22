from django.shortcuts import render
from .models import Meeting


def index(request):
    upcoming_meeting = Meeting.meetings.upcoming_meeting()
    context = {'upcoming_meeting': upcoming_meeting}

    return render(request, 'index.html', context)

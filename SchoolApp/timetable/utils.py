from datetime import timedelta

from django.utils import timezone

from timetable.models import ClassTime


def get_class_announcement():
    today = ClassTime.objects.all().filter(day=timezone.now().weekday())

    # get classes that are 5 minutes in future
    time = timezone.now().replace(second=0, microsecond=0) + timedelta(minutes=5)
    return today.filter(time=time)


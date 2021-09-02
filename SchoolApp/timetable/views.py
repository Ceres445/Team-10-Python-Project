from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from timetable.models import ClassTime


@login_required
def view_timetable(request):
    records = ClassTime.objects.all().filter(key_class__in=request.user.profile.courses.all()) | \
              ClassTime.objects.all().filter(key_class__teacher_id=request.user)
    records = [{
        'day': record.get_day_display(),
        'subject': record.subject,
        'time': record.time.strftime('%H:%M'),
        'link': record.link,
    } for record in records]
    return render(request, 'timetable/view_timetable.html', {"records": records})

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from home.models import Classes
from timetable.forms import ClassTimeCreationForm
from timetable.models import ClassTime


@login_required
def view_timetable(request):
    records = ClassTime.objects.all().filter(key_class__in=request.user.profile.courses.all()) | \
              ClassTime.objects.all().filter(key_class__teacher_id=request.user)
    print(ClassTime.objects.all().filter(key_class__in=request.user.profile.courses.all()),ClassTime.objects.all().filter(key_class__teacher_id=request.user),
          ClassTime.objects.all())
    records = [{
        'day': record.get_day_display(),
        'subject': record.subject,
        'time': record.time.strftime('%H:%M'),
        'link': record.link,
    } for record in records]
    return render(request, 'timetable/view_timetable.html', {"records": records})


@login_required()
def create_timetable(request):
    classes = Classes.objects.all().filter(teacher_id=request.user)
    message = ""
    if request.method == "GET":
        form = ClassTimeCreationForm
    elif request.method == "POST":
        form = ClassTimeCreationForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            form.save()
            message = "Success!, created record"
        else:
            print('invalid')
            message = "Error!, unable to create"
    else:
        return HttpResponseForbidden(f"Method {request.method} not allowed")
    return render(request, 'timetable/create.html', {"form": form, "records": classes, "message": message})

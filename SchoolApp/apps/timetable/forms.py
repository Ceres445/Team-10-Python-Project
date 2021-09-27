from django.forms import ModelForm

from apps.timetable.models import ClassTime


class ClassTimeCreationForm(ModelForm):
    class Meta:
        model = ClassTime
        exclude = ['permanent']

from django.forms import ModelForm

from timetable.models import ClassTime


class ClassTimeCreationForm(ModelForm):
    class Meta:
        model = ClassTime
        exclude = ['permanent']

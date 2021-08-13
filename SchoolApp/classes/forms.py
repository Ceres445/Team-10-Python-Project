from django.forms import ModelForm

from classes.models import Assignment, Upload


class AssignmentCreationForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'questions', 'ends_at']


class UploadCreationForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['assignment', 'file']

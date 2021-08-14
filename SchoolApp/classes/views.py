from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from classes.forms import AssignmentCreationForm, UploadCreationForm
from classes.models import Assignment, Upload
from home.models import Classes


@login_required
def assignment_creation(request, pk):
    """Form to create assignment"""
    class_object = get_object_or_404(Classes, id=pk)
    classes_thought = Classes.objects.all().filter(teacher_id=request.user)
    if request.method == 'POST':
        form = AssignmentCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.key_class = class_object
            form.save()
            return redirect(reverse('classesDetail', args=[pk]))
    else:
        form = AssignmentCreationForm()

    return render(request, 'classes/assignment_create.html', {'form': form, 'classes': classes_thought, 'files': True})


@login_required
def classes_view(request):
    joined = request.user.profile.courses.all()  # classes user has joined
    public = Classes.objects.all().filter(public=True).\
        exclude(id__in=[x.id for x in joined]).\
        exclude(teacher_id=request.user)   # public classes user has not joined
    teacher = Classes.objects.all().filter(teacher_id=request.user)  # User teaches these classes
    print([c.assignments.all() for c in teacher])
    return render(request, 'classes/classes_view.html', {'joined': joined, 'public': public, 'teacher': teacher})


def get_status(user):
    def predicate(assignment: Assignment):
        if user in [x.author for x in assignment.upload.all()]:
            return Upload.objects.get(author=user, assignment=assignment)
        else:
            return None
    return predicate


@login_required
def classes_detail(request, pk=1):
    class_object = get_object_or_404(Classes, id=pk)
    if class_object in request.user.profile.courses.all() or class_object.teacher_id == request.user:
        assignments = Assignment.objects.all().filter(key_class=class_object)[::-1]
        submitted = map(get_status(request.user), assignments)
        teacher = class_object.teacher_id == request.user
        return render(request, 'classes/classes_detail.html', {'class': class_object,
                                                               'assignments': tuple(zip(assignments, submitted)),
                                                               'teacher': teacher})
    else:
        raise PermissionDenied("You are not in this class")


@login_required
def assignment_submit(request, pk=1):
    class_object = get_object_or_404(Classes, id=pk)
    if class_object in request.user.profile.courses.all():
        assignments = Assignment.objects.all().filter(key_class=class_object)
        submitted = [x.assignment for x in request.user.uploads.all()]
        assignments = [x for x in assignments if x not in submitted]   # remove submitted assignments from list
        if request.method == 'POST':
            form = UploadCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect(reverse('classesDetail', args=[pk]))
        else:
            form = UploadCreationForm()

        return render(request, 'classes/assignment_submit.html',
                      {'form': form, 'class': class_object, 'assignments': assignments, 'files': True})
    else:
        raise PermissionDenied("You are not in this class")


@login_required
def view_submissions(request, pk):

    assignment = get_object_or_404(Assignment, pk=pk)
    if assignment.key_class.teacher_id == request.user:
        uploads = Upload.objects.all().filter(assignment=assignment)[::-1]
        return render(request, 'classes/view_submissions.html', {'uploads': uploads})
    else:
        raise PermissionDenied("Only the teacher can see uploads")
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404

from public_api.models import Category


def filter_queryset(user, model, strategy, **kwargs):
    if user.is_staff:
        return model.objects.all()  # return all objects
    elif user.is_authenticated:
        return strategy['authenticated'](user, model, **kwargs)
    else:
        return strategy['anon'](user, model, **kwargs)


def authenticated_home(user, model, **kwargs):
    return model.objects.all().exclude(**{kwargs.get('name'): 'Class'}) | \
           model.objects.all().filter(
               **{kwargs.get('class_in'): user.profile.courses.all(),  # include classes in which user is in
                  kwargs.get('name'): 'Class'})  # return class objects for user


def anon_home(user, model, **kwargs):
    return model.objects.all().exclude(**{kwargs.get('name'): 'Class'})


def authenticated_classes(user, model, **kwarg):
    return model.objects.all().filter(**{kwarg['courses']: user.profile.courses}) | \
           model.objects.all().filter(**{kwarg['teacher']: user})


def anon_classes(*args, **kwargs):
    raise PermissionDenied("Non authenticated users cannot see assignments")


def parse_args(queryset, user, model, category_param=None, user_param=None, **kwargs):
    if model is not Category:
        if category_param in ['Class', 'Public', 'Forum', 'Site']:
            # print([(x.category.name == category, list(x.category.name)) for x in queryset], list(category))
            queryset = queryset.filter(
                **{kwargs.get('name'): category_param.strip("'")})  # filter against given category
            # print(queryset)
            if category_param == 'Class':
                if user.is_authenticated:
                    if not user.is_staff:
                        queryset = queryset.filter(**{kwargs.get('class_in'): user.profile.courses.all()})
                else:
                    raise PermissionDenied("Non authenticated users cannot see classes")
        elif category_param is not None:
            raise Http404
    if user_param is not None:
        get_object_or_404(User, username=user_param)  # raise error if author not found
        # print('filtering', user)
        queryset = queryset.filter(author__username=user_param)
    return queryset
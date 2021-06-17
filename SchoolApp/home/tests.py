from django.test import TestCase

# Create your tests here.
from django.contrib.staticfiles import finders

result = finders.find('registration/login.css')
searched_locations = finders.searched_locations

print(result, searched_locations)

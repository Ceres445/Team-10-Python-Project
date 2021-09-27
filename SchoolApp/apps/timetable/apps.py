from django.apps import AppConfig


class TimetableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.timetable'

    # def ready(self):
    #     # start APS background task
    #     from apps.timetable.announcer import start
    #     start()

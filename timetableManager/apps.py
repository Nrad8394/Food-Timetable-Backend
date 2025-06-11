from django.apps import AppConfig


class TimetablemanagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'timetableManager'
    
    def ready(self):
        # Import the tasks module to ensure tasks are registered
        from . import tasks
        
        from django_celery_beat.models import PeriodicTask, IntervalSchedule,CrontabSchedule
        from django.core.exceptions import ImproperlyConfigured
        
        # create a 1 minute interval schedule
        one_minute_schedule = None
        try:
            one_minute_schedule, created = IntervalSchedule.objects.get_or_create(
                every=1,
                period=IntervalSchedule.MINUTES,
            )
        except ImproperlyConfigured:
            pass
            
        # create a crontab schedule to run every minute
        every_minute_crontab_schedule = None
        try:
            every_minute_crontab_schedule, created = CrontabSchedule.objects.get_or_create(
                minute='*',
                hour='*',
                day_of_week='*',
                day_of_month='*',
                month_of_year='*',
            )
        except ImproperlyConfigured:
            crontab_schedule = None
        # create a periodic task to run the print_timetable task every minute
        try:
            if one_minute_schedule:
                PeriodicTask.objects.get_or_create(
                    interval=one_minute_schedule,
                    name='Print Timetable Every Minute',
                    task='timetableManager.tasks.print_timetable',
                )
        except ImproperlyConfigured:
            periodic_task = None
            periodic_task = None
            
        # create a periodic task to run the print_timetable task every minute using crontab
        try:
            if every_minute_crontab_schedule:
                PeriodicTask.objects.get_or_create(
                    crontab=every_minute_crontab_schedule,
                    name='Print Timetable Every Minute (Crontab)',
                    task='timetableManager.tasks.print_timetable',
                )
        except ImproperlyConfigured:
            periodic_task = None
        

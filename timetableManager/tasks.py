from celery import shared_task
from timetableManager.models import Timetable
        
# task to print timetable for all days
# @shared_task
# def print_timetable():
#     """
#     Task to print all timetables.
#     """
#     timetables = Timetable.objects.all()
    
#     if not timetables:
#         print("No timetable found.")
#         return
    
#     for timetable in timetables:
#         print(f"Timetable")
#         print(f"- {timetable.meals.name} on {timetable.day_of_week} for {timetable.meal_type}")
        
# task to print a timetable for the entire week
@shared_task
def print_timetable():
    """
    Task to print the weekly timetable.
    """
    timetables = Timetable.objects.all()
    
    if not timetables:
        print("No timetable found.")
        return
    
    print("Weekly Timetable:")
    for timetable in timetables:
        print(f"{timetable.day_of_week}: {timetable.meals.name} for {timetable.meal_type}")
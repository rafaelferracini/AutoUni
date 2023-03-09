"""
    Check events in google calendar
"""
from gcsa.google_calendar import GoogleCalendar
import datetime as dt

gc = GoogleCalendar()

events_str = []

start = dt.date.today()
events = gc.get_events(start, start)
for event in events:
    events_str.append(str(event))

current_hour = dt.datetime.now()
event_hour = events_str[]
print(current_hour)
print(type(current_hour))

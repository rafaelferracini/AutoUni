import os.path
import datetime

from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

def main():
    credentials_file = '~/.credentials/credentials.json'

    calendar_id = 'Rafael Haas Ferracini'

    credentials = service_account.Credentials.from_service_account_file(
            credentials_file,
            scopes = ['https://www.googleapis.com/auth/calendar']
            )

    service = build('calendar', 'v3', credentials=credentials)

    while True:
        events_result = service.events().list(calendarId=calendar_id, timeMin=current_time.isoformat(), timeMax=(current_time + datetime.timedelta(hours=1)).isoformat(), singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])




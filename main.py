import datetime
import pickle
import os.path
import pyttsx3

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

engine = pyttsx3.init()
kids_calendar_id = "c_qlq7pm7bim7a8f2lo0njhlleo0@group.calendar.google.com"
seconds_in_day = 24 * 60 * 60
seconds_in_minute = 60


def main():
    setup_voice()

    credentials = login_if_needed()
    service = build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'

    event_results = service.events().list(calendarId=kids_calendar_id, timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = event_results.get('items', [])

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_date = datetime.datetime.fromisoformat(start)

        if is_event_soon(start_date):
            start_time = start_date.strftime("%I:%M %p")
            speak("Next event: " + event['summary'] + " at " + start_time)
            return


def setup_voice():
    voices = engine.getProperty('voices')

    for voice in voices:
        if voice.name == "Daniel":
            engine.setProperty('voice', voice.id)


def login_if_needed():
    credentials = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return credentials


def is_event_soon(start_date):
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    difference = start_date - now
    result = divmod(difference.days * seconds_in_day + difference.seconds, seconds_in_minute)
    return result[0] <= 5 and result[0] > 0


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    main()

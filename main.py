from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import os.path
import datetime


SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def main():
    creds = None 

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('calendar', 'v3', credentials=creds)

# Get events from calendar and create list of start/end times


# Go through list of start/end times and calculate amount of time between each event. Depending on this number, call the create_event()
# function, passing in specific arguments based on the type of break we want to create


if __name__ == '__main__':
    main()
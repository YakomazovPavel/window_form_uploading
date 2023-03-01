import os
from googleapiclient.discovery import build
from google.oauth2 import service_account

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')
SERVICE_ACCOUNT_FILE = '.\\credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SHEET_ID = '1zz7GVckuuoLFdDCAu8aqRtGZcPSZE4mfZzeyAgltGpY'
DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'


def connectiondef(listName, majorDimension='ROWS'):
    try:
        service = build('sheets', 'v4', credentials=CREDENTIALS)
    except:
        service = build('sheets', 'v4', credentials=CREDENTIALS, discoveryServiceUrl=DISCOVERY_SERVICE_URL)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID,
                                range=listName,
                                majorDimension=majorDimension).execute()
    values = result.get('values', [])
    return values

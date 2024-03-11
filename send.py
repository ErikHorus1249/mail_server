import base64
from utils import Create_Service
import base64
from email.mime.text import MIMEText
from requests import HTTPError

CLIENT_SECRET_FILE = "./credentials.json"
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

RECEIVER = 'anhnt376@fpt.com'
def send_email(hostname: str,
               ntp: str,):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    if service:
        message = MIMEText(f"Current NTP server: {ntp}\nExpected NTP server: 10.0.14.11\nPlease investigate and correct the NTP server configuration on this machine.")
        message['to'] = RECEIVER
        message['subject'] = f'ALERT: Mismatched NTP Server on {hostname}'
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (service.users().messages().send(userId="me", body=create_message).execute())
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
            message = None
    else:
        return


if __name__ == "__main__":
#   gmail_create_draft()
    pass
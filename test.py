# pip install google-auth-oauthlib google-api-python-client
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
creds = flow.run_local_server(port=0)
youtube = build("youtube", "v3", credentials=creds)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {"title": "AntiMatrix test upload", "description": "Test", "categoryId": "22"},
        "status": {"privacyStatus": "private", "selfDeclaredMadeForKids": False},
    },
    media_body=MediaFileUpload("test.mp4", resumable=True),
)
print(request.execute()["id"])
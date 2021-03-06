from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .models import Movie

import os

DEVELOPER_KEY = os.environ['YOUTUBE_API_KEY']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_video(movie):
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

        search_response = youtube.search().list(
            q= movie.name,
            part='id, snippet',
            maxResults=1,
            type='trailer',
            safeSearch='strict'
        ).execute()

        first_result = search_response.get('items', [])[0]
        print(first_result)

        video_id = first_result['id']['videoId']

        movie.trailer = video_id
        movie.save()
    
    except Exception as e:
        print(e)
    
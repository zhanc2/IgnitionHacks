import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = "AIzaSyC0kAC9H2dJWzsCRUMt3KQVXMJ2NB2bcn0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def getVideoIdFromLink(link: str):
    return link[32:]

def getCommments(link):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    req = youtube.commentThreads().list(
        part="snippet",
        videoId=getVideoIdFromLink(link)
    )
    resp = req.execute()
    
    print("")
    for item in resp["items"]:
        comment = item["snippet"]["topLevelComment"]
        comment_text = comment["snippet"]["textDisplay"]
        print(comment_text, "\n")

if __name__ == '__main__':
    getCommments(sys.argv[1])
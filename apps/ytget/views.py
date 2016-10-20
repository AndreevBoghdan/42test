import httplib2
import os
import sys
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.management import execute_from_command_line
# Create your views here.


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

from oauth2client.file import Storage
from oauth2client.contrib.django_util.views import oauth2_authorize



CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = 'AIzaSyC5yCDPrBrmWt1pM_Xsuj0514vRKqPkJoQ'

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = ''

clpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))
storpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   "oauth2.json"))
# Authorize the request and store authorization credentials.
def get_authenticated_service():
  flow = flow_from_clientsecrets(clpath, scope=YOUTUBE_READ_WRITE_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage(storpath)
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage)

  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))


def get_channel_videos(youtube):
    results = youtube.search().list(
        part="snippet",
        forMine=True,
        type='video',
        order='viewCount',
        maxResults=3,
        ).execute()
    return results

def get_channel(youtube):
    results = youtube.channels().list(
        part="snippet,statistics",
        mine=True,
        ).execute()
    return results

def get_video_info(youtube, id):
    results = youtube.videos().list(
                id=id,
                part='statistics'
              ).execute()

    return results

def start_youtube_login(request):
    flow = flow_from_clientsecrets(clpath, scope=YOUTUBE_READ_WRITE_SCOPE,
      message=MISSING_CLIENT_SECRETS_MESSAGE, redirect_uri='http://andreevb.pythonanywhere.com/ytube/')
    auth_uri = flow.step1_get_authorize_url()
    request.session['flow'] = flow
    return redirect(auth_uri)


def finish_youtube_login(request):
    code = request.GET.get('code')

    try:
        flow = request.session['flow']
    except Exception:
        return redirect(reverse('start_youtube_login'))
    try:
        credentials = flow.step2_exchange(code)
    except Exception:
        return redirect(reverse('start_youtube_login'))

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY,
        http=credentials.authorize(httplib2.Http()))
    resp = get_channel(youtube)
    viewCount = resp['items'][0]['statistics']['viewCount']
    subscriberCount = resp['items'][0]['statistics']['subscriberCount']
    name = resp['items'][0]['snippet']['title']

    res = get_channel_videos(youtube)


    video_ids = []
    for elem in res['items']:
      video_response = get_video_info(youtube, elem['id']['videoId'])
      video_ids.append({'id':elem['id']['videoId'], 'count': video_response['items'][0]['statistics']['viewCount']})


    return render(request,
                  'ytget/main.html',
                  {'user': request.user,
                  'video_ids': video_ids,
                  'followers': subscriberCount,
                  'name': name,
                  'viewCount': viewCount}
                  )

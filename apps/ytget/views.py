import yapi
from django.shortcuts import render
# Create your views here.


api = yapi.YoutubeAPI('AIzaSyC5yCDPrBrmWt1pM_Xsuj0514vRKqPkJoQ')

def main(request):
    if request.user.is_authenticated():
        channel = api.get_channel_by_name()
        raise Exception(channel)
    return render(request,
                  'ytget/main.html',
                  {'user': request.user,}
                  )
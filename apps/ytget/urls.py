from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^ytauth/start/$', 'ytget.views.start_youtube_login', name='start_youtube_login'),
    url(r'^$', 'ytget.views.finish_youtube_login', name='finish_youtube_login'),
)
urlpatterns += staticfiles_urlpatterns()

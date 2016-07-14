from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^$', 'hello.views.main', name='main'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout', name='logout'),
    url(r'^requests/$', 'hello.views.requests', name='requests'),
    url(r'^edit/$', 'hello.views.edit_person', name='edit_person'),
    url(r'^request_priority/$', 'hello.views.request_priority',
        name='request_priority'),
    url(r'^request_priority/page/(?P<page_number>\d+)/$',
        'hello.views.request_priority',
        name='request_priority'),
)
urlpatterns += staticfiles_urlpatterns()

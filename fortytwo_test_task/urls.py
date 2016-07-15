from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('apps.hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),
    url(r'', include('social_auth.urls')),
)
urlpatterns += staticfiles_urlpatterns()

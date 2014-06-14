# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('blog.views',
    url(r'^blog/$', 'blog', name='blog'),
    url(r'^blog/(?P<billet_id>[0-9]+)/$', 'billet', name='billet'),
)

urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += patterns('',
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
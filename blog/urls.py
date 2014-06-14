from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^blog/$', 'blog', name='blog'),
    url(r'^blog/(?P<billet_id>[0-9]+)/$', 'billet', name='billet'),
)
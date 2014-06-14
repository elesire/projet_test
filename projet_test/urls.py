from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('blog.urls', namespace='blog', app_name='blog')),
)
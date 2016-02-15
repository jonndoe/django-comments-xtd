import django
if django.VERSION[:2] < (1, 8):
    from django.conf.urls import patterns, include, url
else:
    from django.conf.urls import include, url

from django.contrib import admin
from django_comments_xtd import LatestCommentFeed

from multiple import views


admin.autodiscover()


pattern_list = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('multiple.blog.urls')),
    url(r'^projects/', include('multiple.projects.urls')),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'^$', views.homepage_v, name='homepage'),
    url(r'^feeds/comments/$', LatestCommentFeed(), name='comments-feed'),
]

urlpatterns = None

if django.VERSION[:2] < (1, 8):
    urlpatterns = patterns('multiple.views', *patterns_list)
else:
    urlpatterns = pattern_list

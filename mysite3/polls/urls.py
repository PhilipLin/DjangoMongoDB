from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<path>[^/]+)/$', views.detail,name='detail'),
    # ex: /polls/id/rating/comment
    url(r'^(?P<path>[^/]+)/(?P<rating>\d+)/(?P<rate_name>\w+)/(?P<comment>\w+)/$', views.update, name='update'),
    # ex: /polls/pathtoimage/
    url(r'^(?P<path>[^/]+)/(?P<owner>\w+)/(?P<desc>\w+)/$', views.add, name='add'),

)

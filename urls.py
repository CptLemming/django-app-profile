from django.conf.urls import patterns, url

from .views import ProfileListView, ProfileDetailView, ProfileFeedView

urlpatterns = patterns(
    '',
    url(r'^$', ProfileListView.as_view(), name='profile_index'),
    url(r'^(?P<pk>[0-9])/$', ProfileDetailView.as_view(), name='profile_detail'),
    url(r'^(?P<pk>[0-9])/feed/$', ProfileFeedView.as_view(), name='profile_feed'),
)

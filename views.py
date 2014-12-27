from django.views.generic import ListView, DetailView

from .models import Profile


class ProfileListView(ListView):
    model = Profile
    template_name = 'profile/list.html'
    context_object_name = 'users'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/detail.html'
    context_object_name = 'profile'


class ProfileFeedView(DetailView):
    model = Profile
    template_name = 'profile/feed.html'
    context_object_name = 'profile'

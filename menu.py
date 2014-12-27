from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

from .models import Profile


class ProfileMenu(CMSAttachMenu):
    name = _('Profile Menu')

    def get_nodes(self, request):
        nodes = []

        for profile in Profile.objects.all():
            node = NavigationNode(
                profile.username,
                profile.get_absolute_url(),
                profile.pk
            )
            nodes.append(node)

            feed_node = NavigationNode(
                '%s Feed' % profile.username,
                profile.get_feed_url(),
                '%d-feed' % profile.pk,
                profile.pk
            )
            nodes.append(feed_node)
        return nodes

menu_pool.register_menu(ProfileMenu)

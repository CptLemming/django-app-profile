from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .menu import ProfileMenu


class ProfileApp(CMSApp):
    name = _('Profile')
    urls = ['profile.urls']
    menus = [ProfileMenu, ]

apphook_pool.register(ProfileApp)

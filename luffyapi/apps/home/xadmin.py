from django.contrib import admin

# Register your models here.

import xadmin
from xadmin import views

from luffyapi.apps.user.models import User
from . import models

class GlobalSettings(object):
    site_title = '路飞学堂'
    site_foot = '路飞学堂有限公司'
    menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(User)
xadmin.site.register(models.Banner)

# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class AdminSite(admin.AdminSite):
    site_title = 'TITLE'
    site_header = 'HEADER'
    site_url = None
    index_title = None


site = AdminSite()
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)


# Usage in app admin:
#
# from api.admin import site
#
# @admin.register(models.MODELNAME, site=site)
# class MODELNAMEAdmin(admin.ModelAdmin):
# .
# .
# .

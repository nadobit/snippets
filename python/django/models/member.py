# -*- coding: utf-8 -*-
import os
import hashlib
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


def avatar_file_names(instance, filename):
    name, ext = os.path.splitext(filename)
    uu = hashlib.md5(instance.avatar.read()).hexdigest()
    return '/'.join(['avatars', uu[:2], uu[2:4], uu, slugify(name) + ext])


class Member(models.Model):

    user = models.OneToOneField(User, verbose_name=_('user'))
    avatar = models.ImageField(upload_to=avatar_file_names, null=True, blank=True, verbose_name=_('avatar'))

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    def __unicode__(self):

        user = self.user
        if user.first_name and user.last_name:
            return '%s %s' % (user.first_name, user.last_name)

        if user.last_name:
            return user.last_name

        if user.first_name:
            return user.first_name

        return self.user.__unicode__()

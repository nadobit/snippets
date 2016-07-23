# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):

    CONTINENT_ANTARCTICA = 1
    CONTINENT_AUSTRALIA = 2
    CONTINENT_AFRICA = 3
    CONTINENT_NORTH_AMERICA = 4
    CONTINENT_SOUTH_AMERICA = 5
    CONTINENT_EUROPE = 6
    CONTINENT_ASIA = 7
    CONTINENT_SELECT = (
        (CONTINENT_ANTARCTICA, _('Antarctica')),
        (CONTINENT_AUSTRALIA, _('Australia')),
        (CONTINENT_AFRICA, _('Africa')),
        (CONTINENT_NORTH_AMERICA, _('North America')),
        (CONTINENT_SOUTH_AMERICA, _('South America')),
        (CONTINENT_EUROPE, _('Europe')),
        (CONTINENT_ASIA, _('Asia')),
    )

    continent = models.PositiveSmallIntegerField(choices=CONTINENT_SELECT, default=CONTINENT_EUROPE, verbose_name=_('continent'))
    name = models.CharField(max_length=255, verbose_name=_('name of country'))
    captial = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('captial'))
    iso_2 = models.CharField(max_length=2, unique=True, verbose_name='ISO-2')
    iso_3 = models.CharField(max_length=3, blank=True, null=True, verbose_name='ISO-3')
    ioc = models.CharField(max_length=3, blank=True, null=True, verbose_name='IOC')

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countrys')
        ordering = ('name', )

    def __unicode__(self):
        return self.name

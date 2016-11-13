# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy


def validate_zip_code(value):

    zip_code = ZipCodeGermany.objects.filter(zip_code=value).first()
    if not zip_code:
        raise ValidationError(
            _('%(value)s seems not to be an invalid zip code'),
            params={'value': value},
        )


class ZipCodeGermany(models.Model):

    STATE_BW = 'BW'
    STATE_BY = 'BY'
    STATE_BE = 'BE'
    STATE_BB = 'BB'
    STATE_HB = 'HB'
    STATE_HH = 'HH'
    STATE_HE = 'HE'
    STATE_MV = 'MV'
    STATE_NI = 'NI'
    STATE_NW = 'NW'
    STATE_RP = 'RP'
    STATE_SL = 'SL'
    STATE_SN = 'SN'
    STATE_ST = 'ST'
    STATE_SH = 'SH'
    STATE_TH = 'TH'
    STATE_CHOICES = (
        (STATE_BW, 'Baden-Württemberg'),
        (STATE_BY, 'Bayern'),
        (STATE_BE, 'Berlin'),
        (STATE_BB, 'Brandenburg'),
        (STATE_HB, 'Bremen'),
        (STATE_HH, 'Hamburg'),
        (STATE_HE, 'Hessen'),
        (STATE_MV, 'Mecklenburg-Vorpommern'),
        (STATE_NI, 'Niedersachsen'),
        (STATE_NW, 'Nordrhein-Westfalen'),
        (STATE_RP, 'Rheinland-Pfalz'),
        (STATE_SL, 'Saarland'),
        (STATE_SN, 'Sachsen'),
        (STATE_ST, 'Sachsen-Anhalt'),
        (STATE_SH, 'Schlewig-Holstein'),
        (STATE_TH, 'Thüringen'),
    )

    city = models.CharField(max_length=40, verbose_name=_('city'))
    city_addon = models.CharField(max_length=40, blank=True, verbose_name=_('city addon'))
    zip_code = models.CharField(max_length=5, verbose_name=_('zip code'))
    phone_prefix = models.CharField(max_length=10, blank=True, verbose_name=_('phone prefix'))
    state = models.CharField(max_length=2, choices=STATE_CHOICES, db_index=True, verbose_name=pgettext_lazy(u'country state', u'state'))

    class Meta:
        verbose_name = _('german zip code')
        verbose_name_plural = _('german zip codes')

    def __unicode__(self):
        return self.zip_code


class Address(models.Model):

    company_name = models.CharField(max_length=100, blank=True, verbose_name=_('company name'))
    name = models.CharField(max_length=100, blank=True, verbose_name=_('name'))
    street = models.CharField(max_length=100, verbose_name=_('street'))
    house_number = models.CharField(max_length=10, verbose_name=_('house number'))
    zip_code = models.CharField(max_length=5, validators=[RegexValidator(regex='[0-9]+', message=_('Enter a valid zip code')), validate_zip_code], verbose_name=_('zip code'))
    city = models.CharField(max_length=40, verbose_name=_('city'))
    phone = models.CharField(max_length=32, blank=True, verbose_name=_('phone'), help_text=_('used for further inquiry'))

    class Meta:
        abstract = True
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    @property
    def get_address_line(self):
        return "%s %s, %s %s" % (self.street, self.house_number, self.zip_code, self.city)

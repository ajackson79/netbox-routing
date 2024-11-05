import netaddr
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from netbox.models import PrimaryModel

from ipam.fields import IPNetworkField
from netbox_routing import choices
from netbox_routing.fields.ip import IPAddressField

__all__ = (
    'ISISInstance',
    'ISISInterface',
)

class ISISInstance(PrimaryModel):
    name = models.CharField(max_length=100)
    isis_type = models.IntegerField(
        verbose_name='ISIS Type',
        blank=False,
        null=False,
        choices=[
            (2, 'level-2-only'),
            (1, 'level-1'),
            (3, 'level-1-2')
        ],
        default=2
    )
    net = models.CharField(
        max_length=30,
        verbose_name='Network entity title (NET)',
        blank=False,
        null=False
    )
    device = models.ForeignKey(
        to='dcim.Device',
        related_name='isis_instances',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    vrf = models.ForeignKey(
        verbose_name=_('VRF'),
        to='ipam.VRF',
        related_name='isis_instances',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    clone_fields = ('device',)
    prerequisite_models = (
        'dcim.Device',
    )
    class Meta:
        verbose_name = 'ISIS Instance'
        ordering = ('name', 'device', 'vrf', 'net')
        constraints = (
            models.UniqueConstraint(
                fields=('net', ),
                name='%(app_label)s_%(class)s_unique_net'
            ),
            models.UniqueConstraint(
                fields=('name', 'device'),
                name='%(app_label)s_%(class)s_unique_name_device'
            ),
        )

    def __str__(self):
        return f'{self.name} ({self.net})'

    def get_absolute_url(self):
        return reverse('plugins:netbox_routing:isisinstance', args=[self.pk])

class ISISInterface(PrimaryModel):
    instance = models.ForeignKey(
        to='netbox_routing.ISISInstance',
        related_name='interfaces',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    interface = models.ForeignKey(
        to='dcim.Interface',
        related_name='isis_interfaces',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    metric = models.SmallIntegerField(verbose_name='Metric', blank=True, null=True)
    passive = models.BooleanField(verbose_name='Passive', blank=True, null=True)
    bfd = models.BooleanField(blank=True, null=True, verbose_name='BFD')
    authentication = models.CharField(
        max_length=50,
        choices=choices.AuthenticationChoices,
        blank=True,
        null=True
    )
    passphrase = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    clone_fields = ('instance', 'metric', 'bfd', 'authentication', 'passphrase')
    prerequisite_models = ('netbox_routing.ISISInstance', 'dcim.Interface')

    class Meta:
        verbose_name = 'ISIS Interface'
        ordering = ('instance', 'interface')  # Name may be non-unique
        constraints = (
            models.UniqueConstraint(
                fields=('interface', ),
                name='%(app_label)s_%(class)s_unique_interface'
            ),
        )

    def __str__(self):
        return f'{self.interface.name}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_routing:isisinterface', args=[self.pk])
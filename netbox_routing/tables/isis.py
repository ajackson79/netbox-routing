import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable
from netbox_routing.models import ISISInstance, ISISInterface

__all__ = (
    'ISISInstanceTable',
    'ISISInterfaceTable',
)

class ISISInstanceTable(NetBoxTable):
    net = tables.Column(
        verbose_name =_('NET'),
        linkify=True
    )
    device = tables.Column(
        verbose_name=_('Device'),
        linkify=True
    )
    vrf = tables.Column(
        verbose_name=_('VRF'),
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = ISISInstance
        fields = ('pk', 'id', 'name', 'net', 'device', 'vrf', )
        default_columns = ('pk', 'id', 'name', 'net', 'device', )

class ISISInterfaceTable(NetBoxTable):
    instance = tables.Column(
        verbose_name=_('Instance'),
        linkify=True
    )
    interface = tables.Column(
        verbose_name=_('Interface'),
        linkify=True
    )
    device = tables.Column(
        verbose_name=_('Device'),
        accessor='interface.device',
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = ISISInterface
        fields = (
            'pk', 'id', 'instance', 'device', 'interface', 'metric', 'passive', 'bfd', 'authentication', 'passphrase'
        )
        default_columns = ('pk', 'id', 'instance', 'device', 'interface', 'passive')
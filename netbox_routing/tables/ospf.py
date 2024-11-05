import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable
from netbox_routing.models import OSPFArea, OSPFInstance, OSPFInterface, OSPFNetworks


__all__ = (
    'OSPFAreaTable',
    'OSPFInstanceTable',
    'OSPFInterfaceTable',
    'OSPFNetworksTable',
)


class OSPFInstanceTable(NetBoxTable):
    router_id = tables.Column(
        verbose_name =_('Router ID'),
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
        model = OSPFInstance
        fields = ('pk', 'id', 'name', 'router_id', 'process_id', 'device', 'vrf', )
        default_columns = ('pk', 'id', 'name', 'router_id', 'process_id', 'device', )


class OSPFAreaTable(NetBoxTable):
    area_id = tables.Column(
        verbose_name=_('Aread'),
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = OSPFArea
        fields = ('pk', 'id', 'area_id')
        default_columns = ('pk', 'id', 'area_id')


class OSPFInterfaceTable(NetBoxTable):
    instance = tables.Column(
        verbose_name=_('Instance'),
        linkify=True
    )
    area = tables.Column(
        verbose_name=_('Area'),
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
        model = OSPFInterface
        fields = (
            'pk', 'id', 'instance', 'area', 'device', 'interface', 'cost', 'passive', 'priority', 'bfd', 'authentication', 'passphrase'
        )
        default_columns = ('pk', 'id', 'instance', 'area', 'device', 'interface', 'passive')

class OSPFNetworksTable(NetBoxTable):
    network = tables.Column(
        verbose_name=_('Network'),
        linkify=True
    )
    instance = tables.Column(
        verbose_name=_('Instance'),
        linkify=True
    )
    area = tables.Column(
        verbose_name=_('Area'),
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = OSPFNetworks
        fields = ('pk', 'id', 'network', 'instance', 'area', )
        default_columns = ('network', 'instance', 'area', )

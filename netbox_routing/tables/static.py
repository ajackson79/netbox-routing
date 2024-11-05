import django_tables2 as tables
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from netbox.tables import NetBoxTable
from netbox_routing.models import StaticRoute


class StaticRouteTable(NetBoxTable):
    devices = tables.Column(
        verbose_name=_('Devices'),
        # linkify_item=True,
        accessor='pk', 
        empty_values=(),
    )
    vrf = tables.Column(
        verbose_name=_('VRF'),
        linkify=True,
    )

    def render_devices(self, value, record):
        if hasattr(record, 'pk'):
        # Generate the URL for the devices view using the StaticRoute ID
            url = reverse('plugins:netbox_routing:staticroute_devices', kwargs={'pk': record.pk})
            return mark_safe(f'<a href="{url}">Assigned Devices</a>')
        return '-'
    
    class Meta(NetBoxTable.Meta):
        model = StaticRoute
        fields = (
            'pk', 'id', 'devices', 'vrf', 'prefix', 'next_hop', 'name', 'metric', 'route_tag', 'permanent', 'description',
            'comments',
        )
        default_columns = ('pk', 'id', 'devices', 'vrf', 'prefix', 'next_hop', 'route_tag', 'name')

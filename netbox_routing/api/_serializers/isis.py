from rest_framework import serializers

from dcim.api.serializers_.device_components import InterfaceSerializer
from dcim.api.serializers_.devices import DeviceSerializer
from ipam.api.serializers_.vrfs import VRFSerializer
from netbox.api.serializers import NetBoxModelSerializer
from netbox_routing.models import ISISInstance, ISISInterface

__all__ = (
    'ISISInstanceSerializer',
    'ISISInterfaceSerializer',
)

class ISISInstanceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_routing-api:isisinstance-detail')
    device = DeviceSerializer(nested=True)
    vrf = VRFSerializer(nested=True)

    class Meta:
        model = ISISInstance
        fields = (
            'url', 'id', 'display', 'name', 'net', 'device', 'isis_type', 'vrf', 'description', 'comments',
        )
        brief_fields = ('url', 'id', 'display', 'name', 'net', 'isis_type', 'device', 'vrf', )

class ISISInterfaceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_routing-api:isisinterface-detail')
    instance = ISISInstanceSerializer(nested=True)
    interface = InterfaceSerializer(nested=True)

    class Meta:
        model = ISISInterface
        fields = (
            'url', 'id', 'display', 'instance', 'interface', 'metric', 'passive', 'bfd', 'authentication',
            'passphrase', 'description', 'comments',
        )
        brief_fields = (
            'url', 'id', 'display', 'instance', 'interface', 'passive',
        )
from netbox.api.viewsets import NetBoxModelViewSet
from netbox_routing import filtersets
from netbox_routing.api.serializers import OSPFInstanceSerializer, OSPFAreaSerializer, OSPFInterfaceSerializer, OSPFNetworksSerializer
from netbox_routing.models import OSPFInstance, OSPFArea, OSPFInterface, OSPFNetworks


__all__ = (
    'OSPFInstanceViewSet',
    'OSPFAreaViewSet',
    'OSPFInterfaceViewSet',
    'OSPFNetworksViewSet',
)


class OSPFInstanceViewSet(NetBoxModelViewSet):
    queryset = OSPFInstance.objects.all()
    serializer_class = OSPFInstanceSerializer
    filterset_class = filtersets.OSPFInstanceFilterSet


class OSPFAreaViewSet(NetBoxModelViewSet):
    queryset = OSPFArea.objects.all()
    serializer_class = OSPFAreaSerializer
    filterset_class = filtersets.OSPFAreaFilterSet


class OSPFInterfaceViewSet(NetBoxModelViewSet):
    queryset = OSPFInterface.objects.all()
    serializer_class = OSPFInterfaceSerializer
    filterset_class = filtersets.OSPFInterfaceFilterSet


class OSPFNetworksViewSet(NetBoxModelViewSet):
    queryset = OSPFNetworks.objects.all()
    serializer_class = OSPFNetworksSerializer
    filterset_class = filtersets.OSPFNetworksFilterSet
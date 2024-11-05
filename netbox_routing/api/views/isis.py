from netbox.api.viewsets import NetBoxModelViewSet
from netbox_routing import filtersets
from netbox_routing.api.serializers import ISISInstanceSerializer, ISISInterfaceSerializer
from netbox_routing.models import ISISInstance, ISISInterface

__all__ = (
    'ISISInstanceViewSet',
    'ISISInterfaceViewSet',
)

class ISISInstanceViewSet(NetBoxModelViewSet):
    queryset = ISISInstance.objects.all()
    serializer_class = ISISInstanceSerializer
    filterset_class = filtersets.ISISInstanceFilterSet

class ISISInterfaceViewSet(NetBoxModelViewSet):
    queryset = ISISInterface.objects.all()
    serializer_class = ISISInterfaceSerializer
    filterset_class = filtersets.ISISInterfaceFilterSet
from dcim.models import Device
from netbox.views import generic
from utilities.views import register_model_view, ViewTab

from netbox_routing.filtersets import StaticRouteFilterSet, OSPFInstanceFilterSet, ISISInstanceFilterSet
from netbox_routing.models import StaticRoute, OSPFInstance, ISISInstance
from netbox_routing.tables.static import StaticRouteTable
from netbox_routing.tables.ospf import OSPFInstanceTable
from netbox_routing.tables.isis import ISISInstanceTable


@register_model_view(Device, name='staticroutes', path='static_routes')
class DeviceStaticRoutesView(generic.ObjectChildrenView):
    template_name = 'generic/object_children.html'
    queryset = Device.objects.all()
    child_model = StaticRoute
    table = StaticRouteTable
    filterset = StaticRouteFilterSet
    tab = ViewTab(
        label='Static Routes',
        badge=lambda obj: StaticRoute.objects.filter(devices=obj).count(),
        permission='netbox_routing.view_staticroute'
    )

    def get_children(self, request, device):
        return self.child_model.objects.filter(devices=device)
    
@register_model_view(Device, name='ospfinstance', path='ospfinstance')
class DeviceOSPFInstanceView(generic.ObjectChildrenView):
    template_name = 'generic/object_children.html'
    queryset = Device.objects.all()
    child_model = OSPFInstance
    table = OSPFInstanceTable
    filterset = OSPFInstanceFilterSet
    tab = ViewTab(
        label='OSPF Instances',
        badge=lambda obj: OSPFInstance.objects.filter(device=obj).count(),
        permission='netbox_routing.view_ospfinstance'
    )

    def get_children(self, request, device):
        return self.child_model.objects.filter(device=device)
    
@register_model_view(Device, name='isisinstance', path='isisinstance')
class DeviceISISInstanceView(generic.ObjectChildrenView):
    template_name = 'generic/object_children.html'
    queryset = Device.objects.all()
    child_model = ISISInstance
    table = ISISInstanceTable
    filterset = ISISInstanceFilterSet
    tab = ViewTab(
        label='ISIS Instances',
        badge=lambda obj: ISISInstance.objects.filter(device=obj).count(),
        permission='netbox_routing.view_isisinstance'
    )

    def get_children(self, request, device):
        return self.child_model.objects.filter(device=device)

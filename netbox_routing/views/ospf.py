from netbox.views.generic import ObjectListView, ObjectEditView, ObjectView, ObjectDeleteView, ObjectChildrenView, \
    BulkImportView, BulkEditView, BulkDeleteView
from netbox_routing.filtersets.ospf import OSPFInterfaceFilterSet, OSPFAreaFilterSet, OSPFInstanceFilterSet, OSPFNetworksFilterSet
from netbox_routing.forms import *
from netbox_routing.tables.ospf import OSPFAreaTable, OSPFInstanceTable, OSPFInterfaceTable, OSPFNetworksTable
from utilities.views import register_model_view, ViewTab

from netbox_routing.models import OSPFArea, OSPFInstance, OSPFInterface, OSPFNetworks

__all__ = (
    'OSPFInstanceListView',
    'OSPFInstanceView',
    'OSPFInstanceInterfacesView',
    'OSPFInstanceNetworksView',
    'OSPFInstanceEditView',
    'OSPFInstanceBulkEditView',
    'OSPFInstanceDeleteView',
    'OSPFInstanceBulkDeleteView',

    'OSPFAreaListView',
    'OSPFAreaView',
    'OSPFAreaInterfacesView',
    'OSPFAreaEditView',
    'OSPFAreaBulkEditView',
    'OSPFAreaDeleteView',
    'OSPFAreaBulkDeleteView',

    'OSPFInterfaceListView',
    'OSPFInterfaceView',
    'OSPFInterfaceEditView',
    'OSPFInterfaceBulkEditView',
    'OSPFInterfaceDeleteView',
    'OSPFInterfaceBulkDeleteView',

    'OSPFNetworksListView',
    'OSPFNetworksView',
    'OSPFNetworksEditView',
    'OSPFNetworksBulkEditView',
    'OSPFNetworksDeleteView',
    'OSPFNetworksBulkDeleteView',
)


#
# Instance
#
@register_model_view(OSPFInstance, name='list')
class OSPFInstanceListView(ObjectListView):
    queryset = OSPFInstance.objects.all()
    table = OSPFInstanceTable
    filterset = OSPFInstanceFilterSet
    filterset_form = OSPFInstanceFilterForm


@register_model_view(OSPFInstance)
class OSPFInstanceView(ObjectView):
    queryset = OSPFInstance.objects.all()
    template_name = 'netbox_routing/ospfinstance.html'


@register_model_view(OSPFInstance, name='interfaces')
class OSPFInstanceInterfacesView(ObjectChildrenView):
    template_name = 'netbox_routing/object_children.html'
    queryset = OSPFInstance.objects.all()
    child_model = OSPFInterface
    table = OSPFInterfaceTable
    filterset = OSPFInterfaceFilterSet
    tab = ViewTab(
        label='Interfaces',
        badge=lambda obj: OSPFInterface.objects.filter(instance=obj).count(),
        hide_if_empty=False,
    )

    def get_children(self, request, parent):
        return self.child_model.objects.filter(instance=parent)


@register_model_view(OSPFInstance, name='networks')
class OSPFInstanceNetworksView(ObjectChildrenView):
    template_name = 'netbox_routing/object_children.html'
    queryset = OSPFInstance.objects.all()
    child_model = OSPFNetworks
    table = OSPFNetworksTable
    filterset = OSPFNetworksFilterSet
    tab = ViewTab(
        label='Networks',
        badge=lambda obj: OSPFNetworks.objects.filter(instance=obj).count(),
        hide_if_empty=False,
    )

    def get_children(self, request, parent):
        return self.child_model.objects.filter(instance=parent)


@register_model_view(OSPFInstance, name='edit')
class OSPFInstanceEditView(ObjectEditView):
    queryset = OSPFInstance.objects.all()
    form = OSPFInstanceForm


@register_model_view(OSPFInstance, name='bulk_edit')
class OSPFInstanceBulkEditView(BulkEditView):
    queryset = OSPFInstance.objects.all()
    filterset = OSPFInstanceFilterSet
    table = OSPFInstanceTable
    form = OSPFInstanceBulkEditForm


@register_model_view(OSPFInstance, name='delete')
class OSPFInstanceDeleteView(ObjectDeleteView):
    queryset = OSPFInstance.objects.all()


@register_model_view(OSPFInstance, name='bulk_delete')
class OSPFInstanceBulkDeleteView(BulkDeleteView):
    queryset = OSPFInstance.objects.all()
    filterset = OSPFInstanceFilterSet
    table = OSPFInstanceTable


class OSPFInstanceBulkImportView(BulkImportView):
    queryset = OSPFInstance.objects.all()
    model_form = OSPFInstanceImportForm


#
# Area
#
@register_model_view(OSPFArea, name='list')
class OSPFAreaListView(ObjectListView):
    queryset = OSPFArea.objects.all()
    table = OSPFAreaTable
    filterset = OSPFAreaFilterSet
    filterset_form = OSPFAreaFilterForm


@register_model_view(OSPFArea)
class OSPFAreaView(ObjectView):
    queryset = OSPFArea.objects.all()
    template_name = 'netbox_routing/ospfarea.html'


@register_model_view(OSPFArea, name='interfaces')
class OSPFAreaInterfacesView(ObjectChildrenView):
    template_name = 'netbox_routing/object_children.html'
    queryset = OSPFArea.objects.all()
    child_model = OSPFInterface
    table = OSPFInterfaceTable
    filterset = OSPFInterfaceFilterSet
    tab = ViewTab(
        label='Interfaces',
        badge=lambda obj: OSPFInterface.objects.filter(area=obj).count(),
    )

    def get_children(self, request, parent):
        return self.child_model.objects.filter(area=parent)


@register_model_view(OSPFArea, name='edit')
class OSPFAreaEditView(ObjectEditView):
    queryset = OSPFArea.objects.all()
    form = OSPFAreaForm


@register_model_view(OSPFArea, name='bulk_edit')
class OSPFAreaBulkEditView(BulkEditView):
    queryset = OSPFArea.objects.all()
    table = OSPFAreaTable
    filterset = OSPFAreaFilterSet
    form = OSPFAreaBulkEditForm


@register_model_view(OSPFArea, name='delete')
class OSPFAreaDeleteView(ObjectDeleteView):
    queryset = OSPFArea.objects.all()


@register_model_view(OSPFArea, name='delete')
class OSPFAreaBulkDeleteView(BulkDeleteView):
    queryset = OSPFArea.objects.all()
    table = OSPFAreaTable
    filterset = OSPFAreaFilterSet


class OSPFAreaBulkImportView(BulkImportView):
    queryset = OSPFArea.objects.all()
    model_form = OSPFAreaImportForm


#
# Interface
#
@register_model_view(OSPFInterface, name='list')
class OSPFInterfaceListView(ObjectListView):
    queryset = OSPFInterface.objects.all()
    table = OSPFInterfaceTable
    filterset = OSPFInterfaceFilterSet
    filterset_form = OSPFInterfaceFilterForm


@register_model_view(OSPFInterface)
class OSPFInterfaceView(ObjectView):
    queryset = OSPFInterface.objects.all()
    template_name = 'netbox_routing/ospfinterface.html'


@register_model_view(OSPFInterface, name='edit')
class OSPFInterfaceEditView(ObjectEditView):
    queryset = OSPFInterface.objects.all()
    form = OSPFInterfaceForm


@register_model_view(OSPFInterface, name='delete')
class OSPFInterfaceDeleteView(ObjectDeleteView):
    queryset = OSPFInterface.objects.all()


class OSPFInterfaceBulkImportView(BulkImportView):
    queryset = OSPFInterface.objects.all()
    model_form = OSPFInterfaceImportForm


class OSPFInterfaceBulkEditView(BulkEditView):
    queryset = OSPFInterface.objects.all()
    filterset = OSPFInterfaceFilterSet
    table = OSPFInterfaceTable
    form = OSPFInterfaceBulkEditForm


class OSPFInterfaceBulkDeleteView(BulkDeleteView):
    queryset = OSPFInterface.objects.all()
    filterset = OSPFInterfaceFilterSet
    table = OSPFInterfaceTable


#
# Networks
#
@register_model_view(OSPFNetworks, name='list')
class OSPFNetworksListView(ObjectListView):
    queryset = OSPFNetworks.objects.all()
    table = OSPFNetworksTable
    filterset = OSPFNetworksFilterSet
    filterset_form = OSPFNetworksFilterForm


@register_model_view(OSPFNetworks)
class OSPFNetworksView(ObjectView):
    queryset = OSPFNetworks.objects.all()
    template_name = 'netbox_routing/ospfnetworks.html'


@register_model_view(OSPFNetworks, name='edit')
class OSPFNetworksEditView(ObjectEditView):
    queryset = OSPFNetworks.objects.all()
    form = OSPFNetworksForm


@register_model_view(OSPFNetworks, name='bulk_edit')
class OSPFNetworksBulkEditView(BulkEditView):
    queryset = OSPFNetworks.objects.all()
    table = OSPFNetworksTable
    filterset = OSPFNetworksFilterSet
    form = OSPFNetworksBulkEditForm


@register_model_view(OSPFNetworks, name='delete')
class OSPFNetworksDeleteView(ObjectDeleteView):
    queryset = OSPFNetworks.objects.all()


@register_model_view(OSPFNetworks, name='delete')
class OSPFNetworksBulkDeleteView(BulkDeleteView):
    queryset = OSPFNetworks.objects.all()
    table = OSPFNetworksTable
    filterset = OSPFNetworksFilterSet


class OSPFNetworksBulkImportView(BulkImportView):
    queryset = OSPFNetworks.objects.all()
    model_form = OSPFNetworksImportForm
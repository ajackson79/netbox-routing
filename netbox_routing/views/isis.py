from netbox.views.generic import ObjectListView, ObjectEditView, ObjectView, ObjectDeleteView, ObjectChildrenView, \
    BulkImportView, BulkEditView, BulkDeleteView
from netbox_routing.filtersets.isis import ISISInstanceFilterSet, ISISInterfaceFilterSet
from netbox_routing.forms import *
from netbox_routing.tables.isis import ISISInstanceTable, ISISInterfaceTable
from utilities.views import register_model_view, ViewTab

from netbox_routing.models import ISISInstance, ISISInterface

__all__ = (
    'ISISInstanceListView',
    'ISISInstanceView',
    'ISISInstanceInterfacesView',
    'ISISInstanceEditView',
    'ISISInstanceBulkEditView',
    'ISISInstanceDeleteView',
    'ISISInstanceBulkDeleteView',

    'ISISInterfaceListView',
    'ISISInterfaceView',
    'ISISInterfaceEditView',
    'ISISInterfaceBulkEditView',
    'ISISInterfaceDeleteView',
    'ISISInterfaceBulkDeleteView',
)

#
# Instance
#
@register_model_view(ISISInstance, name='list')
class ISISInstanceListView(ObjectListView):
    queryset = ISISInstance.objects.all()
    table = ISISInstanceTable
    filterset = ISISInstanceFilterSet
    filterset_form = ISISInstanceFilterForm


@register_model_view(ISISInstance)
class ISISInstanceView(ObjectView):
    queryset = ISISInstance.objects.all()
    template_name = 'netbox_routing/isisinstance.html'


@register_model_view(ISISInstance, name='interfaces')
class ISISInstanceInterfacesView(ObjectChildrenView):
    template_name = 'netbox_routing/object_children.html'
    queryset = ISISInstance.objects.all()
    child_model = ISISInterface
    table = ISISInterfaceTable
    filterset = ISISInterfaceFilterSet
    tab = ViewTab(
        label='Interfaces',
        badge=lambda obj: ISISInterface.objects.filter(instance=obj).count(),
        hide_if_empty=False,
    )

    def get_children(self, request, parent):
        return self.child_model.objects.filter(instance=parent)
    

@register_model_view(ISISInstance, name='edit')
class ISISInstanceEditView(ObjectEditView):
    queryset = ISISInstance.objects.all()
    form = ISISInstanceForm


@register_model_view(ISISInstance, name='bulk_edit')
class ISISInstanceBulkEditView(BulkEditView):
    queryset = ISISInstance.objects.all()
    filterset = ISISInstanceFilterSet
    table = ISISInstanceTable
    form = ISISInstanceBulkEditForm


@register_model_view(ISISInstance, name='delete')
class ISISInstanceDeleteView(ObjectDeleteView):
    queryset = ISISInstance.objects.all()


@register_model_view(ISISInstance, name='bulk_delete')
class ISISInstanceBulkDeleteView(BulkDeleteView):
    queryset = ISISInstance.objects.all()
    filterset = ISISInstanceFilterSet
    table = ISISInstanceTable


class ISISInstanceBulkImportView(BulkImportView):
    queryset = ISISInstance.objects.all()
    model_form = ISISInstanceImportForm


#
# Interface
#
@register_model_view(ISISInterface, name='list')
class ISISInterfaceListView(ObjectListView):
    queryset = ISISInterface.objects.all()
    table = ISISInterfaceTable
    filterset = ISISInterfaceFilterSet
    filterset_form = ISISInterfaceFilterForm


@register_model_view(ISISInterface)
class ISISInterfaceView(ObjectView):
    queryset = ISISInterface.objects.all()
    template_name = 'netbox_routing/isisinterface.html'


@register_model_view(ISISInterface, name='edit')
class ISISInterfaceEditView(ObjectEditView):
    queryset = ISISInterface.objects.all()
    form = ISISInterfaceForm


@register_model_view(ISISInterface, name='delete')
class ISISInterfaceDeleteView(ObjectDeleteView):
    queryset = ISISInterface.objects.all()


class ISISInterfaceBulkImportView(BulkImportView):
    queryset = ISISInterface.objects.all()
    model_form = ISISInterfaceImportForm


class ISISInterfaceBulkEditView(BulkEditView):
    queryset = ISISInterface.objects.all()
    filterset = ISISInterfaceFilterSet
    table = ISISInterfaceTable
    form = ISISInterfaceBulkEditForm


class ISISInterfaceBulkDeleteView(BulkDeleteView):
    queryset = ISISInterface.objects.all()
    filterset = ISISInterfaceFilterSet
    table = ISISInterfaceTable
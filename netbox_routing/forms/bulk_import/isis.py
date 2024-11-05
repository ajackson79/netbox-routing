from django.utils.translation import gettext as _

from dcim.models import Interface, Device
from ipam.models import VRF
from netbox.forms import NetBoxModelImportForm
from utilities.forms.fields import CSVModelChoiceField

from netbox_routing.models import ISISInstance, ISISInterface

__all__ = (
    'ISISInstanceImportForm',
    'ISISInterfaceImportForm',
)

class ISISInstanceImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
        to_field_name='name',
        help_text=_('Name of device')
    )
    vrf = CSVModelChoiceField(
        queryset=VRF.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Name of VRF')
    )

    class Meta:
        model = ISISInstance
        fields = ('name', 'net', 'device', 'isis_type', 'vrf', 'description', 'comments', 'tags',)

class ISISInterfaceImportForm(NetBoxModelImportForm):
    instance = CSVModelChoiceField(
        queryset=ISISInstance.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Name of ISIS Instance')
    )
    interface = CSVModelChoiceField(
        queryset=Interface.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Name of interface')
    )

    class Meta:
        model = ISISInterface
        fields = ('instance', 'interface', 'metric', 'passive', 'description', 'comments', 'tags',)
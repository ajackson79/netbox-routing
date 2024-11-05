from django import forms
from django.utils.translation import gettext as _

from dcim.models import Interface, Device
from ipam.models import VRF
from netbox.forms import NetBoxModelFilterSetForm
from netbox_routing.choices import AuthenticationChoices
from utilities.forms import BOOLEAN_WITH_BLANK_CHOICES, add_blank_choice
from utilities.forms.fields import TagFilterField, DynamicModelMultipleChoiceField

from netbox_routing.models import ISISInstance, ISISInterface

from utilities.forms.rendering import FieldSet

__all__ = (
    'ISISInstanceFilterForm',
    'ISISInterfaceFilterForm',
)

class ISISInstanceFilterForm(NetBoxModelFilterSetForm):
    device = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        selector=True,
        label=_('Device'),
    )
    vrf = DynamicModelMultipleChoiceField(
        queryset=VRF.objects.all(),
        required=False,
        selector=True,
        label=_('VRF'),
    )
    model = ISISInstance
    fieldsets = (
        FieldSet('q', 'filter_id', 'tag', 'device', 'vrf', 'isis_type'),
    )
    tag = TagFilterField(model)

class ISISInterfaceFilterForm(NetBoxModelFilterSetForm):
    model = ISISInterface
    fieldsets = (
        FieldSet('q', 'filter_id', 'tag'),
        FieldSet('instance', name=_('ISIS')),
        FieldSet('interface', name=_('Device')),
        FieldSet('metric', 'priority', 'bfd', 'authentication', name=_('Attributes'))
    )
    device = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        selector=True,
        label=_('Device'),
    )
    vrf = DynamicModelMultipleChoiceField(
        queryset=VRF.objects.all(),
        required=False,
        selector=True,
        label=_('VRF'),
    )
    instance = DynamicModelMultipleChoiceField(
        queryset=ISISInstance.objects.all(),
        required=False,
        selector=True,
        label=_('Instance'),
    )
    interface = DynamicModelMultipleChoiceField(
        queryset=Interface.objects.all(),
        required=False,
        selector=True,
        label=_('Interface'),
    )
    passive = forms.NullBooleanField(
        required=False,
        label='Passive Interface',
        widget=forms.Select(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    bfd = forms.NullBooleanField(
        required=False,
        label='BFD Enabled',
        widget=forms.Select(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    metric = forms.IntegerField(
        required=False
    )
    priority = forms.IntegerField(
        required=False
    )
    authentication = forms.ChoiceField(
        choices=add_blank_choice(AuthenticationChoices),
        required=False
    )
    tag = TagFilterField(model)
from django import forms
from django.utils.translation import gettext as _

from dcim.models import Device
from ipam.models import VRF
from netbox.forms import NetBoxModelBulkEditForm
from utilities.forms import BOOLEAN_WITH_BLANK_CHOICES, add_blank_choice
from utilities.forms.fields import DynamicModelChoiceField, CommentField

from netbox_routing import choices
from netbox_routing.models import ISISInstance, ISISInterface

from utilities.forms.rendering import FieldSet

__all__ = (
    'ISISInterfaceBulkEditForm',
    'ISISInstanceBulkEditForm',
)

class ISISInstanceBulkEditForm(NetBoxModelBulkEditForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        label=_('Device'),
        required=False,
        selector=True
    )
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        label=_('VRF'),
        required=False,
        selector=True
    )

    description = forms.CharField(
        label=_('Description'),
        max_length=200,
        required=False
    )
    comments = CommentField()

    model = ISISInstance
    fieldsets = (
        FieldSet('device', 'vrf', 'net', name='ISIS'),
        FieldSet('description', ),
    )
    nullable_fields = ('vrf', 'description', )

class ISISInterfaceBulkEditForm(NetBoxModelBulkEditForm):
    instance = DynamicModelChoiceField(
        queryset=ISISInstance.objects.all(),
        label=_('ISIS Instance'),
        required=False,
        selector=True
    )
    cost = forms.IntegerField(label=_('Cost'), required=False)
    passive = forms.ChoiceField(label=_('Passive'), choices=BOOLEAN_WITH_BLANK_CHOICES, required=False)
    priority = forms.IntegerField(label=_('Priority'), required=False)
    bfd = forms.ChoiceField(label=_('BFD'), choices=BOOLEAN_WITH_BLANK_CHOICES, required=False)
    authentication = forms.ChoiceField(
        label=_('Authentication'),
        choices=add_blank_choice(choices.AuthenticationChoices),
        required=False
    )
    passphrase = forms.CharField(label=_('Passphrase'), required=False)

    description = forms.CharField(
        label=_('Description'),
        max_length=200,
        required=False
    )
    comments = CommentField()

    model = ISISInterface
    fieldsets = (
        FieldSet('instance', name='ISIS'),
        FieldSet('metric', 'passive', 'bfd', 'authentication', 'passphrase', name='Attributes'),
        FieldSet('description'),
    )
    nullable_fields = ()
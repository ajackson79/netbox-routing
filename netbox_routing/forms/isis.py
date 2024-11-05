from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from dcim.models import Interface, Device
from ipam.models import VRF
from netbox.forms import NetBoxModelForm
from utilities.forms import BOOLEAN_WITH_BLANK_CHOICES
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField, CommentField

from netbox_routing.models import ISISInstance, ISISInterface

__all__ = (
    'ISISInstanceForm',
    'ISISInterfaceForm',
)

class ISISInstanceForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
        selector=True,
        label=_('Device'),
    )
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        required=True,
        selector=True,
        label=_('VRF'),
    )
    comments = CommentField()

    class Meta:
        model = ISISInstance
        fields = ('name', 'device', 'net', 'vrf', 'description', 'comments', )

class ISISInterfaceForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        selector=True,
        label=_('Device'),
    )
    instance = DynamicModelChoiceField(
        queryset=ISISInstance.objects.all(),
        required=True,
        selector=True,
        label=_('Instance'),
        query_params={
            'device_id': '$device',
        }
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        required=True,
        selector=True,
        label=_('Interface'),
        query_params={
            'device_id': '$device',
        }
    )
    comments = CommentField()


    class Meta:
        model = ISISInterface
        fields = (
            'device', 'instance', 'interface', 'metric', 'passive', 'bfd', 'authentication', 'passphrase',
            'description', 'comments',
        )

        widgets = {
            'bfd': forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
            'passive': forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['device'] = self.instance.interface.device.pk

    def clean(self):
        super().clean()
        if self.cleaned_data.get('instance') and self.cleaned_data.get('interface'):
            if self.cleaned_data.get('instance').device != self.cleaned_data.get('interface').device:
                raise ValidationError(
                    {
                        'instance': _('ISIS Instance Device and Interface Device must match'),
                        'interface': _('ISIS Instance Device and Interface Device must match')
                    }
                )
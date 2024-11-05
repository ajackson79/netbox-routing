from ipam.models import VRF
from netbox.forms import NetBoxModelFilterSetForm
from netbox_routing.models import StaticRoute
from utilities.forms.fields import DynamicModelMultipleChoiceField, TagFilterField
from django.utils.translation import gettext as _

from utilities.forms.rendering import FieldSet
from django import forms


class StaticRouteFilterForm(NetBoxModelFilterSetForm):
    model = StaticRoute
    fieldsets = (
        FieldSet('q', 'filter_id', 'route_tag', 'tag', 'vrf'),
    )
    route_tag = forms.ChoiceField(
        choices=[
            (None, ''),
            (9999, 9999),
            (9993, 9993),
            (9666, 9666),
        ],
        required=False,
        label='Route Tag'
    )
    vrf = DynamicModelMultipleChoiceField(
        queryset=VRF.objects.all(),
        required=False,
        selector=True,
        label=_('VRF'),
    )
    tag = TagFilterField(model)
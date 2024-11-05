import django_filters
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext as _

from dcim.models import Device, Interface
from ipam.models import VRF
from utilities.filters import MultiValueCharFilter

from netbox.filtersets import NetBoxModelFilterSet
from netbox_routing.models import ISISInstance, ISISInterface


__all__ = (
    'ISISInstanceFilterSet',
    'ISISInterfaceFilterSet',
)

class ISISInstanceFilterSet(NetBoxModelFilterSet):
    device_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device',
        queryset=Device.objects.all(),
        label='Device (ID)',
    )
    device = django_filters.ModelMultipleChoiceFilter(
        field_name='device__name',
        queryset=Device.objects.all(),
        to_field_name='name',
        label='Device',
    )
    vrf_id = django_filters.ModelMultipleChoiceFilter(
        field_name='vrf',
        queryset=VRF.objects.all(),
        label='VRF (ID)',
    )
    vrf = django_filters.ModelMultipleChoiceFilter(
        field_name='vrf__name',
        queryset=VRF.objects.all(),
        to_field_name='name',
        label='VRF',
    )

    net = MultiValueCharFilter(
        method='filter_net',
        label=_('NET ID'),
    )

    class Meta:
        model = ISISInstance
        fields = ('device_id', 'device', 'name', 'vrf_id', 'vrf', 'net', 'isis_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value) |
            Q(device__name__icontains=value) |
            Q(net__icontains=value)
        )
        return queryset.filter(qs_filter).distinct()

    def filter_rid(self, queryset, name, value):
        try:
            return queryset.filter(**{f'{name}__in': value})
        except ValidationError:
            return queryset.none()
        
class ISISInterfaceFilterSet(NetBoxModelFilterSet):
    instance_id = django_filters.ModelMultipleChoiceFilter(
        field_name='instance',
        queryset=ISISInstance.objects.all(),
        label='Instance (ID)',
    )
    instance = django_filters.ModelMultipleChoiceFilter(
        field_name='instance__name',
        queryset=ISISInstance.objects.all(),
        to_field_name='name',
        label='Instance',
    )
    vrf_id = django_filters.ModelMultipleChoiceFilter(
        field_name='instance__vrf',
        queryset=VRF.objects.all(),
        label='VRF (ID)',
    )
    vrf = django_filters.ModelMultipleChoiceFilter(
        field_name='instance__vrf__name',
        queryset=VRF.objects.all(),
        to_field_name='name',
        label='VRF',
    )
    device_id = django_filters.ModelMultipleChoiceFilter(
        field_name='interface__device',
        queryset=Device.objects.all(),
        label='Device (ID)',
    )
    device = django_filters.ModelMultipleChoiceFilter(
        field_name='interface__device__name',
        queryset=Device.objects.all(),
        to_field_name='name',
        label='Device',
    )
    interface_id = django_filters.ModelMultipleChoiceFilter(
        field_name='interface',
        queryset=Interface.objects.all(),
        label='Area (ID)',
    )
    interface = django_filters.ModelMultipleChoiceFilter(
        field_name='interface__name',
        queryset=Interface.objects.all(),
        to_field_name='name',
        label='Area',
    )

    class Meta:
        model = ISISInterface
        fields = ('instance', 'interface', 'metric', 'passive', 'bfd', 'authentication', 'passphrase')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(instance__name__icontains=value) |
            Q(interface__name__icontains=value) |
            Q(interface__label__icontains=value) |
            Q(interface__device__name__icontains=value)
        )
        return queryset.filter(qs_filter).distinct()
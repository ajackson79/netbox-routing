from .static import StaticRouteFilterSet
from .objects import PrefixListFilterSet, PrefixListEntryFilterSet, RouteMapFilterSet, RouteMapEntryFilterSet
from .ospf import *
from .bgp import *
from .eigrp import *
from .isis import *


__all__ = (
    'StaticRouteFilterSet',

    'ISISInstanceFilterSet',
    'ISISInterfaceFilterSet',

    'BGPSettingFilterSet',
    'BGPRouterFilterSet',

    'OSPFInstanceFilterSet',
    'OSPFAreaFilterSet',
    'OSPFInterfaceFilterSet',
    'OSPFNetworksFilterSet',

    'EIGRPRouterFilterSet',
    'EIGRPAddressFamilyFilterSet',
    'EIGRPNetworkFilterSet',
    'EIGRPInterfaceFilterSet',

    'PrefixListFilterSet',
    'PrefixListEntryFilterSet',
    'RouteMapFilterSet',
    'RouteMapEntryFilterSet',
)

from .static import StaticRouteFilterForm
from .bgp import BGPRouterFilterForm, BGPScopeFilterForm, BGPAddressFamilyFilterForm, BGPSettingFilterForm
from .ospf import OSPFAreaFilterForm, OSPFInstanceFilterForm, OSPFInterfaceFilterForm, OSPFNetworksFilterForm
from .objects import PrefixListFilterForm, PrefixListEntryFilterForm, RouteMapFilterForm,\
    RouteMapEntryFilterForm
from .eigrp import *
from .isis import *

__all__ = (
    # Static
    'StaticRouteFilterForm',

    # ISIS
    'ISISInstanceFilterForm',
    'ISISInterfaceFilterForm',

    # BGP
    'BGPRouterFilterForm',
    'BGPScopeFilterForm',
    'BGPAddressFamilyFilterForm',
    'BGPSettingFilterForm',

    # EIGRP
    'EIGRPRouterFilterForm',
    'EIGRPAddressFamilyFilterForm',
    'EIGRPNetworkFilterForm',
    'EIGRPInterfaceFilterForm',

    # OSPF
    'OSPFAreaFilterForm',
    'OSPFInstanceFilterForm',
    'OSPFInterfaceFilterForm',
    'OSPFNetworksFilterForm',

    # Routing Objects
    'PrefixListFilterForm',
    'PrefixListEntryFilterForm',
    'RouteMapFilterForm',
    'RouteMapEntryFilterForm'
)

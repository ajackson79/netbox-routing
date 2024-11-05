from .static import StaticRouteViewSet
from .ospf import OSPFInstanceViewSet, OSPFAreaViewSet, OSPFInterfaceViewSet, OSPFNetworksViewSet
from .bgp import BGPRouterViewSet, BGPScopeViewSet, BGPAddressFamilyViewSet, BGPSettingViewSet
from .objects import PrefixListViewSet, PrefixListEntryViewSet, RouteMapViewSet, RouteMapEntryViewSet
from .eigrp import (
    EIGRPRouterViewSet, EIGRPAddressFamilyViewSet,
    EIGRPNetworkViewSet, EIGRPInterfaceViewSet
)
from .isis import ISISInstanceViewSet, ISISInterfaceViewSet

__all__ = (
    'StaticRouteViewSet',

    'ISISInstanceViewSet',
    'ISISInterfaceViewSet',

    'BGPRouterViewSet',
    'BGPScopeViewSet',
    'BGPAddressFamilyViewSet',
    'BGPSettingViewSet',

    'EIGRPRouterViewSet',
    'EIGRPAddressFamilyViewSet',
    'EIGRPNetworkViewSet',
    'EIGRPInterfaceViewSet',

    'OSPFInstanceViewSet',
    'OSPFAreaViewSet',
    'OSPFInterfaceViewSet',
    'OSPFNetworksViewSet',

    'PrefixListViewSet',
    'PrefixListEntryViewSet',
    'RouteMapViewSet',
    'RouteMapEntryViewSet',
)

from .static import StaticRoute
from .ospf import OSPFArea, OSPFInstance, OSPFInterface, OSPFNetworks
from .objects import PrefixList, PrefixListEntry, RouteMap, RouteMapEntry
from .bgp import BGPRouter, BGPScope, BGPAddressFamily, BGPSetting
from .eigrp import *
from .isis import *

__all__ = (
    'StaticRoute',

    'ISISInstance',
    'ISISInterface',

    'OSPFArea',
    'OSPFInstance',
    'OSPFInterface',
    'OSPFNetworks',

    'EIGRPRouter',
    'EIGRPAddressFamily',
    'EIGRPNetwork',
    'EIGRPInterface',

    'PrefixList',
    'PrefixListEntry',
    'RouteMap',
    'RouteMapEntry',

    # Not fully implemented
    'BGPRouter',
    'BGPScope',
    'BGPAddressFamily',
    'BGPSetting'
)

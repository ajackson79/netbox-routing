from .filtersets import *
from .bulk_edit import *
from .bulk_import import *
from .objects import PrefixListForm, PrefixListEntryForm, RouteMapForm, RouteMapEntryForm
from .ospf import OSPFAreaForm, OSPFInstanceForm, OSPFInterfaceForm, OSPFNetworksForm
from .bgp import BGPRouterForm, BGPScopeForm, BGPAddressFamilyForm
from .static import StaticRouteForm
from .eigrp import *
from .isis import *

__all__ = (
    
    # Static Routes
    'StaticRouteForm',
    'StaticRouteFilterForm',

    # ISIS
    'ISISInstanceForm',
    'ISISInstanceImportForm',
    'ISISInstanceBulkEditForm',
    'ISISInstanceFilterForm',

    'ISISInterfaceForm',
    'ISISInterfaceImportForm',
    'ISISInterfaceBulkEditForm',
    'ISISInterfaceFilterForm',

    # OSPF
    'OSPFAreaForm',
    'OSPFAreaBulkEditForm',
    'OSPFAreaImportForm',
    'OSPFAreaFilterForm',

    'OSPFInstanceForm',
    'OSPFInstanceBulkEditForm',
    'OSPFInstanceFilterForm',
    'OSPFInstanceImportForm',

    'OSPFInterfaceForm',
    'OSPFInterfaceFilterForm',
    'OSPFInterfaceBulkEditForm',
    'OSPFInterfaceImportForm',

    'OSPFNetworksForm',
    'OSPFNetworksFilterForm',
    'OSPFNetworksBulkEditForm',
    'OSPFNetworksImportForm',


    # EIGRP
    'EIGRPRouterForm',
    'EIGRPRouterBulkEditForm',
    'EIGRPRouterFilterForm',
    'EIGRPRouterImportForm',

    'EIGRPAddressFamilyForm',
    'EIGRPAddressFamilyBulkEditForm',
    'EIGRPAddressFamilyFilterForm',
    'EIGRPAddressFamilyImportForm',

    'EIGRPNetworkForm',
    'EIGRPNetworkBulkEditForm',
    'EIGRPNetworkFilterForm',
    'EIGRPNetworkImportForm',

    'EIGRPInterfaceForm',
    'EIGRPInterfaceBulkEditForm',
    'EIGRPInterfaceFilterForm',
    'EIGRPInterfaceImportForm',

    # BGP
    'BGPRouterForm',
    'BGPScopeForm',
    'BGPAddressFamilyForm',
    'BGPRouterFilterForm',
    'BGPScopeFilterForm',
    'BGPAddressFamilyFilterForm',
    'BGPSettingFilterForm',

    # Objects
    'PrefixListForm',
    'PrefixListEntryForm',
    'RouteMapForm',
    'RouteMapEntryForm',
    'PrefixListFilterForm',
    'PrefixListEntryFilterForm',
    'RouteMapFilterForm',
    'RouteMapEntryFilterForm'
)

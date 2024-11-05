from .static import *

from .objects import PrefixListView, PrefixListEditView, PrefixListListView, PrefixListDeleteView, RouteMapListView, \
    RouteMapView, RouteMapEditView, RouteMapDeleteView, PrefixListEntryListView, PrefixListEntryEditView, \
    PrefixListEntryDeleteView, PrefixListEntryView, RouteMapEntryListView, RouteMapEntryView, RouteMapEntryEditView, \
    RouteMapEntryDeleteView, PrefixListEntriesView, RouteMapEntriesView, RouteMapEntryBulkEditView, \
    RouteMapEntryBulkDeleteView, PrefixListEntryBulkDeleteView, PrefixListEntryBulkEditView

from .ospf import *
from .eigrp import *
from .bgp import *
from .core import *
from .isis import *

__all__ = (
    # Core View Extensions
    'DeviceStaticRoutesView',

    # Static
    'StaticRouteListView',
    'StaticRouteView',
    'StaticRouteDevicesView',
    'StaticRouteEditView',
    'StaticRouteBulkEditView',
    'StaticRouteDeleteView',
    'StaticRouteBulkDeleteView',

    # ISIS
    'ISISInstanceListView',
    'ISISInstanceView',
    'ISISInstanceEditView',
    'ISISInstanceDeleteView',
    'ISISInstanceInterfacesView',

    'ISISInterfaceListView',
    'ISISInterfaceView',
    'ISISInterfaceEditView',
    'ISISInterfaceDeleteView',

    # OSPF
    'OSPFInstanceListView',
    'OSPFInstanceView',
    'OSPFInstanceEditView',
    'OSPFInstanceDeleteView',
    'OSPFInstanceInterfacesView',
    'OSPFInstanceNetworksView',

    'OSPFAreaListView',
    'OSPFAreaView',
    'OSPFAreaInterfacesView',
    'OSPFAreaEditView',
    'OSPFAreaDeleteView',

    'OSPFInterfaceListView',
    'OSPFInterfaceView',
    'OSPFInterfaceEditView',
    'OSPFInterfaceDeleteView',

    'OSPFNetworksListView',
    'OSPFNetworksView',
    'OSPFNetworksEditView',
    'OSPFNetworksBulkEditView',
    'OSPFNetworksDeleteView',
    'OSPFNetworksBulkDeleteView',

    # EIGRP
    'EIGRPRouterListView',
    'EIGRPRouterView',
    'EIGRPRouterInterfacesView',
    'EIGRPRouterEditView',
    'EIGRPRouterImportView',
    'EIGRPRouterBulkEditView',
    'EIGRPRouterDeleteView',
    'EIGRPRouterBulkDeleteView',

    'EIGRPAddressFamilyListView',
    'EIGRPAddressFamilyView',
    'EIGRPAddressFamilyInterfacesView',
    'EIGRPAddressFamilyEditView',
    'EIGRPAddressFamilyBulkEditView',
    'EIGRPAddressFamilyDeleteView',
    'EIGRPAddressFamilyBulkDeleteView',

    'EIGRPNetworkListView',
    'EIGRPNetworkView',
    'EIGRPNetworkEditView',
    'EIGRPNetworkBulkEditView',
    'EIGRPNetworkDeleteView',
    'EIGRPNetworkBulkDeleteView',

    'EIGRPInterfaceListView',
    'EIGRPInterfaceView',
    'EIGRPInterfaceEditView',
    'EIGRPInterfaceBulkEditView',
    'EIGRPInterfaceDeleteView',
    'EIGRPInterfaceBulkDeleteView',

    'BGPRouterView',
    'BGPRouterEditView',

    # Routing Objects
    'PrefixListListView',
    'PrefixListView',
    'PrefixListEntriesView',
    'PrefixListEditView',
    'PrefixListDeleteView',
    'PrefixListEntryListView',
    'PrefixListEntryView',
    'PrefixListEntryEditView',
    'PrefixListEntryDeleteView',
    'PrefixListEntryBulkEditView',
    'PrefixListEntryBulkDeleteView',

    'RouteMapListView',
    'RouteMapView',
    'RouteMapEntriesView',
    'RouteMapEditView',
    'RouteMapDeleteView',
    'RouteMapEntryListView',
    'RouteMapEntryView',
    'RouteMapEntryEditView',
    'RouteMapEntryDeleteView',
    'RouteMapEntryBulkEditView',
    'RouteMapEntryBulkDeleteView',

)

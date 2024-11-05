from .static import *
from .objects import *
from .ospf import *
from .eigrp import *
from .isis import *


__all__ = (
    # Staticroute
    'StaticRouteBulkEditForm',

    # ISIS
    'ISISInterfaceBulkEditForm',
    'ISISInstanceBulkEditForm',

    # OSPF
    'OSPFInstanceBulkEditForm',
    'OSPFInterfaceBulkEditForm',
    'OSPFAreaBulkEditForm',
    'OSPFNetworksBulkEditForm',

    # EIGRP
    'EIGRPRouterBulkEditForm',
    'EIGRPAddressFamilyBulkEditForm',
    'EIGRPNetworkBulkEditForm',
    'EIGRPInterfaceBulkEditForm',

    # Route Objects
    'PrefixListEntryBulkEditForm',
    'RouteMapEntryBulkEditForm'
)


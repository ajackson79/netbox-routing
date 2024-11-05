from netbox.search import SearchIndex, register_search
from .models import *

@register_search
class StaticRouteListIndex(SearchIndex):
    model = StaticRoute
    fields = (
        ('comments', 5000),
        ('prefix', 100),
        ('next_hop', 100),
        ('route_tag', 100),
        ('description', 200),
        ('name', 100),
    )

@register_search
class ISISInstanceListIndex(SearchIndex):
    model = ISISInstance
    fields = (
        ('name', 100),
        ('comments', 5000),
        ('net', 100),
        ('isis_type', 100),
    )

@register_search
class ISISInterfaceListIndex(SearchIndex):
    model = ISISInterface
    fields = (
        ('comments', 5000),
        ('instance', 100),
    )
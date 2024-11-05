from netbox.choices import ButtonColorChoices
from netbox.plugins import PluginMenuItem, PluginMenuButton

__all__ = (
    'MENUITEMS',
)

isis_instance = PluginMenuItem(
    link='plugins:netbox_routing:isisinstance_list',
    link_text='Instances',
    permissions=['netbox_routing.view_isisinstance'],
    buttons=(
        PluginMenuButton('plugins:netbox_routing:isisinstance_add', 'Add', 'mdi mdi-plus', ButtonColorChoices.GREEN),
        PluginMenuButton(
            'plugins:netbox_routing:isisinstance_import',
            'Import',
            'mdi mdi-upload',
            ButtonColorChoices.CYAN
        ),
    )
)

isis_interfaces = PluginMenuItem(
    link='plugins:netbox_routing:isisinterface_list',
    link_text='Interfaces',
    permissions=['netbox_routing.view_isisinterface'],
    buttons=(
        PluginMenuButton('plugins:netbox_routing:isisinterface_add', 'Add', 'mdi mdi-plus', ButtonColorChoices.GREEN),
        PluginMenuButton(
            'plugins:netbox_routing:isisinterface_import',
            'Import',
            'mdi mdi-upload',
            ButtonColorChoices.CYAN
        ),
    )
)

MENUITEMS = (isis_instance, isis_interfaces)
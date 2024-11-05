# Generated by Django 5.0.9 on 2024-10-27 13:20

import netbox_routing.fields.ip
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_routing', '0019_remove_ospfinstance_netbox_routing_ospfinstance_unique_ospfinstance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ospfinstance',
            name='router_id',
            field=netbox_routing.fields.ip.IPAddressField(unique=True),
        ),
    ]
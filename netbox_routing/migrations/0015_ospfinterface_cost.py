# Generated by Django 5.0.9 on 2024-10-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_routing', '0014_alter_ospf_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='ospfinterface',
            name='cost',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]

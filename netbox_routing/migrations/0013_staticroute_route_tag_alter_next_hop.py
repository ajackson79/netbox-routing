# Generated by Django 5.0.9 on 2024-10-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    
    dependencies = [
        ('netbox_routing', '0012_osfp_instance_vrf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticroute',
            name='next_hop',
            field=models.CharField(max_length=15),
        ),
        migrations.AddField(
            model_name='staticroute',
            name='route_tag',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
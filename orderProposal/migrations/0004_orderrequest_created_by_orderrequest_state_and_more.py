# Generated by Django 4.0.3 on 2022-04-12 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orderProposal', '0003_alter_devicedata_order_alter_sensordata_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrequest',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'role': 3}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderrequest',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Placed'), (2, 'Accepted'), (3, 'Ready'), (4, 'Dispatched'), (5, 'Delivered')], default=1),
        ),
        migrations.AlterField(
            model_name='orderrequest',
            name='customer',
            field=models.ForeignKey(limit_choices_to={'role': 5}, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]

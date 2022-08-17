# Generated by Django 4.1 on 2022-08-14 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ticketing', '0003_alter_ticket_closed_on_alter_ticket_time_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='closed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.4 on 2023-03-09 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0019_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='on_display',
            field=models.BooleanField(default=False, unique=True),
        ),
    ]

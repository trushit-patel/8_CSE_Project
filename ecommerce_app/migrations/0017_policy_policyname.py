# Generated by Django 3.2.4 on 2023-03-08 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0016_auto_20230308_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='policyName',
            field=models.CharField(default='thisPolicy', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
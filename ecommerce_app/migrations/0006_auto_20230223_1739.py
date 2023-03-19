# Generated by Django 3.2.4 on 2023-02-23 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce_app', '0005_auto_20230223_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cc', 'Credit Card'), ('dc', 'Debit Card'), ('pp', 'PayPal'), ('st', 'Stripe'), ('ap', 'Apple Pay'), ('gp', 'Google Pay'), ('up', 'UPI')], default=True, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.CreateModel(
            name='CheckOutDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=191)),
                ('last_name', models.CharField(max_length=191)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=191)),
                ('city', models.CharField(max_length=255)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip_code', models.CharField(max_length=20)),
                ('phn', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

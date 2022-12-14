# Generated by Django 4.0.6 on 2022-10-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=20000)),
                ('name', models.CharField(max_length=20000)),
                ('email', models.CharField(max_length=20000)),
                ('address', models.CharField(max_length=20000)),
                ('city', models.CharField(max_length=20000)),
                ('state', models.CharField(max_length=20000)),
                ('zip_code', models.CharField(max_length=20000)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
    ]

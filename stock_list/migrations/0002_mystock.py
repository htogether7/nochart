# Generated by Django 4.0.3 on 2022-10-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mystock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('symbol', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'mystock',
                'managed': False,
            },
        ),
    ]
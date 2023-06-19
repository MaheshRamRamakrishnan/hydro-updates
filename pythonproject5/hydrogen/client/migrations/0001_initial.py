# Generated by Django 4.0.8 on 2022-12-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client1_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phonenumber', models.PositiveBigIntegerField(null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2024-03-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300)),
                ('lastname', models.CharField(max_length=200)),
                ('userid', models.CharField(max_length=200)),
                ('password', models.IntegerField()),
                ('mblenum', models.BigIntegerField()),
                ('email', models.EmailField(max_length=400, null=True)),
            ],
        ),
    ]

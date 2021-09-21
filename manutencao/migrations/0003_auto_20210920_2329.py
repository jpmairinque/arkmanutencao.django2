# Generated by Django 2.2.24 on 2021-09-20 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0002_auto_20210920_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('fabricante', models.CharField(max_length=100, null=True)),
                ('modelo', models.CharField(max_length=100, null=True)),
                ('patrimonio', models.CharField(max_length=100, null=True)),
                ('numero_serie', models.CharField(max_length=100, null=True)),
                ('proprietario', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Empresa',
            new_name='Company',
        ),
    ]
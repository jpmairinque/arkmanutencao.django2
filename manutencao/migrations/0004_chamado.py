# Generated by Django 2.2.24 on 2021-09-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0003_auto_20210920_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('numero', models.IntegerField(null=True)),
                ('equipamento_id', models.IntegerField()),
                ('responsavel_str', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]

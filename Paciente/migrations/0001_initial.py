# Generated by Django 5.0.2 on 2024-02-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cui', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
        migrations.AddConstraint(
            model_name='paciente',
            constraint=models.UniqueConstraint(fields=('cui', 'name'), name='unique_cui_name'),
        ),
    ]

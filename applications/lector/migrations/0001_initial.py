# Generated by Django 4.2.1 on 2024-05-24 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Lector',
                'verbose_name_plural': 'Lectores',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('devuelto', models.BooleanField()),
                ('lector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lector.lector')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_prestamo', to='libro.libro')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-07-05 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_alter_libro_categoria'),
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_prestamo', to='libro.libro'),
        ),
    ]

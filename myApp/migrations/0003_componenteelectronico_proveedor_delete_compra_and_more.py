# Generated by Django 4.2.7 on 2023-12-05 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_usuario_correo_remove_usuario_direccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponenteElectronico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('numero_de_serie', models.CharField(max_length=50, unique=True)),
                ('cantidad_disponible', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_de_ingreso', models.DateField(auto_now_add=True)),
                ('fecha_de_modificacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='Informe',
        ),
        migrations.RemoveField(
            model_name='resena',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Resena',
        ),
        migrations.AddField(
            model_name='componenteelectronico',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.proveedor'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-12-20 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.CharField(max_length=50)),
                ('Contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Producto', models.CharField(max_length=50)),
                ('Precio', models.PositiveIntegerField()),
                ('Stock', models.PositiveIntegerField()),
                ('Material', models.CharField(max_length=50)),
                ('Alto', models.PositiveIntegerField()),
                ('Ancho', models.PositiveIntegerField()),
                ('Largo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad_Productos', models.PositiveIntegerField()),
                ('Total', models.PositiveIntegerField()),
                ('Fecha', models.DateField()),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiendaMueblesApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_usuario', models.CharField(max_length=50)),
                ('Rut', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiendaMueblesApp.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiendaMueblesApp.venta')),
            ],
        ),
        migrations.CreateModel(
            name='imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ruta', models.ImageField(upload_to='static/images/')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiendaMueblesApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Archivo_Complementario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ruta', models.ImageField(upload_to='static/images/')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiendaMueblesApp.producto')),
            ],
        ),
    ]

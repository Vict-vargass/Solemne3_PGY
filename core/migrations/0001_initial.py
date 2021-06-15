# Generated by Django 3.2.3 on 2021-06-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='obrasPublicadas',
            fields=[
                ('idObra', models.IntegerField(primary_key=True, serialize=False, verbose_name='id obra')),
                ('nombreObra', models.CharField(max_length=40, verbose_name='nombre obra')),
                ('historia', models.TextField(max_length=3000, verbose_name='historia obra')),
                ('descripcion', models.TextField(max_length=1000, verbose_name='descripcion obra')),
                ('precio', models.CharField(max_length=100, verbose_name='precio obra')),
                ('tecnicaUsada', models.TextField(max_length=1000, verbose_name='tecnica usada obra')),
            ],
        ),
        migrations.CreateModel(
            name='solicitudesContacto',
            fields=[
                ('idSolicitud', models.IntegerField(primary_key=True, serialize=False, verbose_name='id solicitud')),
                ('nombreSolicitante', models.CharField(max_length=60, verbose_name='nombre solicitante')),
                ('correo', models.EmailField(max_length=60, verbose_name='correo solicitante')),
                ('run', models.CharField(max_length=25, verbose_name='run solicitante')),
                ('pasaporte', models.CharField(max_length=25, verbose_name='pasaporte solicitante')),
                ('celular', models.CharField(max_length=20, null=True, verbose_name='celular solicitante')),
                ('ciudad', models.CharField(max_length=40, verbose_name='ciudad solicitante')),
                ('mensaje', models.TextField(max_length=500, verbose_name='mensaje solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='solicitudObra',
            fields=[
                ('idSolicitudObra', models.IntegerField(primary_key=True, serialize=False, verbose_name='id solicitud obra')),
                ('nombreObra', models.CharField(max_length=40, verbose_name='nombre obra')),
                ('historia', models.TextField(max_length=3000, verbose_name='historia obra')),
                ('descripcion', models.TextField(max_length=1000, verbose_name='descripcion obra')),
                ('precio', models.CharField(max_length=100, verbose_name='precio obra')),
                ('tecnicaUsada', models.TextField(max_length=1000, verbose_name='tecnica usada obra')),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='id usuario')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='nombre usuario')),
                ('emailUsuario', models.EmailField(max_length=60, unique=True, verbose_name='email usuario')),
                ('contraseñaUsuario', models.CharField(max_length=20, verbose_name='contraseña')),
            ],
        ),
    ]
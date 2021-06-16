# Generated by Django 3.2.3 on 2021-06-15 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaObras',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id categoria')),
                ('nombreCategoria', models.CharField(max_length=20, verbose_name='Categoria obra')),
            ],
        ),
        migrations.AddField(
            model_name='solicitudobra',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.categoriaobras'),
            preserve_default=False,
        ),
    ]
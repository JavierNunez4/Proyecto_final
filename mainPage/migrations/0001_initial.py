# Generated by Django 4.2.4 on 2023-11-29 01:42

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rol', models.IntegerField(default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Detalle_Pedido',
                'verbose_name_plural': 'Detalle_Pedidos',
                'db_table': 'pedidos_detalle',
            },
        ),
        migrations.CreateModel(
            name='Propietarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePyme', models.CharField(max_length=30)),
                ('datosPropietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
                'db_table': 'propietarios',
            },
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_solicitud', models.DateField(auto_now_add=True, null=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('categoria', models.CharField(default=None, max_length=60)),
                ('nombrePyme', models.CharField(max_length=100)),
                ('solicitud', models.CharField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to='logoPymesSoli')),
                ('idSolicitante', models.IntegerField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
                'db_table': 'solicitudes',
            },
        ),
        migrations.CreateModel(
            name='Pymes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePyme', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60)),
                ('categoria', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to='logoPymes')),
                ('propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainPage.propietarios')),
            ],
            options={
                'verbose_name': 'Pymes',
                'verbose_name_plural': 'Pymes',
                'db_table': 'pymes',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=35)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenesT')),
                ('pymeAsociada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainPage.pymes')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('productos', models.ManyToManyField(through='mainPage.ItemPedido', to='mainPage.productos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedidos',
            },
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.productos'),
        ),
    ]

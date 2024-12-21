# filepath: /c:/Users/Piotr/Desktop/Python/Inzynierka/bookstore/app_users/migrations/0002_create_order_manager_group.py
from django.db import migrations

def create_order_manager_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Create the group
    order_manager_group, created = Group.objects.get_or_create(name='Order Manager')

    # Assign permissions to the group
    permissions = Permission.objects.filter(codename__in=[
        'can_view_orders',
        'can_confirm_completion',
        'can_ship_orders',
    ])
    order_manager_group.permissions.set(permissions)
    order_manager_group.save()

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_order_manager_group),
    ]
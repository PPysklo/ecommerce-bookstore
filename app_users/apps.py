# filepath: /c:/Users/Piotr/Desktop/Python/Inzynierka/bookstore/app_users/apps.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AppUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_users'
    verbose_name = "Użytkownicy"

    def ready(self):
        post_migrate.connect(self.create_order_manager_group, sender=self)

    @staticmethod
    def create_order_manager_group(sender, **kwargs):
        from django.apps import apps
        Group = apps.get_model('auth', 'Group')
        Permission = apps.get_model('auth', 'Permission')

        # Tworzenie grupy
        order_manager_group, created = Group.objects.get_or_create(name='Order Manager')
        
        # Przypisywanie uprawnień
        permissions = Permission.objects.filter(codename__in=[
            'can_change_order',
            'can_delete_order',
            'can_view_order',
            'can_change_order_item',
            'can_delete_order_item',
            'can_view_order_item',
            'can_add_shipping_address',
            'can_change_shipping_address',
            'can_view_shipping_address',
        ])
        
        order_manager_group.permissions.set(permissions)
        order_manager_group.save()

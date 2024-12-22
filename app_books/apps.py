from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AppBooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_books'
    verbose_name = "Zamówienia"

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
        # print(Permission.objects.all())
        permissions = Permission.objects.filter(codename__in=[
            'change_order',
            'delete_order',
            'view_order',
            'change_orderitem',
            'delete_orderitem',
            'view_orderitem',
            'add_shippingaddress',
            'change_shippingaddress',
            'view_shippingaddress',
        ])
        
        order_manager_group.permissions.set(permissions)
        order_manager_group.save()
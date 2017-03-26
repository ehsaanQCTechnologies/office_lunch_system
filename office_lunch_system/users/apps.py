from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'office_lunch_system.users'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Creates default groups and assigns permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        editors, _ = Group.objects.get_or_create(name='Editors')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Get permissions
        perm_view = Permission.objects.get(codename='can_view')
        perm_create = Permission.objects.get(codename='can_create')
        perm_edit = Permission.objects.get(codename='can_edit')
        perm_delete = Permission.objects.get(codename='can_delete')

        # Assign permissions to groups
        viewers.permissions.set([perm_view])
        editors.permissions.set([perm_view, perm_create, perm_edit])
        admins.permissions.set([perm_view, perm_create, perm_edit, perm_delete])

        self.stdout.write(self.style.SUCCESS("Groups & permissions created successfully!"))

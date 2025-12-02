# netbox/netbox/netbox/custom_pipeline.py
# Sync groups from Keycloak

from django.contrib.auth.models import Group

class AuthFailed(Exception):
    """Custom Auth Exception"""
    pass

def set_role(response, user, backend, *args, **kwargs):
    """
    Get roles from JWT
    Assign user to netbox group matching role
    Also set is_superuser or is_staff for special roles 'superusers' and 'staff'
    """
    try:
        # get roles from 'roles' JWT field
        roles = response['roles']
    except KeyError:
        # if no 'roles' field in JWT
        # clear user groups
        user.groups.clear()
        raise AuthFailed("No role assigned")

    try:
        # reset privileges
        user.is_superuser = False
        user.is_staff = False

        # set privileges
        for role in roles:
            # netbox superuser
            if role == 'netbox_admins':
                user.is_superuser = True
                user.save()
                continue
            # netbox staff
            if role == "netbox_users":
                user.is_staff = True
                user.save()
                continue

            # add to existed groups, uncomment if needed
            #group, created = Group.objects.get_or_create(name=role)
            #group.user_set.add(user)
    except Group.DoesNotExist:
        pass

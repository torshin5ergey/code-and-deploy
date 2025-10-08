# docker/extra_settings/local_settings.py

from dojo.settings import *

def keycloak_groups_sync(backend, details, response, user=None, *args, **kwargs):
    if backend.name != "keycloak" or not user:
        return
    from dojo.models import Dojo_Group, Dojo_User, Dojo_Group_Member, Role
    from dojo.authorization.roles_permissions import Roles
    from dojo.group.utils import get_auth_group_name
    from django.contrib.auth.models import User

    print(f"[Keycloak Groups Sync] Groups sync for user {user} started")
    # get user groups from access token
    keycloak_groups = response.get("groups", [])
    print(f"[Keycloak Groups Sync] Groups from Keycloak for user {user}: {keycloak_groups}")
    django_user = User.objects.get(username=response.get("preferred_username"))

    for group_name in keycloak_groups:
        # if the group exist
        try:
            group = Dojo_Group.objects.get(name=group_name, social_provider="Keycloak")
            print(f"[Keycloak Groups Sync] Group {group_name} found in DefectDojo")

            # Add the user as Maintainer
            maintainer_role = Role.objects.get(id=Roles.Maintainer)
            group_member, added = Dojo_Group_Member.objects.get_or_create(
                group=group,
                user=user,
                defaults={'role': maintainer_role}
            )
            if added:
                print(f"[Keycloak Groups Sync] User {user} added to the group {group_name} as Maintainer")
            else:
                print(f"[Keycloak Gorups Sync] User {user} already member of group {group_name}")

        except Dojo_Group.DoesNotExist:
            print(f"[Keycloak Groups Sync] Group {group_name} not found in DefectDojo")
            continue

    # cleanup old groups for user
    for group_member in Dojo_Group_Member.objects.select_related("group").filter(user=user):
        group = group_member.group
        if str(group) not in keycloak_groups:
            group_member.delete()
            print(f"[Keycloak Groups Sync] User {user} deleted from group {str(group)}")

    print(f"[Keycloak Groups Sync] Groups sync from Keycloak for User {user} completed successfully"
)

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "dojo.pipeline.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "dojo.pipeline.create_user",
    "dojo.pipeline.modify_permissions",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
    "dojo.pipeline.update_azure_groups",
    "dojo.pipeline.update_product_access",
    "dojo.settings.local_settings.keycloak_groups_sync", #
)

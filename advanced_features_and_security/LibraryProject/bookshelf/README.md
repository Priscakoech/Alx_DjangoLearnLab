# Permissions and Groups in the Application

## Permissions
The application uses the following custom permissions:
- `can_view`: Allows viewing documents.
- `can_create`: Allows creating new documents.
- `can_edit`: Allows editing existing documents.
- `can_delete`: Allows deleting documents.

## Groups
The following groups are configured:
- **Viewers**: Assigned the `can_view` permission.
- **Editors**: Assigned the `can_create` and `can_edit` permissions.
- **Admins**: Assigned all permissions.

## Enforcing Permissions
Permissions are enforced using Django's `@permission_required` decorator in the views. Users attempting unauthorized actions will see an error message.

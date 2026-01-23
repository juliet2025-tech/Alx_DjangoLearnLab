# Permissions and Groups Setup

This project uses Django's permissions and groups system to control access.

## Custom Permissions
Defined in `relationship_app/models.py`:

- `can_view` - view relationship
- `can_create` - create relationship
- `can_edit` - edit relationship
- `can_delete` - delete relationship

## Groups

- **Viewers:** can_view
- **Editors:** can_view, can_create, can_edit
- **Admins:** can_view, can_create, can_edit, can_delete

## Enforcement

Permissions are enforced in views using `@permission_required` decorators.

Unauthorized users receive a 403 Forbidden response.

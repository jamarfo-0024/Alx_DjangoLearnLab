# Permissions and Groups Configuration

This project uses Django permissions to restrict access to book management.

## Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Custom Model Permissions:
Defined in Book model:

- can_view
- can_create
- can_edit
- can_delete

## Enforcement in Views:
Access is restricted using @permission_required decorator.

Example:
@permission_required('bookshelf.can_edit', raise_exception=True)

## Testing:
1. Create users and groups via Django Admin.
2. Assign permissions to groups.
3. Assign users to groups.
4. Log in as different users to verify access control.

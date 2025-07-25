# Permissions & Groups Setup

## Custom Permissions

Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups

Created via Django Admin:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: All permissions

## Enforcement

In `views.py`, we used `@permission_required` decorators to lock down views based on the above permissions.

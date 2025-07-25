# LibraryProject - Permissions and Groups Management

## Overview

This Django project demonstrates managing custom permissions and user groups to control access to different features of the application. The permissions are tied to the `Book` model in the `bookshelf` app.

---

## Custom Permissions

Defined in `bookshelf/models.py` under the `Book` model:

- `can_create` – Allows a user to create new book entries.
- `can_delete` – Allows a user to delete book entries.

These permissions are declared using the `Meta` class of the model.

---

## User Groups

The following user groups were created using the Django admin:

- **Admins**: All permissions (`can_create`, `can_delete`, etc.)
- **Editors**: Only `can_create` permission
- **Viewers**: No special permissions, just view access

Permissions were assigned to groups via the admin interface.

---

## Permission Enforcement in Views

Views in `bookshelf/views.py` use the `@permission_required` decorator to enforce access control.

Example:
```python
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    ...

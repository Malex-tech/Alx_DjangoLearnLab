# LibraryProject

## Overview

This Django project demonstrates how to implement and manage custom user permissions and groups using Django's built-in auth system. The `bookshelf` app contains the core models and views for managing books and enforcing access control.

## Permissions

The `Book` model in `bookshelf/models.py` has two custom permissions:
- `can_create`: Allows users to add new books.
- `can_delete`: Allows users to delete existing books.

## User Groups

Created via the Django admin panel:
- **Admins**: Full access (`can_create`, `can_delete`)
- **Editors**: Only `can_create`
- **Viewers**: No special permissions

## Views Protection

Permissions are enforced in views using the `@permission_required` decorator. For example:

```python

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    ...

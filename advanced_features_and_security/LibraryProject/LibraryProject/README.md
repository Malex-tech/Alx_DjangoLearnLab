## Django Advanced Features and Security: Permissions & Groups Setup

## Overview

This project demonstrates Django’s built-in user authentication system with a focus on **permissions**, **groups**, and **role-based access control**. The goal is to restrict or allow access to certain views and actions based on user roles, using Django's native security features.

## 🔐 Permissions Configuration

Django allows assigning granular permissions to models and custom actions. In this project:

- **Model-level permissions** (Add, Change, Delete, View) are auto-generated for each model.
- **Custom permissions** were added using the `Meta` class in the model:
  
  
  class Document(models.Model):
      ...
      class Meta:
          permissions = [
              ("can_approve_document", "Can approve documents"),
              ("can_reject_document", "Can reject documents"),
          ]


👥 Groups Usage
Groups were created to simplify permission management by role.

Example Groups:
Admin: Has all permissions including approve/reject.

Editor: Can add/change documents but cannot approve.

Viewer: Can only view documents.

Assigned Programmatically (sample):

from django.contrib.auth.models import Group, Permission

admin_group = Group.objects.get(name='Admin')
perm = Permission.objects.get(codename='can_approve_document')
admin_group.permissions.add(perm)

✅ Usage in Views
Permissions are enforced in views using decorators and permission mixins:

Function-Based Views

from django.contrib.auth.decorators import permission_required

@permission_required('app.can_approve_document')
def approve_document(request, doc_id):

Class-Based Views

from django.contrib.auth.mixins import PermissionRequiredMixin

class DocumentApproveView(PermissionRequiredMixin, View):
    permission_required = 'app.can_approve_document'
    
🛠️ Admin Configuration
Permissions and groups are managed in Django’s Admin Interface:

Go to /admin/

Navigate to Groups

Add or update group permissions

Assign users to appropriate groups

🧪 Testing Roles and Permissions
To verify the system:

Log in as a user in each group.

Attempt actions like creating, viewing, approving documents.

Unauthorized actions are blocked and redirected or denied with 403 Forbidden.

🔍 Summary
Role	View	Add	Change	Approve	Reject
Admin	✅	✅	✅	✅	✅
Editor	✅	✅	✅	❌	❌
Viewer	✅	❌	❌	❌	❌

📎 References
Django Permissions Docs

Django Group Permissions

✍️ Author
Alex Alexander
Project: advanced_features_and_security
Repo: https://github.com/Malex-tech/Alx_DjangoLearnLab

✅ Next Steps:
- Replace `"app"` in the permission strings with your actual app name.
- If you’ve got screenshots of the admin panel or group settings, upload them and embed like:
  ```markdown
  
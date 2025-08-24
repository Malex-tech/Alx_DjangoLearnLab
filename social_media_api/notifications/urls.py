from django.urls import path
from .views import (
    NotificationListView,
    UnreadNotificationListView,
    MarkNotificationReadView,
    MarkAllReadView,
)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('unread/', UnreadNotificationListView.as_view(), name='notifications-unread'),
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='notification-read'),
    path('read-all/', MarkAllReadView.as_view(), name='notifications-read-all'),
]

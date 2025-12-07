from django.urls import path
from .views import AccountSettingsView

urlpatterns = [
    path("account/", AccountSettingsView.as_view(), name="account-settings"),
]

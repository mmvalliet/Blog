from django.urls import path
from .views import UserProfileView,EditProfile

app_name="cuentas"

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="profile"),
    path('profile/edit', EditProfile, name="edit-profile")
]
from django.urls import path
from .views import SingUpView, ProfileUpdate

urlpatterns = [
    path('signup/', SingUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
]
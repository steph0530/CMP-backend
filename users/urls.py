from django.urls import path

from users.api import(
    # Auth
    LoginAPI,
    # Registration
    RegistrationAPI,
    # Users
    UpdateUserAPI,
)

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('new/', RegistrationAPI.as_view()),
    path('user/<uuid>/',UpdateUserAPI.as_view()),
]
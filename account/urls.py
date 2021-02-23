from django.urls import path

from account.views import RegistrationView, SuccessfulRegistrationView, ActivationView, SigninView, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('successul_registration/', SuccessfulRegistrationView.as_view, name='successful-registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login/', SigninView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
]
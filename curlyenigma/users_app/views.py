from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'app_users/login.html'


class CustomLogoutView(LogoutView):
    pass

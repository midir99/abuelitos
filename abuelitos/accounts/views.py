from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"


login_view = LoginView.as_view()


class LogoutView(auth_views.LogoutView):
    template_name = "accounts/logged_out.html"


logout_view = LogoutView.as_view()


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "accounts/password_change_form.html"


password_change_view = PasswordChangeView.as_view()


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


password_change_done_view = PasswordChangeDoneView.as_view()


class PasswordResetView(auth_views.PasswordResetView):
    template_name = "accounts/password_reset_form.html"


password_reset_view = PasswordResetView.as_view()


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


password_reset_done_view = PasswordResetDoneView.as_view()


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"


password_reset_confirm_view = PasswordResetConfirmView.as_view()


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


password_reset_complete_view = PasswordResetCompleteView.as_view()

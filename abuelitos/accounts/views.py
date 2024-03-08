from django.contrib.auth import views as views_auth


class LoginView(views_auth.LoginView):
    template_name = "accounts/login.html"


login_view = LoginView.as_view()


class LogoutView(views_auth.LogoutView):
    template_name = "accounts/logged_out.html"


logout_view = LogoutView.as_view()


class PasswordChangeView(views_auth.PasswordChangeView):
    template_name = "accounts/password_change_form.html"


password_change_view = PasswordChangeView.as_view()


class PasswordChangeDoneView(views_auth.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


password_change_done_view = PasswordChangeDoneView.as_view()


class PasswordResetView(views_auth.PasswordResetView):
    template_name = "accounts/password_reset_form.html"


password_reset_view = PasswordResetView.as_view()


class PasswordResetDoneView(views_auth.PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


password_reset_done_view = PasswordResetDoneView.as_view()


class PasswordResetConfirmView(views_auth.PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"


password_reset_confirm_view = PasswordResetConfirmView.as_view()


class PasswordResetCompleteView(views_auth.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


password_reset_complete_view = PasswordResetCompleteView.as_view()

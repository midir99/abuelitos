from django.contrib import auth
from django.contrib.auth import views as views_auth
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic as views_generic


class LoginView(views_auth.LoginView):
    template_name = "accounts/login.html"


login_view = LoginView.as_view()


class LogoutConfirmView(views_generic.TemplateView):
    template_name = "accounts/profile_logout_confirm.html"


logout_confirm_view = LogoutConfirmView.as_view()


class LogoutView(views_auth.LogoutView):
    template_name = "accounts/logged_out.html"


logout_view = LogoutView.as_view()


class PasswordChangeView(SuccessMessageMixin, views_auth.PasswordChangeView):
    template_name = "accounts/profile_password_change_form.html"
    success_message = _("Your password was updated successfully.")
    success_url = reverse_lazy("accounts:password_change")


password_change_view = PasswordChangeView.as_view()


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


class ProfileView(SuccessMessageMixin, views_generic.UpdateView):
    template_name = "accounts/profile_my_information.html"
    model = auth.get_user_model()
    fields = [
        "username",
        "first_name",
        "last_name",
    ]
    success_message = _("Your profile was updated successfully.")

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.request.user.pk)


profile_view = ProfileView.as_view()

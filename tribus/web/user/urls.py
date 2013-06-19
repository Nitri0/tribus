"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed for
django-registration 1.0. For new installs, use
``include('registration.backends.default.urls')``.

"""

"""
URLconf for registration and activation, using django-registration's
default backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.default.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize registration behavior, feel free to set up
your own URL patterns for these views instead.

"""


from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from tribus.web.user.views import ActivationView, SignupView, LoginView
from tribus.web.user.forms import LoginForm


urlpatterns = patterns(
    '',

    url(regex=r'^login/$',
        view=LoginView,
        kwargs={
            'template_name': 'user/login_form.html',
            'redirect_field_name': '/',
            'authentication_form': LoginForm
        },
        name='user_login',
        ),

    url(regex=r'^logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={'next_page': '/'},
        name='user_logout'
        ),

    url(regex=r'^signup/$',
        view=SignupView.as_view(template_name='user/signup_form.html'),
        name='user_signup',
        ),

    url(regex=r'^signup/complete/$',
        view=TemplateView.as_view(template_name='user/signup_complete.html'),
        name='user_signup_complete',
        ),

    url(regex=r'^activate/(?P<activation_key>\w+)/$',
        view=ActivationView.as_view(template_name='user/activate_form.html'),
        name='user_activate',
        ),

    url(regex=r'^activate/complete/$',
        view=TemplateView.as_view(template_name='user/activate_complete.html'),
        name='user_activate_complete',
        ),

    url(regex=r'^password/change/$',
        view='django.contrib.auth.views.password_change',
        kwargs={'template_name': 'user/password_change_form.html'},
        name='user_password_change',
        ),

    url(regex=r'^password/change/done/$',
        view='django.contrib.auth.views.password_change_done',
        kwargs={'template_name': 'user/password_change_done.html'},
        name='user_password_change_done',
        ),

    url(regex=r'^password/reset/$',
        view='django.contrib.auth.views.password_reset',
        kwargs={
            'template_name': 'user/password_reset_form.html',
            'email_template_name': 'user/password_reset_email.html'
        },
        name='user_password_reset',
        ),

    url(regex=r'^password/reset/done/$',
        view='django.contrib.auth.views.password_reset_done',
        kwargs={'template_name': 'user/password_reset_done.html'},
        name='user_password_reset_done',
        ),

    url(regex=r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        view='django.contrib.auth.views.password_reset_confirm',
        kwargs={'template_name': 'user/password_reset_confirm.html'},
        name='user_password_reset_confirm',
        ),

    url(regex=r'^password/reset/complete/$',
        view='django.contrib.auth.views.password_reset_complete',
        kwargs={'template_name': 'user/password_reset_complete.html'},
        name='user_password_reset_complete',
        ),

)

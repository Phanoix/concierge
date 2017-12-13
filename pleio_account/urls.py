"""pleio_account URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from oauth2_provider import views as oauth2_views
from api import views as api_views
from django.contrib import admin
from core import views
from core.class_views import PleioLoginView, PleioSessionDeleteView, PleioSessionDeleteOtherView

legacy_urls = [
    url(r'^mod/profile/icondirect.php$', views.avatar, name='avatar_legacy'),
    url(r'^action/logout$', views.logout, name='logout_legacy')
]

urls = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register/complete/$', views.register_complete, name='register_complete'),
    url(r'^register/activate/(?P<activation_token>[-:\w]+)/$', views.register_activate, name='register_activate'),
    url(r'^termsofuse/$', views.terms_of_use, name='terms_of_use'),
    url(r'^securitypages/(?P<page_action>[\w-]+)/$', views.security_pages, name='security_pages'),
    url(r'^securitypages/$', views.security_pages, name='security_pages'),
    url(r'^password_reset/$', auth_views.password_reset, { 'template_name': 'password_reset.html' }, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, { 'template_name': 'password_reset_done.html' }, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, { 'template_name': 'password_reset_confirm.html' }, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, { 'template_name': 'password_reset_complete.html' }, name='password_reset_complete'),
    url(r'^login/$', PleioLoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^accept_previous_logins/(?P<acceptation_token>[-:\w]+)/$', views.accept_previous_login, name='accept_previous_login'),
    url(r'^account/login/$', PleioLoginView.as_view(), name='login'),
    url(r'^account/sessions/other/delete/$', view=PleioSessionDeleteOtherView.as_view(), name='session_delete_other'),
    url(r'^account/sessions/(?P<pk>\w+)/delete/$', view=PleioSessionDeleteView.as_view(), name='session_delete'),
    url(r'^oauth/v2/authorize$', oauth2_views.AuthorizationView.as_view(), name='authorize'),
    url(r'^oauth/v2/token$', oauth2_views.TokenView.as_view(), name='token'),
    url(r'^oauth/v2/revoke_token$', oauth2_views.RevokeTokenView.as_view(), name='revoke-token'),
    url(r'^api/users/me$', api_views.me, name='me'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home')
]

tf_urls = [
    url(r'', include('two_factor.urls', 'two_factor'))
]
us_urls = [
    url(r'', include('user_sessions.urls', 'user_sessions'))
]

urlpatterns = legacy_urls + urls +  tf_urls + us_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

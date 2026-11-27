from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

admin.site.site_header = "CEAL / LUZ — Administração"
admin.site.site_title = "CEAL / LUZ"
admin.site.index_title = "Gestão do sistema"

urlpatterns = [
    path("pessoas/", include("pessoas.urls")),
    path("", login_required(TemplateView.as_view(template_name="home.html")), name="home"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
]

from django.urls import path
from . import views

app_name = "pessoas"
urlpatterns = [
    path("", views.PessoaList.as_view(), name="list"),
    path("nova/", views.PessoaCreate.as_view(), name="create"),
    path("<int:pk>/editar/", views.PessoaUpdate.as_view(), name="update"),
    path("<int:pk>/situacao/", views.alterar_situacao, name="status"),
]

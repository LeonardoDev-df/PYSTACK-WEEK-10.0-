from django.urls import path

from . import views


jls_extract_var = "cadastro"
jls_extract_var_Login = "login"
urlpatterns = [
     path('cadastro/', views.cadastro, name=jls_extract_var),
     path('login/', views.login_view, name=jls_extract_var_Login),
     path('sair/', views.sair, name="sair")

]
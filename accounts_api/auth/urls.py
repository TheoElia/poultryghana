from django.urls import re_path
from . import views


urlpatterns = [
    ##################     AUTH APIS      #############################
    re_path(r'^login-user/$',views.login_user),
    re_path(r'^create-user/$',views.create_account),
]
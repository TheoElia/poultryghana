from django.urls import re_path
from . import views

urlpatterns = [
    # login
    re_path(r'^$',views.dashboard,name="home"),
    re_path(r'^login/$',views.login_page,name="login-page"),
    re_path(r'^register/$',views.register,name="login-page"),
    re_path(r'^dashboard/$',views.dashboard,name="dashboard-page"),
    re_path(r'^add-farm/$',views.add_farm,name="add-farm-page"),
]
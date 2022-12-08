from django.urls import re_path
from . import views

urlpatterns = [
    # login
    re_path(r'^$',views.index,name="home"),
    re_path(r'^dashboard/$',views.dashboard,name="dashboard"),
    re_path(r'^login/$',views.login_page,name="login-page"),
    re_path(r'^register/$',views.register,name="login-page"),
    re_path(r'^dashboard/$',views.dashboard,name="dashboard-page"),
    re_path(r'^add-farm/$',views.add_farm,name="add-farm-page"),
    re_path(r'^add-shop/$',views.add_shop,name="add-shop-page"),
    re_path(r'^dashboard/(?P<pen_no>[^/]+)/$',views.records,name="records-page"),
]
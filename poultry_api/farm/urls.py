from django.urls import re_path
from . import views


urlpatterns = [
    ##################     FARM APIS      #############################
    re_path(r'^get-poultry-records/$',views.get_poultry_records),
    re_path(r'^get-poultry-record-records/$',views.get_poultry_record_records),
    re_path(r'^get-shop-products/$',views.get_shop_products),
    re_path(r'^search-api/$',views.search_api),
]
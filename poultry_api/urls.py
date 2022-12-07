from django.urls import include, re_path



urlpatterns = [
    re_path('farm/', include("poultry_api.farm.urls")),
    ]


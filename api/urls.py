from django.urls import include, re_path



urlpatterns = [
    re_path('accounts/', include('accounts_api.urls')),
    re_path('poultry/', include('poultry_api.urls')),
    ]
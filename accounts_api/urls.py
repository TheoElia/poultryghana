from django.urls import include, re_path



urlpatterns = [
    re_path('auth/', include("accounts_api.auth.urls")),
    ]


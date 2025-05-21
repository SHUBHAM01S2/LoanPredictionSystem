from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),                # Home page
    path('predict/', views.predict, name='predict'),  # Prediction form and result
    path('predict/result/',views.result)
]

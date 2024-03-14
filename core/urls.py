"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import RedirectView

from apps.user.api.views import UserViewSet
from apps.loan.api.views import LoanViewSet
from apps.payment.api.views import PaymentViewSet
from utils.favicon import empty_favicon

router = DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"loan", LoanViewSet)
router.register(r"payment", PaymentViewSet)

urlpatterns = [
    path("favicon.ico", empty_favicon),
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/home/")),
    path("", include("apps.frontend.urls")),
]

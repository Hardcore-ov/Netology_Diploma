"""order_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from orders.views import (CategoryViewSet, CharacteristicViewSet,
                            ImportView, OrderItemViewSet,
                            OrderViewSet, PasswordResetView,
                            ProductCharacteristicViewSet,
                            ProductViewSet, CustomerViewSet,
                            CatalogViewSet, ProviderViewSet,
                            UserViewSet, ImportCheckView)

app_name = "orders"
r = DefaultRouter()
r.register("users", UserViewSet)
r.register("providers", ProviderViewSet)
r.register("categories", CategoryViewSet)
r.register("products", ProductViewSet)
r.register("characteristics", CharacteristicViewSet)
r.register("catalogs", CatalogViewSet)
r.register("product_characteristics", ProductCharacteristicViewSet)
r.register("customers", CustomerViewSet)
r.register("orders", OrderViewSet)
r.register("order_items", OrderItemViewSet)
urlpatterns = [
    path("authorize/", obtain_auth_token),
    path("password_reset/", PasswordResetView.as_view()),
    path("import/", ImportView.as_view()),
    path("import/<str:task_id>/", ImportCheckView.as_view()),
] + r.urls
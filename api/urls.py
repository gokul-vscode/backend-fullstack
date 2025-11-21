from django.urls import path
from .views import getProducts, ProductList, ProductDetail
from .auth_views import signup, login

urlpatterns = [
    path("products/", getProducts),
    path("products/list/", ProductList.as_view()),
    path("products/<int:pk>/", ProductDetail.as_view()),

    path("signup/", signup),
    path("login/", login),
]

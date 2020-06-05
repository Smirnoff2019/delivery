from django.urls import path
from market.views.auth import AuthView, hello
from market.views.product import ProductListView


urlpatterns = [
    path('userlogin/', AuthView.as_view()),
    path('product_list/', ProductListView.as_view()),
    path('hello/', hello)
]
from django.urls import path
from market.views.auth import AuthView
from market.views.product import ProductListView
from market.views.consumer import ConsumerListView
from market.views.provider import ProviderListView


urlpatterns = [
    path('userlogin/', AuthView.as_view()),
    # path('hello/', hello),
    path('product_list/', ProductListView.as_view()),
    path('consumer_list/', ConsumerListView.as_view()),
    path('provider_list/', ProviderListView.as_view())
]
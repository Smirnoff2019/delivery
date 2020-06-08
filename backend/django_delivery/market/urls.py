from django.urls import path
from market.views.auth import AuthView
from market.views.product import ProductListView
from market.views.consumer import ConsumerListView
from market.views.provider import ProviderListView

from market.views.auth import about_us, contacts

urlpatterns = [
    path('userlogin/', AuthView.as_view()),
    path('about_us/', about_us),
    path('contacts/', contacts),
    path('product_list/', ProductListView.as_view()),
    path('consumer_list/', ConsumerListView.as_view()),
    path('provider_list/', ProviderListView.as_view())
]
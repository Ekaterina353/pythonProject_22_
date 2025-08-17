from operator import index

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, CatalogContactsView, HomeListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('contacts/', CatalogContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')

]

from django.urls import path
from . import views

app_name = 'Products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='all'),
    path('products/<int:pk>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]
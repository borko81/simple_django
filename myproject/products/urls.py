from django.urls import path
from products import views as product

app_name = 'product'
urlpatterns = [
    path('', product.view_all_product, name='view_all_product'),
    path('detail/<int:product_id>/', product.product_detail_view, name='detail_product'),
    path('new/', product.product_new, name='product_new'),
    path('edit/<int:product_id>/', product.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', product.delete_product, name='delete_product'),
]

from django.urls import path
from .views import supplier, brand, category, device

urlpatterns = [
    path('suppliers/', supplier.supplier_list, name="supplier_list"),
    path('suppliers/create', supplier.create_supplier, name="create_supplier"),
    path('suppliers/<str:sid>', supplier.view_supplier, name="view_supplier"),
    path('suppliers/edit/<str:sid>', supplier.edit_supplier, name="edit_supplier"),
    path('suppliers/delete/<str:sid>', supplier.delete_supplier, name="delete_supplier"),
    path('brands/', brand.brand_list, name="brand_list"),
    path('brands/create', brand.create_brand, name="create_brand"),
    path('brands/<str:sid>', brand.view_brand, name="view_brand"),
    path('brands/edit/<str:bid>', brand.edit_brand, name="edit_brand"),
    path('brands/delete/<str:bid>', brand.delete_brand, name="delete_brand"),
    path('categories/', category.category_list, name="category_list"),
    path('categories/create', category.create_category, name="create_category"),
    path('categories/<str:cid>', category.view_category, name="view_category"),
    path('categories/edit/<str:cid>', category.edit_category, name="edit_category"),
    path('categories/delete/<str:cid>', category.delete_category, name="delete_category"),
    path('devices/create', device.create_device, name="create_device"),
]
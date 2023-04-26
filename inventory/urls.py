from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.supplier_list, name="supplier_list"),
    path('suppliers/create', views.create_supplier, name="create_supplier"),
    path('suppliers/<str:sid>', views.view_supplier, name="view_supplier"),
    path('suppliers/edit/<str:sid>', views.edit_supplier, name="edit_supplier"),
    path('suppliers/delete/<str:sid>', views.delete_supplier, name="delete_supplier"),
]
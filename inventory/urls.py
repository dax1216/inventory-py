from django.urls import path
from django.contrib.auth import views as auth_views
from .views import supplier, brand, category, device, order, user, home

urlpatterns = [
    path('', home.home, name="home"),
    path('suppliers/', supplier.supplier_list, name="supplier_list"),
    path('suppliers/create', supplier.create_supplier, name="create_supplier"),
    path('suppliers/<str:sid>', supplier.view_supplier, name="view_supplier"),
    path('suppliers/edit/<str:sid>', supplier.edit_supplier, name="edit_supplier"),
    path('suppliers/delete/<str:sid>', supplier.delete_supplier, name="delete_supplier"),
    path('brands/', brand.brand_list, name="brand_list"),
    path('brands/create', brand.create_brand, name="create_brand"),
    path('brands/<str:bid>', brand.view_brand, name="view_brand"),
    path('brands/edit/<str:bid>', brand.edit_brand, name="edit_brand"),
    path('brands/delete/<str:bid>', brand.delete_brand, name="delete_brand"),
    path('categories/', category.category_list, name="category_list"),
    path('categories/create', category.create_category, name="create_category"),
    path('categories/<str:cid>', category.view_category, name="view_category"),
    path('categories/edit/<str:cid>', category.edit_category, name="edit_category"),
    path('categories/delete/<str:cid>', category.delete_category, name="delete_category"),
    path('devices/', device.device_list, name="device_list"),
    path('devices/create', device.create_device, name="create_device"),
    path('devices/edit/<str:did>', device.edit_device, name="edit_device"),
    path('orders/', order.order_list, name="order_list"),
    path('orders/create', order.create_order, name="create_order"),
    path('orders/edit/<str:oid>', order.edit_order, name="edit_order"),
    path("register", user.register_request, name="register"),
    path("login", user.login_request, name="login"),
    path("logout", user.logout_request, name="logout"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path("password_reset", user.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='inventory/user/reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="inventory/user/reset_password_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='inventory/user/reset_password_complete.html'), name='password_reset_complete'),
]
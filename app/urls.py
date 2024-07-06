from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('ml_cart/', views.ml_cart, name='ml_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_list/', views.add_list, name='add_list'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('crossoff/<item_id>', views.cross_off, name='cross_off'),
    path('uncross/<item_id>', views.uncross, name='uncross'),
    # path('edit/<item_id>', views.edit, name='edit'),
  
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]

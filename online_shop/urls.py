from django.urls import path
from . import views

urlpatterns = [
    path('', views.barang, name='home'),
    path('barang/tambah/', views.tambah, name='tambah'),
    path('barang/<int:barang_id>', views.detail_barang, name='detail_barang'),
    path('submit', views.submit, name='submit')
]
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def barang(request):
    fields = {"barang": Barang.objects.all()[::-1]}
    return render(request, 'online_shop/barang.html', fields)

def detail_barang(request, barang_id):
    querry_barang = Barang.objects.get(pk=barang_id)
    # deskripsi = Barang.deskripsi.get(pk=barang_id)
    fields = {"barang": querry_barang}
    
    return render(request, 'online_shop/detail.html', fields)

def tambah(request):
    fields = {}
    return render(request, 'online_shop/tambah.html', fields)

def submit(request):
    barang = Barang(
        gambar = request.POST['gambar'],
        nama_barang = request.POST['nama-barang'],
        harga = request.POST['harga'],
        deskripsi = request.POST['deskripsi']
    )
    barang.save()
    return redirect('home')
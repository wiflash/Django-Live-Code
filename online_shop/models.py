from django.db import models

# Create your models here.
class Barang(models.Model):
    gambar = models.CharField(max_length=200, default="")
    nama_barang = models.CharField(max_length=100, default="")
    deskripsi = models.TextField(default="")
    harga = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama_barang
from django.db import models

class Gejala(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Penyakit(models.Model):
    nama        = models.CharField(max_length=255)
    definisi    = models.TextField()
    solusi      = models.TextField()

    def __str__(self):
        return self.nama
    
class BasisPengetahuan(models.Model):
    id_gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)
    id_penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)
    bobot = models.FloatField()

class DsRules(models.Model):
    id_gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)
    id_penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)
    bobot = models.FloatField()

class Riwayat(models.Model):
    nama = models.CharField(max_length=244)
    tgl = models.DateTimeField()
    result = models.TextField()

    def __str__(self):
        return self.nama

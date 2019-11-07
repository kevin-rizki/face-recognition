# KetokMagicHalal

Program untuk mencari kemiripan kedua buah gambar dengan *Brute Force Matching*

### Konfigurasi

Gunakan Python 3, lalu install pip3
- **Untuk pengguna windows**, download file get-pip.py dari [sini](https://bootstrap.pypa.io/get-pip.py)
Buka command line dan lalu pindah folder ke folder tempat file get-pip.py, lalu ketik : <br />
```python get-pip.py```
- **Untuk pengguna linux**, jalankan perintah: <br />
```sudo apt-get install pip```

Dalam windows ataupun linux, install library tambahan yaitu **cv2**,**tkinter**, dan **pillow** <br />
```pip3 install cv2``` <br />
```pip3 install tkinter```<br />
```pip3 install pillow```

Setelah itu, download database dari [sini](https://www.kaggle.com/frules11/pins-face-recognition/version/1#) dan taruh pada folder yang sama dengan folder program.
Kemudian dalam Command Line / Bash jalankan:<br />
```python generateinputdata.py```

Akan terdapat dua folder baru, yaitu *testdata* dan *reference*. Pada Command Line / Bash jalankan:<br />
```python generatepicklefile.py reference```
Ini untuk membuat file *pins.db* yang akan digunakan sebagai database pada program.

### Penggunaan
*Flow* penggunaan adalah sebagai berikut:

- Dalam folder program ***Ketok Magic Halal***, dalam command line / bash, jalankan:<br />
*Python main.py*
- Dalam menu utama, klik **Pilih File**, lalu pilih gambar pada folder PINS/Nama orang/Foto orang tersebut.jpg
- Pilih metode *feature matching* yang ingin digunakan. Kalau ingin *cosine similarity* pilih ***Match (CS)***. Jika ingin *Euclidean Distance*,
Pilih ***Match (ED)***.
- Setelah di klik akan muncul 10 gambar terurut skor kemiripannya dengan gambar sampel. Anda dapat menutup program atau
kembali ke menu awal untuk mencoba gambar lain.

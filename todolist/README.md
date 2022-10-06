

# PBP Assignment 4 - Implementing Forms and Authentication Using Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh 
Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama  : Wayan Angga Putra Aldita**

**NPM   : 2106650065**

**Kelas : C**

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline CSS diimplementasikan pada elemen HTML, yang mana pengguaannya cukup efisien apabila hanya melakukan styling satu atau dua elemen yang berbeda. Namun, penambahan styling pada html secara langsung membuat file html sulit untuk dibaca. 
2. Internal CSS diimplementasikan secara internal di dalam file .html pada section `<style></style>`, namun terpisah dari tag HTML. Terdapat fitur yang tidak ada pada inline CSS seperti Id selector & class. Namun, implementasi tersebut akan memakan waktu yang cukup lama apabila terdapat banyak file .html
3. External CSS diimplementasikan secara external di luar file .html yang biasanya diaplikasikan ke file .css yang nantinya akan di link ke file .html. Implementasi ini sangat berguna apabila bekerja pada website besar, di mana styling hanya cukup dilakukan di satu halaman untuk beberapa element/komponen yang sama. Namun, terkadang ada kemungkinan halaman .html tidak akan disajikan dengan baik sebelum external CSS sepenuhnya dimuat.

## Jelaskan tag HTML5 yang kamu ketahui.
1. `<h1></h1>` - `<h6></h6>`, untuk membuat heading
2. `<p></p>`, untuk membuat element teks yang membentuk suatu paragraf
3. `<img src=''/>`, untuk menambahkan/link gambar ke dalam project
4. `<br></br>`, untuk memberi line break
5. `<a><a/>`, untuk membuat suatu link yang dapat melakukan navigasi ke suatu route
6. `<form></form>`, untuk membuat element form


## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Id selector; styling terhadap suatu elemen yang menggunakan Id reference yang unik
- Tag selector, styling terhadap keseluruhan elemen tag
- Class selector, melakukan styling secara universal

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Instalasi Django Tailwind dapat dilihat melalui [dokumentasi ini](https://django-tailwind.readthedocs.io/en/latest/installation.html)
2. Styling dengan menggunakan tailwind ke masing-masing template yang digunakan todolist dengan memperhatikan aspek estetika dan responsivitas halaman
3. Mengubah item pada todolist menjadi individual card 

## Link aplikasi
Link untuk menuju aplikasi yang telah dikerjakan dapat diakses [di sini](https://pbp-tugas-2-angga.herokuapp.com/todolist/).

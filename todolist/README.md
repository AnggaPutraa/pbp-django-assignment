

# PBP Assignment 5 - Javascript and AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh 
Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama  : Wayan Angga Putra Aldita**

**NPM   : 2106650065**

**Kelas : C**

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Asynchronous programming memungkinkan pengguna untuk melakukan interaksi dengan website selagi server atau client side memproses data, sehingga sangat memungkinkan untuk menjalankan banyak proses secara bersamaan tanpa harus menunggu proses lain selesai.
- Synchronous programming mengharuskan user untuk menunggu server dan client side memproses data terlebih dahulu sebelum berpindah ke suatu state, sehingga hanya terdapat satu proses yang dapat dieksekusi dalam satu waktu dengan memperhatikan urutan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event Driven Programming merupakan paradigma pemrograman di mana objek dapat berkomunikasi secara tidak langsung dengan mengirimkan pesan satu sama lain melalui perantara. Pengiriman pesan tersebut dilakukan melalui event stream. Paradigma ini bergantung pada event dengan memperhatikan operasi apa yang akan diimplementasikan dari adanya event. Penerapan paradigma dalam tugas ini terdapat pada implementasi tombol submit form penambahan task. Apabila tombol ditekan, maka akan terdapat event yang di trigger dan ditangani oleh AJAX sebagai perantara untuk mengirim data yang diisi dari form ke server, Selain itu, AJAX akan memperbarui data pada section Todo list secara asynchronous.

## Jelaskan penerapan asynchronous programming pada AJAX.
Membuat view serta url path baru yang mereturn sebuah response JSON. Implementasi asynchronous programming AJAX dalam tugas ini terdapat pada function get serta post untuk mengambil serta mengirim data JSON ke server, serta mengatur tampilan pada Todo list secara asynchronous sesuai data yang ada pada database

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat function baru yang mereturn response berupa JSON 
2. Menambahkan attribute onClick pada button create task yang diintegrasikan dengan AJAX serta modals pop up
3. Menambahkan beberapa function javascript untuk melakukan get dan post request ke server
4. Memindahkan component card menjadi response dari post request AJAX dengan data pada card yang didapat dari get request.


## Link aplikasi
Link untuk menuju aplikasi yang telah dikerjakan dapat diakses [di sini](https://pbp-tugas-2-angga.herokuapp.com/todolist/).
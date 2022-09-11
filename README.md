**Nama  : Wayan Angga Putra Aldita**

**NPM   : 2106650065**

**Kelas : C**

# PBP - Tugas 2
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer 
Universitas Indonesia, Semester Ganjil 2022/2023

## Deskirpsi Tugas
Mengimplementasikan konsep Model-View-Template serta beberapa  hal yang telah dipelajari selama sesi tutorial lab.

## Jawaban dari pertanyaan yang diajukan pada Tugas 2

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

   ![](https://raw.githubusercontent.com/AnggaPutraa/pbp-tugas-2/main/assets/preview_bagan_client_django.png)

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    
    Virtual environment berfungsi untuk mengatasi pemindahan dependencies dari suatu project 
    akibat perbedaan versi Python dan sistem operasi yang digunakan. Virtual environment sangat 
    bermanfaat ketika mengerjakan project Django dengan tim, di mana sangat ada kemungkinan tiap orang 
    dalam tim memiliki sistem operasi serta versi python yang berbeda-beda dan di sini lah peran 
    virtual environment untuk menjamin project yang dikerjakan dapat berjalan di lingkungannya 
    masing-masing. Contoh implementasinya adalah ketika menginstal requirement.txt, sebelum 
    menjalankan project Django, di mana virtual environment akan menginstall third libraries yang 
    dibutuhkan dengan versi yang dapat digunakan sesuai dengan lingkungannya. 
    Sekarang muncul suatu pertanyaan yaitu apakah bisa membuat aplikasi web berbasis Django tanpa 
    menggunakan virtual environment? Jawabannya adalah bisa, namun harus sesuai dengan kebutuhan 
    project, di mana jika mengerjakan project sendiri, jawabannya tentu saja bisa, karena tidak 
    memerlukan penyesuaian environment yang digunakan pada project, namun ketika work as a team, 
    penggunaan virtual environment sangat dibutuhkan demi kelancaran project.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
    - Membuat function di views.py pada folder katalog untuk mengambil data dari model dan me-retrun sebuah render untuk mengembalikan sebuah halaman yang berisikan data yang telah diproses dan diolah dengan file katalog.html.
    - Membuat routing untuk melakukan mapping function yang ada pada views.py yang telag dibuat, di mana perlu melakukan konfigurasi pada folder katalog dibagian urls.py dengan cara membuat variabel global bernama app_name dengan nama katalog dan membuat sebuah list yang berisikan method path dengan route ‘ ‘ , beserta function show_katalog pada views.py dan memberi argumen nama string nama function yang dimasukkan pada argumen view (‘show_katalog’). Selanjutkan, konfigurasi pada folder project_django dibagian setting.py untuk mendaftarkan aplikasinya dengan cara memasukkan string “katalog” pada bagian INSTALLED_APPS yang berupa list of String dan bagian urls.py pada list urlpatterns, tambahkan method path dengan mengisi field route dengan “/katalog” di mana nama routing ketika client mengakses baseUrl/katalog.
    - Selanjutnya, pada katalog.html kita perlu memetakan data yang telah diolah pada models yang di-passing melalui views.py dengan cara mengisi field yang sebelumnya telah tersedia pada template project tugas 2 ini, di mana field dapat dimasukkan dengan memberi tag html pada biasanya ditambah dengan {{ namaKeyPadaContext }} dan untuk data pada file initial_catalog_data.json yang telah diolah model, untuk menampilkannya pada file html, kita dapat melakukan loop dengan syntax khusus template django.
    - Untuk melakukan deployment, kita perlu membuat aplikasi baru di Heroku, pada dashboard Heroku  tekan New - Create New App, lalu setelah memberi nama aplikas, pada bagian setting aplikasi tambahkan Config Vars dengan variabel bernama HEROKU_APP_NAME dengan value nama project dan variable bernama SECRET_KEY dengan value berupa key secret yang ingin dimasukkan. Selanjutnya buat repository pada account Github dan pada project Django yang dikerjakan lakukan add, commit, add remote, dan push. Selanjutnya pada Github tambahkan file dpl.yml yang menuju directory nama-repo/workflows/dpl.yml. dpl.yml berisikan beberapa instruksi untuk mengeksekusi deployment oleh runner dari GitHub Actions. Selanjutnya pada aplikasi Heroku bagian deploy, kaitkan account github beserta repository yang akan di deploy, lalu tekan button Deploy Branch.

## Link aplikasi
Link untuk menuju website Django yang telah dikerjakan dapat diakses [di sini](https://pbp-tugas-2-angga.herokuapp.com/).

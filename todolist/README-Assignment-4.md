
# PBP Assignment 4 - Implementing Forms and Authentication Using Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh 
Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama  : Wayan Angga Putra Aldita**

**NPM   : 2106650065**

**Kelas : C**

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>?` Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
`{% csrf_token %}` token berfungsi untuk menjamin keamanan user dan site.  Apabila tidak mencantumkan syntax tersebut, kedua aspek penting yaitu user dan site akan rawan terkena serangan dari pihak eksternal, serta Django sendiri tidak mengizinkan serta memverifikasi akses ke dalam route yang menggunakan form pada website tanpa adanya `{% csrf_token %}`.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Bisa, hal ini dapat dilakukan dengan membuat form sebagai suatu object dengan membuat input fields secara manual dalam syntax HTML dan membuat sebuah trigger untuk mensubmit POST request pada setiap text controller yang berisi value. Pembuatan form secara manual memiliki keuntungan tersendiri, di mana hal ini bergantung dengan keinginan developer dalam menampilkan interfacenya.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika user menekan tombol login, submit, atau save, browser meresponse dengan mengirimkan POST request ke dalam server. event POST request tersebut akan melakukan perubahan pada server atau database. Setelah menjalankan event tersebut, Django views akan merespon kembali dengan mengembalikan atau memproses data yang diinginkan dengan melakukan user redirect  ke views sebelumnya yang mana hal ini akan mengupdate tampilan dengan data yang baru.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama `todolist` dengan cara menjalankan perintah ini ke terminal
    ```bash
    python manage.py startapp todolist
    ```

2. Menambahkan aplikasi `todolist` ke **INSTALLED_APPS** pada `settings.py`
    ```bash
    INSTALLED_APPS = [
        .....,
        'todolist',
        .....,
    ]
    ```

3. Pada bagian file `models.py` yang berada pada folder `todolist`, buat modelsnya dengan fields
- user
- date
- title
- description
- is_finished

4. Jalankan perintah
    ```bash
    python manage.py makemingrations
    python manage.py migrate
    ```

5. Pada bagian `views.py` yang berada `todolist` buatlah fungsi-fungsi yang dibutuhkan yang diantaraya adalah
    ```python
    def register_user(request):
        .........

    def login_user(request):
        .........

    def logout_user(request):
        .........

    @login_required(login_url='/todolist/login/')
    def show_todos(request):
        .........

    @login_required(login_url='/todolist/login/')
    def create_task(request, id):
        .........

    @login_required(login_url='/todolist/login/')
    def update_task(request, id):
        .........
    ```

6. Buat folder bernama `templates` di dalam folder `todolist` lalu tambahkan file html yang diperlukan ke dalam folder `templates`

7. Pada folder `todolist` tambahkan file `urls.py` untuk melakukan roting ke fungsi yang ada pada file `views.py` dengan menambahkan variable **app_name** dengan  value 'todolist' serta membuat sebuah list yang menampung url patterns

8. Terakhir, daftarkan `todolist` ke dalam `urls.py` yang ada pada folder `project_django` pada variabel **urlpatterns**
    ```bash
    urlpatterns = [
        .........,
        path('todolist/', include('todolist.urls')),
        .........,
    ]
    ```

## Link aplikasi
Link untuk menuju aplikasi yang telah dikerjakan dapat diakses [di sini](https://pbp-tugas-2-angga.herokuapp.com/todolist/).

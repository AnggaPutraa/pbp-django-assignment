
# PBP Assignment 3 - Implementing Data Delivery Using Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh 
Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama  : Wayan Angga Putra Aldita**

**NPM   : 2106650065**

**Kelas : C**

## Perbedaan antara JSON, XML, dan HTML

### JSON

```json
{
    "model": "mywatchlist.watchitem",
    "pk": 4,
    "fields": {
        "watched": true,
        "title": "Check the Store Next Door",
        "rating": 5,
        "release_date": "December 20, 2016",
        "review": "The best thing is, each character can resonate with the audience in some way."
    }
}
```
- Hanya sebuah format text yang ditulis dalam JavaScript object
- Tidak dapat melakukan pemrosesan ataupun perhitungan pada data
- Hanya mendukung data bertipe primitif
- Data diisimpan dalam bentuk tree structure
- Data bersifat dinamis
- Size yang digunakan relatif lebih kecil sehingga sangat cepat ketika mentransfer data


### XML

```xml
<object model="mywatchlist.watchitem" pk="4">
    <field name="watched" type="BooleanField">True</field>
    <field name="title" type="TextField">Check the Store Next Door</field>
    <field name="rating" type="IntegerField">5</field>
    <field name="release_date" type="TextField">December 20, 2016</field>
    <field name="review" type="TextField">The best thing is, each character can resonate with the audience in some way.</field>
</object>
```

- Merupakan bahasa markup
- Dapat melakukan pemrosesan serta pemformatan dokumen dan object
- Mendukung banyak tipe data kompleks seperti charts, bagan, dan data non primitif.
- Data disimpan dalam bentuk map dengan key value
- Data bersifat dinamis
- Size yang digunakan relatif lebih besar sehingga lambat ketika mentransfer data


### HTML

```html
{% extends 'base.html' %}
{% block content %}
<table cellspacing = "16">
    <tr>
        <th align="left">watched</th>
        <th align="left">title</th>
        <th align="left">rating</th>
        <th align="left">release_date</th>
        <th align="left">reveiw</th>
    </tr>
    <tr>
        <td>True</td>
        <td>Check the Store Next Door</td>
        <td>5</td>
        <td>December 20, 2016</td>
        <td>The best thing is, each charachter can resonate with the audience in some way.</td>
    </tr>
</table>
{% endblock content %}
```

- Merupakan bahasa markup
- fungsionalitas utamanya adalah untuk menampilkan data
- Dapat melakukan pemrosesan serta pemformatan data atau object
- Data bersifat statis


## Fungsi data delivery dalam pengimplementasian sebuah platform
Melihat pesatnya perkembangan teknologi di era Revolusi Industri 4.0 ini, dunia industri mulai menerapkan 
data delivery ke dalam platform mereka. Data delivery sendiri memberikan manfaat yang signifikan ke dalam 
industri aplikasi seperti membuat aplikasi tidak statis dan lebih interaktif, dengan adanya data delivery 
aplikasi-aplikasi yang berdiri di atas sebuah platform dapat melakukan komunikasi serta bertukar informasi 
satu sama lain.

## Implementasi poin 1-3
1. Membuat suatu aplikasi baru bernama `mywatchlist` dengan cara menjalankan perintah ini ke terminal
    ```bash
    python manage.py startapp mywatchlist
    ```

2. Menambahkan aplikasi `mywatchlist` ke **INSTALLED_APPS** pada `settings.py`
    ```bash
    INSTALLED_APPS = [
        .....,
        .....,
        'wishlist',
    ]
    ```

3. Pada bagian file `models.py` yang berada pada folder `mywatchlist`, buat modelsnya dengan fields
- watched
- title
- rating
- release_date
- review

4. Jalankan perintah ini ke terminal
    ```bash
    python manage.py makemingrations
    python manage.py migrate
    ```

5. Buat sebuah folder bernama `fixture` di dalam folder `mywatchlist`, lalu tambahkan data yang berupa file json dengan nama `initial_mywatchlist_data.json`

6. Selanjutnya, jalankan perintah ini ke terminal
    ```bash
    python manage.py loaddata initial_mywatchlist_data.json
    ```

7. Pada bagian `views.py` yang berada `mywatchlist` buatlah fungsi-fungsi yang dibutuhkan yang diantaraya adalah
    ```python
    def show_my_watch_list(request):
        .........
    def show_my_watchlist_json(request):
        .........
    def show_my_watchlist_xml(request):
        .........
    def show_my_wishlist_html(request):
        .........
    ```

8. Buat folder bernama `templates` di dalam folder `mywatchlist` lalu tambahkan file html di dalam folder `templates`


9. Pada folder `mywatchlist` tambahkan file `urls.py` untuk melakukan roting ke fungsi yang ada pada file `views.py` dengan menambahkan
    ```bash
    app_name = 'mywatchlist'

    urlpatterns = [
        path('', show_my_watch_list, name = 'show_my_watch_list'),
        path('json/', show_my_watchlist_json, name = 'show_my_watchlist_json'),
        path('xml/', show_my_watchlist_xml, name = 'show_my_watchlist_xml'),
        path('html/', show_my_wishlist_html, name = 'show_my_wishlist_html'),
    ]
    ```

10. Daftarkan `mywatchlist` ke dalam `urls.py` yang ada pada folder `project_django` pada variabel **urlpatterns**
    ```bash
    urlpatterns = [
        .........,
        path('mywatchlist/', include('mywatchlist.urls')),
        .........,
    ]
    ```

## Postman
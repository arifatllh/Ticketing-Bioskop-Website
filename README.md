# Dokumentasi Website Ticketing Bioskop

Dokumentasi ini menjelaskan secara rinci tentang teknologi yang digunakan dalam proyek website pemesanan tiket bioskop ini, serta panduan untuk melihat isi database.

## 🛠️ Teknologi yang Digunakan

Website ini dibangun menggunakan arsitektur *Full-Stack* yang memanfaatkan beberapa teknologi modern:

### 1. Backend (Sisi Server)
*   **Python**: Bahasa pemrograman utama yang digunakan untuk logika backend.
*   **Flask**: *Framework* web mikro berbasis Python. Digunakan untuk mengatur *routing* halaman (seperti `/login`, `/movie/<id>`), mengelola *session* pengguna (login/logout), dan menangani *request/response* (GET dan POST).
*   **Werkzeug**: Pustaka standar yang digunakan oleh Flask. Dalam proyek ini, Werkzeug secara khusus digunakan untuk keamanan, yaitu melakukan *hashing* pada *password* pengguna (`generate_password_hash` dan `check_password_hash`) sehingga *password* tidak disimpan dalam bentuk teks biasa.

### 2. Database
*   **SQLite**: *Database engine* yang ringan dan berbasis *file*. Semua data (pengguna, film, jadwal tayang, kursi, transaksi) disimpan secara lokal di dalam satu file bernama `cinema.db`. SQLite dipilih karena sangat mudah di-setup dan tidak memerlukan server *database* terpisah seperti MySQL atau PostgreSQL.

### 3. Frontend (Sisi Klien / UI)
*   **HTML5 & Jinja2**: Struktur kerangka halaman web menggunakan HTML. Jinja2 adalah *templating engine* bawaan Flask yang memungkinkan kita untuk menyisipkan variabel dan logika Python ke dalam file HTML (seperti perulangan `{% for %}` untuk menampilkan daftar film atau `{{ variable }}` untuk menampilkan data dinamis).
*   **Tailwind CSS (v4)**: *Framework* CSS berbasis *utility-first* yang sangat populer. Digunakan untuk mendesain antarmuka (UI) agar terlihat modern, responsif, dan rapi secara cepat tanpa harus menulis file CSS kustom yang panjang.
*   **Vanilla JavaScript**: Digunakan untuk menangani interaktivitas di sisi klien (browser), seperti:
    *   Memilih kursi (mengubah warna saat diklik).
    *   Menghitung total harga secara *real-time*.
    *   Menampilkan *popup* (modal) untuk pembayaran QRIS.
    *   Mencetak tiket/riwayat transaksi.

### 4. Tools & Environment
*   **Node.js & npm**: Digunakan secara khusus untuk mengelola paket dan *build tools* dari Tailwind CSS (`package.json` dan `tailwind.config.js`).

---

## 🗄️ Cara Melihat Database (Pengganti phpMyAdmin)

Karena kita menggunakan **SQLite**, databasenya berupa *file* fisik bernama `cinema.db` yang ada di dalam folder proyek. SQLite tidak berjalan sebagai sebuah "server" seperti MySQL, sehingga ia tidak memiliki halaman web bawaan seperti **phpMyAdmin**.

Namun, ada beberapa cara sangat mudah untuk melihat dan mengedit tabel datanya (seperti di phpMyAdmin):

### Cara 1: Menggunakan Ekstensi VS Code (Paling Mudah)
Jika Anda menggunakan Visual Studio Code untuk *coding*, ini adalah cara yang paling cepat:
1. Buka tab **Extensions** di VS Code (ikon kotak-kotak di sebelah kiri atau `Ctrl+Shift+X`).
2. Cari dan install ekstensi bernama **SQLite Viewer** (oleh *Florian Klampfer*) atau **SQLite** (oleh *alexcvzz*).
3. Setelah terinstall, cukup **klik file `cinema.db`** di folder proyek Anda.
4. VS Code akan otomatis membuka tab baru yang menampilkan semua tabel (users, movies, shows, seats, transactions) beserta isinya dengan tampilan yang rapi.

### Cara 2: DB Browser for SQLite (Aplikasi Desktop)
Ini adalah aplikasi paling populer dan paling mirip dengan phpMyAdmin (namun versi aplikasi desktop).
1. Download aplikasinya secara gratis di: [https://sqlitebrowser.org/](https://sqlitebrowser.org/)
2. Install dan buka aplikasi **DB Browser for SQLite**.
3. Klik tombol **Open Database**, lalu cari dan pilih file `cinema.db` di folder proyek Anda.
4. Buka tab **Browse Data**. Di sana Anda bisa memilih tabel dan melihat, mengubah, atau menghapus data persis seperti di phpMyAdmin.

### Cara 3: SQLite Viewer Web (Tanpa Install)
Jika Anda tidak ingin menginstall apapun dan hanya ingin melihat di browser:
1. Buka website: [https://sqliteviewer.app/](https://sqliteviewer.app/)
2. Tarik (*drag and drop*) file `cinema.db` dari folder proyek Anda ke halaman web tersebut.
3. Anda bisa langsung melihat semua tabel dan data di dalam browser Anda dengan aman (data tidak diupload ke server mereka, hanya dibaca di browser Anda).

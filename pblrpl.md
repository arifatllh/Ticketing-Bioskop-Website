LAPORAN PROJECT PENGEMBANGAN APLIKASI WEB
PEMESANAN TIKET FILM (CINEMA BOOKING) UNTUK BIOSKOP
SEDERHANA
Dosen Pengampu :
Norma Ningsih S.T., M.T.
Kelompok 7:
Guntur Bagus Permadi (2424600004)
Raditya Arif Atahillah (2424600014)
Nathan Andira Raditya (2424600023)
PROGRAM STUDI D4 TEKNOLOGI REKAYASA INTERNET
DEPARTEMEN TEKNIK ELEKTRO
POLITEKNIK ELEKTRONIKA NEGERI SURABAYA
SURABAYA
2026

DAFTAR ISI
Bab I Pendahuluan
1.1 Latar Belakang
1.2 Pembatasan Masalah
1.3 Tujuan
1.4 Manfaat
Bab II Landasan Teori
2.1 Teori Terkait Penelitian Masing-masing
2.2 UML : Usecase Bisnis, Diagram Activity Dan Usecase Sistem
2.3 ooad
Bab III Metodelogi Penelitian
3.1 Pemodelan Bisnis
3.1.1 Hasil Wawancara, Observasi, Dan Studi Pustaka
3.1.2 Identifikasi Masalah (Tabel Masalah, Dampak, Solusi)
3.1.3 Usecase Bisnis
A. Identifikasi Aktor
B. Identifikasi Business Worker
C. Identifikasi Usecase Business
D. Diagram Usecase Business
3.1.4 Diagram Activity
3.1.5 Business Entity
3.2 Analisis Sistem
3.2.1 Analisa Kebutuhan Fungsi
3.2.2 Story Product Backlog
3.2.3 Sprint Backlog (Dan Pembagian Sprint Nya)
3.3 Pemodelan Usecase Sistem
3.3.1 Usecase Sistem
A. Identifikasi Aktor
B. Identifikasi Usecase
C. Diagram Usecase Sistem
3.4 Desain
3.4.1 Diagram Interaksi (Sekuensial Atau Kolaborasi)
3.4.2 Diagram Kelas
3.4.3 Diagram IPO
3.4.4 Rancangan UI/UX
3.4.5 Site Map Dan Gambaran Sistem
3.5 Implementasi
3.5.1 Daily Scrum Report

|     |     |     |
| --- | --- | --- |

3.5.2 Sprint Review
3.5.3 Sprint Retrospective
3.5.4 Tampilan Aplikasi Beserta Penjelasannya
  3.6 Daftar Pustaka
Minimal 10 Daftar Pustaka (Sumber Dari Jurnal Atau Buku)

|     |     |     |
| --- | --- | --- |

BAB I
PENDAHULUAN
1.1 Latar Belakang
Perkembangan teknologi informasi telah memberikan pengaruh yang signifikan
terhadap berbagai bidang pelayanan, termasuk pada industri hiburan seperti bioskop.
Pemanfaatan teknologi berbasis web memungkinkan penyampaian informasi dan layanan
dilakukan secara lebih cepat, mudah, dan efisien. Menurut Pressman & Maxim (2020),
perkembangan perangkat lunak berbasis web telah mendorong transformasi berbagai
layanan konvensional menjadi layanan digital yang lebih efektif. Rosa & Shalahuddin
(2018) juga menjelaskan bahwa aplikasi berbasis web banyak digunakan untuk
menyediakan layanan yang dapat diakses kapan saja dan di mana saja, termasuk pada
sistem pemesanan tiket secara online.
Pada bioskop sederhana, proses penyampaian informasi jadwal film dan
pemesanan tiket masih sering dilakukan secara manual. Calon penonton harus datang
langsung ke lokasi bioskop untuk mengetahui film yang sedang tayang, jadwal
penayangan, serta ketersediaan tiket. Kondisi tersebut dapat menimbulkan
ketidaknyamanan karena memerlukan waktu dan biaya tambahan. Enterprise (2019)
menjelaskan bahwa keterbatasan akses informasi secara langsung sering menjadi kendala
dalam pelayanan yang belum memanfaatkan teknologi berbasis web. Selain itu, antrian
panjang pada loket pembelian tiket dapat menyebabkan calon penonton kehabisan tiket
ketika jumlah kursi yang tersedia terbatas. Kendall & Kendall (2020) menyatakan bahwa
proses pelayanan manual berpotensi menimbulkan keterlambatan layanan dan
menurunkan efisiensi operasional.
Permasalahan juga dialami oleh pengelola bioskop dalam melakukan pengelolaan
data film dan jadwal tayang. Pengelolaan secara manual berpotensi menimbulkan
kesalahan pencatatan, keterlambatan pembaruan informasi, serta kesulitan dalam
memantau transaksi pemesanan yang terjadi. Sommerville (2016) menjelaskan bahwa
sistem yang masih bergantung pada pencatatan manual memiliki risiko kesalahan data
yang lebih tinggi dibandingkan sistem yang terkomputerisasi. Oleh karena itu, diperlukan
sebuah sistem yang mampu menyediakan informasi film secara online, memfasilitasi
pemesanan tiket, menampilkan ketersediaan tiket secara real-time, serta membantu
pengelola dalam mengelola data film dan jadwal tayang. Kebutuhan tersebut sejalan
dengan konsep pengembangan sistem informasi berbasis web yang dijelaskan oleh Rosa
& Shalahuddin (2018).

Berdasarkan permasalahan tersebut, dikembangkan aplikasi web pemesanan tiket
film (Cinema Booking) untuk bioskop sederhana yang dapat memberikan kemudahan
bagi pengguna dalam memperoleh informasi film dan melakukan pemesanan tiket secara
daring, sekaligus membantu pengelola bioskop dalam mengelola operasional pemesanan
tiket secara lebih efektif dan terorganisir. Konsep ini didukung oleh Enterprise (2019)
dan Sommerville (2016) yang menjelaskan bahwa pemanfaatan sistem informasi berbasis
web dapat meningkatkan kualitas layanan, efisiensi pengelolaan data, serta kemudahan
akses informasi bagi pengguna.
1.2 Pembatasan Masalah
Agar pembahasan lebih terarah dan sesuai dengan ruang lingkup proyek, maka
ditetapkan beberapa batasan masalah sebagai berikut:
1. Sistem dikembangkan dalam bentuk aplikasi web.
2. Sistem digunakan untuk pengelolaan pemesanan tiket pada satu bioskop sederhana.
3. Pengguna dapat melakukan registrasi, login, melihat daftar film, melihat detail film,
melakukan pemesanan tiket, dan melihat riwayat pemesanan.
4. Admin dapat mengelola data film, jadwal tayang, serta melihat daftar pemesanan
yang masuk.
5. Sistem menampilkan ketersediaan tiket berdasarkan data yang tersimpan pada basis
data.
6. Sistem belum menyediakan fitur pembayaran online dan integrasi dengan payment
gateway.
7. Sistem tidak membahas pengelolaan tempat duduk secara detail maupun pencetakan
tiket fisik.

1.3 Tujuan
Tujuan dari pengembangan aplikasi web Cinema Booking adalah sebagai
berikut:
1. Mengembangkan aplikasi web yang dapat menampilkan informasi film dan jadwal
tayang secara online.
2. Mengembangkan fitur pemesanan tiket film yang mudah digunakan oleh pengguna.
3. Menyediakan informasi ketersediaan tiket secara real-time untuk setiap jadwal
tayang.
4. Membantu pengelola bioskop dalam mengelola data film, jadwal tayang, dan data
pemesanan secara terpusat.
5. Menyediakan fitur riwayat pemesanan yang dapat digunakan untuk memantau
transaksi yang telah dilakukan pengguna.
1.4 Manfaat
Manfaat yang diharapkan dari pengembangan aplikasi web Cinema Booking
adalah sebagai berikut:
Bagi Pengguna
Memberikan kemudahan dalam memperoleh informasi film yang sedang tayang, melihat
jadwal penayangan, mengetahui ketersediaan tiket, serta melakukan pemesanan tiket
secara online tanpa harus datang langsung ke bioskop.
Bagi Pengelola Bioskop
Membantu proses pengelolaan data film, jadwal tayang, dan transaksi pemesanan secara
lebih efektif, terstruktur, dan mudah dipantau.
Bagi Pengembang
Menjadi sarana penerapan ilmu rekayasa perangkat lunak, analisis sistem, perancangan
basis data, dan pengembangan aplikasi web dalam menyelesaikan permasalahan nyata.
Bagi Institusi Akademik
Menjadi referensi dalam penerapan metodologi pengembangan perangkat lunak pada
studi kasus sistem pemesanan tiket film berbasis web.

BAB II
DASAR TEORI
2.1 Teori Terkait Sistem Pemesanan Tiket (E-Ticketing) dan Aplikasi Web

Dalam pengembangan aplikasi pemesanan tiket bioskop (*Cinema Booking*), terdapat beberapa landasan teori utama yang saling berkaitan, yaitu konsep Sistem Informasi, E-Ticketing, dan arsitektur Aplikasi Web.

**1. Sistem Informasi dan Pemesanan Online**
Sistem informasi adalah kombinasi dari teknologi informasi dan aktivitas orang yang menggunakan teknologi tersebut untuk mendukung operasi dan manajemen (O'Brien & Marakas, 2018). Dalam konteks bioskop, sistem pemesanan online berfungsi sebagai jembatan antara penyedia layanan (bioskop) dan konsumen (penonton) untuk melakukan transaksi tanpa harus bertemu secara fisik. Sistem ini harus mampu mengelola data kompleks seperti jadwal tayang, ketersediaan kursi secara *real-time*, dan pencatatan transaksi secara akurat.

**2. Electronic Ticketing (E-Ticketing)**
*E-Ticketing* atau tiket elektronik adalah suatu cara untuk mendokumentasikan proses penjualan, pelacakan, dan penggunaan tiket tanpa mengeluarkan dokumen berbentuk fisik (kertas) hingga waktu yang dibutuhkan. Menurut Sulistyo (2019), penerapan *e-ticketing* pada industri hiburan seperti bioskop memberikan banyak keuntungan, di antaranya adalah efisiensi waktu karena pelanggan tidak perlu mengantre panjang di loket, transparansi ketersediaan kursi, serta kemudahan bagi pengelola dalam merekap data penjualan dan laporan keuangan secara otomatis.

**3. Pengembangan Aplikasi Web dan Arsitektur *Client-Server***
Aplikasi web yang dibangun umumnya menggunakan arsitektur *Client-Server*. Sisi *client* (frontend) bertanggung jawab atas antarmuka pengguna (UI/UX) dan interaktivitas menggunakan HTML, CSS, dan JavaScript. Sementara itu, sisi *server* (backend) menangani logika bisnis, pemrosesan data, dan komunikasi dengan basis data (database) untuk menyimpan informasi krusial seperti data akun pengguna, film, dan riwayat transaksi pesanan (Pressman & Maxim, 2020). Sistem *ticketing* ini mengadopsi model tersebut guna memastikan data kursi yang dipesan selalu tersinkronisasi antar pengguna dan mencegah terjadinya pemesanan ganda (*double-booking*).
2.2 UML: Usecase Bisnis, Diagram Activity dan Usecase Sistem
2.2.1 Pengertian UML
Unified Modeling Language (UML) adalah bahasa pemodelan standar yang
digunakan untuk memvisualisasikan, menspesifikasikan, membangun, dan
mendokumentasikan artefak dari sistem perangkat lunak. Menurut Pressman &
Maxim (2020), UML menyediakan notasi grafis yang kaya untuk menggambarkan
analisis dan desain sistem berorientasi objek, sehingga memudahkan komunikasi
antar pengembang. Sommerville (2016) juga menambahkan bahwa UML menjadi
standar de facto dalam rekayasa perangkat lunak modern karena kemampuannya
dalam memodelkan sistem baik dari sudut pandang statis maupun dinamis.
Secara umum, UML terbagi menjadi dua kategori besar, yaitu structural
diagrams (diagram struktur) dan behavioral diagrams (diagram perilaku). Untuk
pemodelan proses bisnis dan kebutuhan fungsional sistem, diagram yang paling
umum digunakan adalah use case diagram dan activity diagram (Rosa &
Shalahuddin, 2018).
2.2.2 Usecase Bisnis (Business Use Case)
Business Use Case atau use case bisnis adalah representasi dari proses-proses
bisnis yang terjadi dalam suatu organisasi, tanpa mempertimbangkan teknologi
sistem yang akan dibangun. Menurut Kendall & Kendall (2020), use case bisnis
menggambarkan interaksi antara business actor (pelaku bisnis) dengan business
worker (pekerja bisnis) untuk mencapai tujuan bisnis tertentu.
Dalam pengembangan sistem Cinema Booking, identifikasi use case bisnis
dilakukan dengan terlebih dahulu menentukan aktor bisnis. Berdasarkan analisis,
aktor bisnis yang terlibat terdiri dari:
1. Calon Penonton (Customer), yaitu individu yang ingin mengetahui jadwal film
dan melakukan pemesanan tiket.
2. Admin Bioskop (Pengelola), yaitu pihak yang bertanggung jawab mengelola
data film, jadwal tayang, dan memvalidasi pemesanan.
3. Sistem, yaitu aplikasi web yang memproses data secara otomatis.

Rospricilia & Ma'ady (2024) menjelaskan bahwa dalam pemodelan use case
untuk sistem yang terintegrasi, penting untuk membedakan antara business use case
(tingkat bisnis) dan system use case (tingkat sistem). Pada tingkat bisnis, proses
seperti "Melakukan pemesanan tiket secara manual di loket" dapat digantikan
dengan "Pemesanan tiket melalui aplikasi web" sebagai bentuk transformasi digital.
Firmansyah & Voutama (2024) dalam penelitiannya tentang penerapan UML
pada sistem pemesanan tiket bioskop berbasis website mengidentifikasi bahwa
business use case utama dalam sistem pemesanan tiket meliputi: registrasi calon
penonton, login pengguna dan admin, pencarian jadwal film, pemesanan tiket, serta
pelaporan transaksi. Hasil identifikasi ini sejalan dengan kebutuhan pada proyek
Cinema Booking yang mengembangkan fitur serupa.
2.2.3 Diagram Activity
Diagram activity adalah salah satu diagram UML yang digunakan untuk
memodelkan aliran kerja (workflow) atau proses bisnis secara dinamis. Dennis,
Wixom, & Roth (2019) menyatakan bahwa diagram activity sangat berguna untuk
menggambarkan urutan aktivitas dalam suatu proses, termasuk percabangan
(decision), penggabungan (merge), serta aktivitas paralel (fork dan join).
Rosa & Shalahuddin (2018) menjelaskan bahwa diagram activity memiliki simbol-
simbol utama seperti:
a. Initial node (titik awal) yang menandai dimulainya aliran.
b. Activity (aktivitas) yang digambarkan dengan persegi panjang dengan sudut
membulat.
c. Decision node (keputusan) berbentuk belah ketupat untuk percabangan
berdasarkan kondisi.
d. Fork node dan join node untuk aktivitas yang berjalan paralel.
e. Final node (titik akhir) yang menandai berakhirnya aliran.
Dalam konteks sistem Cinema Booking, diagram activity digunakan untuk
memodelkan beberapa alur utama, antara lain:
1. Alur pemesanan tiket: dimulai dari pengguna memilih film, memilih jadwal
tayang, mengisi jumlah tiket, sistem melakukan validasi stok, menampilkan
total harga, hingga konfirmasi pemesanan dan pengurangan stok.
2. Alur rating dan review: pengguna yang telah login dan memiliki riwayat tiket
yang sudah ditonton dapat memberikan rating bintang dan komentar pada film
tersebut.

3. Alur validasi pembayaran oleh admin: admin menerima bukti pembayaran via
WhatsApp, melakukan verifikasi, lalu mengubah status pesanan menjadi
"dibayar".
Prayoga et al. (2023) dalam rancang bangun aplikasi pemesanan tiket
bioskop berbasis website menggunakan diagram activity untuk menggambarkan
alur pemesanan mulai dari pengguna memilih kursi, mengisi data pemesan,
melakukan pembayaran, hingga mencetak tiket. Penelitian tersebut menjadi rujukan
bahwa diagram activity efektif untuk memodelkan proses yang melibatkan interaksi
antara pengguna dan sistem.
Pressman & Maxim (2020) menambahkan bahwa diagram activity juga dapat
dilengkapi dengan swimlane (jalur) untuk memisahkan tanggung jawab antar aktor
yang berbeda. Pada sistem Cinema Booking, swimlane dapat membedakan area
aktivitas pengguna, admin, dan sistem.
2.2.4 Usecase Sistem (System Use Case)
Use case sistem adalah diagram yang menggambarkan interaksi antara aktor
(pengguna sistem) dengan sistem itu sendiri untuk mencapai suatu tujuan
fungsional. Berbeda dengan use case bisnis yang berfokus pada proses organisasi,
use case sistem berfokus pada fungsionalitas yang harus disediakan oleh sistem
perangkat lunak (Sommerville, 2016).
Menurut Kendall & Kendall (2020), komponen utama dalam use case sistem
meliputi:
1. Aktor: entitas di luar sistem yang berinteraksi dengan sistem, dapat berupa
pengguna manusia atau sistem eksternal.
2. Use Case: deskripsi urutan tindakan yang dilakukan sistem yang menghasilkan
hasil yang terukur bagi aktor.
3. Relasi: meliputi association (hubungan antara aktor dan use case), include (use
case memanggil use case lain), extend (use case memperluas use case lain), dan
generalization (pewarisan antar aktor atau use case).
Rospricilia & Ma'ady (2024) dalam penelitiannya tentang Integration Use
Case (IUC) menekankan pentingnya notasi yang benar dalam use case diagram,
terutama untuk sistem-sistem yang terintegrasi. Mereka mengidentifikasi bahwa
kesalahan umum dalam pemodelan use case sering terjadi pada penggunaan relasi
include dan extend yang tidak tepat.

Berdasarkan analisis kebutuhan sistem Cinema Booking yang telah
dilakukan, aktor yang terlibat dalam use case sistem adalah:
1. Pengguna (Calon Penonton): aktor yang memiliki hak akses terbatas, seperti
melihat film, memesan tiket, memberikan rating, dan melihat riwayat
pemesanan.
2. Admin (Pengelola Bioskop): aktor yang memiliki hak akses penuh untuk
mengelola data film (CRUD), mengelola jadwal tayang, mengupload gambar
cover film, memvalidasi pembayaran, dan melihat laporan pemesanan.
Firmansyah & Voutama (2024) dalam jurnalnya mengidentifikasi use case
sistem untuk aplikasi pemesanan tiket bioskop yang meliputi: registrasi, login,
melihat daftar film, melihat detail film, memesan tiket, melihat riwayat pemesanan,
mengelola film, dan mengelola jadwal tayang. Penelitian ini diperkuat oleh Prayoga
et al. (2023) yang juga mengidentifikasi use case serupa dengan tambahan fitur
pencarian film berdasarkan jam tayang dan sistem rating.
Rosa & Shalahuddin (2018) menjelaskan bahwa dokumentasi flow of event
(aliran kejadian) untuk setiap use case sangat penting untuk melengkapi diagram
use case. Aliran kejadian terdiri dari:
a. Basic flow (aliran normal): menggambarkan skenario sukses ketika semua
kondisi terpenuhi.
b. Alternative flow (aliran alternatif): menggambarkan skenario lain jika terjadi
kondisi tertentu.
c. Exception flow (aliran pengecualian): menggambarkan skenario jika terjadi
kesalahan atau kondisi gagal.
Sebagai contoh, untuk use case "Memesan Tiket", aliran normalnya adalah
pengguna memilih film, memilih jadwal, mengisi jumlah tiket, sistem memvalidasi
stok, dan menyimpan pemesanan. Aliran alternatif terjadi jika stok tiket tidak
mencukupi, sistem akan menampilkan pesan error dan meminta pengguna
mengurangi jumlah tiket.
Nasikhin, Putra, & Pramono (2019) dalam penelitiannya tentang analisis dan
perancangan sistem informasi reservasi menggunakan metode OOAD menegaskan
bahwa use case diagram merupakan fondasi awal dalam pemodelan sistem
berorientasi objek. Mereka menggunakan use case diagram untuk mengidentifikasi
kebutuhan fungsional sebelum melanjutkan ke tahap pembuatan diagram sequence,
class, dan statechart.

2.3 OOAD
2.3.1 Pengertian OOAD
Object-Oriented Analysis and Design (OOAD) adalah pendekatan dalam
rekayasa perangkat lunak yang menggunakan konsep-konsep berorientasi objek
untuk menganalisis kebutuhan sistem dan merancang solusinya. Menurut Pressman
& Maxim (2020), OOAD merupakan metodologi yang memandang sistem sebagai
kumpulan objek-objek yang saling berinteraksi, di mana setiap objek memiliki data
(atribut) dan perilaku (method) yang terenkapsulasi di dalamnya.
Rosa & Shalahuddin (2018) menjelaskan bahwa analisis berorientasi objek
(Object-Oriented Analysis / OOA) berfokus pada pemahaman domain masalah dan
identifikasi kelas-kelas serta relasi yang relevan dengan sistem, sedangkan desain
berorientasi objek (Object-Oriented Design / OOD) berfokus pada bagaimana
kelas-kelas tersebut diimplementasikan ke dalam sistem perangkat lunak yang akan
dibangun.
Sommerville (2016) menambahkan bahwa keunggulan utama OOAD
dibandingkan pendekatan terstruktur adalah kemampuannya dalam menangani
kompleksitas sistem, mendukung reusability (penggunaan ulang kode), serta
memudahkan pemeliharaan sistem karena perubahan pada satu objek tidak terlalu
berdampak pada objek lainnya.
2.3.2 Konsep Dasar OOAD
Menurut Kendall & Kendall (2020), terdapat empat konsep dasar dalam
pendekatan berorientasi objek yang menjadi fondasi OOAD, yaitu:
1. Enkapsulasi (Encapsulation) : Konsep yang menyembunyikan detail
implementasi internal suatu objek dari objek lain. Objek hanya mengekspos
interface publik yang diperlukan untuk berinteraksi. Hal ini meningkatkan
keamanan dan kemudahan pemeliharaan sistem (Pressman & Maxim, 2020).
2. Pewarisan (Inheritance) : Mekanisme di mana suatu kelas dapat mewarisi
atribut dan method dari kelas lain yang lebih umum. Kelas yang mewarisi
disebut subclass atau child class, sedangkan kelas yang diwarisi disebut
superclass atau parent class. Inheritance mendukung konsep reusability (Rosa
& Shalahuddin, 2018).
3. Polimorfisme (Polymorphism) : Kemampuan suatu objek untuk memiliki
banyak bentuk atau merespon pesan yang sama dengan cara yang berbeda.
Polimorfisme memungkinkan satu interface digunakan untuk berbagai
implementasi yang berbeda (Sommerville, 2016).

|     |     |     |
| --- | --- | --- |

4.  Asosiasi (Association) : Relasi antar kelas yang menggambarkan bagaimana
objek-objek saling terhubung. Asosiasi dapat berupa one-to-one, one-to-many,
atau many-to-many (Dennis, Wixom, & Roth, 2019).

|     |     |     |
| --- | --- | --- |

BAB III
METODOLOGI PENELITIAN
3.1 Pemodelan Bisnis
Pemodelan bisnis merupakan tahap awal dalam rekayasa perangkat lunak yang
bertujuan untuk memahami proses bisnis yang terjadi dalam suatu organisasi sebelum
sistem baru dibangun. Menurut Kendall & Kendall (2020), pemodelan bisnis membantu
mengidentifikasi kebutuhan organisasi, masalah yang ada, serta ruang lingkup solusi
yang akan dikembangkan.
Pada pengembangan aplikasi web Cinema Booking untuk bioskop sederhana,
pemodelan bisnis dilakukan melalui beberapa tahapan, yaitu penentuan ruang lingkup,
identifikasi masalah, pemodelan use case bisnis, diagram activity, dan identifikasi
business entity.
3.1.1 Hasil wawancara, observasi, dan studi pustaka
Berdasarkan hasil wawancara dan observasi yang dilakukan terhadap proses
pemesanan tiket pada bioskop sederhana, diperoleh informasi bahwa penyampaian
informasi film dan jadwal tayang masih memiliki beberapa kendala. Calon penonton
sering mengalami kesulitan dalam memperoleh informasi mengenai film yang
sedang tayang, jadwal penayangan, serta ketersediaan tiket tanpa harus datang
langsung ke lokasi bioskop. Selain itu, proses pemesanan tiket yang dilakukan secara
langsung di loket menyebabkan terjadinya antrian pada jam-jam tertentu, terutama
ketika terdapat film yang sedang diminati oleh banyak penonton.
Dari sisi pengelola bioskop, pengelolaan data film, jadwal tayang, dan
transaksi pemesanan masih dilakukan secara sederhana sehingga berpotensi
menimbulkan kesalahan pencatatan dan keterlambatan pembaruan informasi.
Pengelola juga mengalami kesulitan dalam memantau jumlah tiket yang telah terjual
dan jumlah tiket yang masih tersedia untuk setiap jadwal penayangan.
Hasil studi pustaka menunjukkan bahwa pemanfaatan aplikasi berbasis web
dapat membantu meningkatkan efisiensi pelayanan dengan menyediakan informasi
yang dapat diakses secara online, mempermudah proses pemesanan tiket, serta
membantu pengelolaan data secara terpusat. Oleh karena itu, dikembangkan aplikasi
Cinema Booking sebagai solusi untuk mendukung proses pemesanan tiket dan
pengelolaan operasional bioskop secara lebih efektif.
3.1.2 Identifikasi Masalah (Tabel Masalah, Dampak, Solusi)
Identifikasi masalah merupakan tahap awal dalam pemodelan bisnis yang
bertujuan untuk menemukan dan menganalisis kelemahan-kelemahan yang terdapat

pada sistem yang sedang berjalan. Menurut Kendall & Kendall (2020), identifikasi
masalah yang komprehensif akan menghasilkan pemahaman yang mendalam
tentang akar permasalahan sehingga solusi yang dirancang dapat tepat sasaran.
Sommerville (2016) juga menambahkan bahwa identifikasi masalah melibatkan
berbagai pihak terkait (stakeholder) seperti pengguna, pengelola sistem, dan
pengembang untuk mendapatkan perspektif yang beragam.
Pada proyek pengembangan aplikasi web Cinema Booking untuk bioskop
sederhana, identifikasi masalah dilakukan melalui beberapa metode:
1. Studi literatur terhadap jurnal dan penelitian terkait sistem pemesanan tiket
bioskop.
2. Wawancara dengan product owner (Dewan Direksi Cinema Booking), scrum
master (Chief Technology Officer Cinema Booking), dan stakeholder
(Pengunjung Bioskop, Development Team, praktisi IT).
3. Observasi terhadap proses pemesanan tiket konvensional yang masih berjalan.
Berdasarkan hasil identifikasi tersebut, ditemukan beberapa permasalahan
yang dikelompokkan berdasarkan pihak-pihak yang terdampak, yaitu: calon
penonton (pengguna), pengelola bioskop (admin), dan sistem itu sendiri.
Firmansyah & Voutama (2024) dalam penelitiannya tentang penerapan UML
pada sistem pemesanan tiket bioskop berbasis website mengidentifikasi masalah
serupa, seperti calon penonton harus datang langsung ke bioskop untuk mengetahui
jadwal, antrean panjang di loket, dan pengelola kesulitan mengelola data film secara
manual. Prayoga et al. (2023) juga menambahkan bahwa kurangnya informasi
ketersediaan tiket secara real-time menjadi kendala bagi calon penonton.
Seluruh permasalahan yang berhasil diidentifikasi tersebut dirangkum dalam
Tabel 3.1 berikut ini, yang memuat tiga komponen utama yaitu masalah yang terjadi,
solusi yang diusulkan untuk mengatasi masalah, serta dampak yang akan diperoleh
setelah solusi diterapkan.
Tabel 3.1. Identifikasi Masalah Cinema Booking
Masalah Solusi Dampak
Calon penonton harus datang Membangun aplikasi web yang Memudahkan calon
langsung ke bioskop untuk menampilkan daftar film beserta penonton mengakses
mengetahui jadwal film yang jadwal tayang secara online informasi kapan saja dan
sedang tayang di mana saja

Calon penonton sering Menyediakan fitur pemesanan Mengurangi antrean di
kehabisan tiket karena harus tiket online sehingga calon loket dan menjamin
antre panjang di loket bioskop penonton dapat memesan tiket ketersediaan tiket bagi
dari rumah yang sudah memesan
Pengelola bioskop kesulitan Menyediakan halaman admin Memudahkan pengelola
mengelola data film dan untuk mengelola data film bioskop dalam
jadwal secara manual (tambah, edit, hapus) dan jadwal mengupdate informasi
tayang film
Pengguna tidak mengetahui Menampilkan sisa tiket yang Pengguna dapat
sisa tiket yang tersedia untuk tersedia secara real-time pada memutuskan untuk
suatu jadwal tayang halaman detail film memesan sebelum tiket
habis, meningkatkan
transparansi informasi
Pengguna kesulitan mencari Menyediakan fitur filter/pencarian Pengguna dapat langsung
film berdasarkan jam tayang film berdasarkan jam tayang (pagi, melihat film yang tayang
yang sesuai dengan waktu siang, sore, malam) di halaman pada jam yang diinginkan
luang mereka utama tanpa harus membuka satu
per satu film
Pengguna tidak memiliki Menyediakan fitur rating bintang Pengguna dapat melihat
referensi yang cukup untuk (1-5) dan review teks yang dapat kualitas film dari ulasan
memutuskan film mana yang diberikan oleh pengguna yang pengguna lain sebelum
akan ditonton karena tidak ada sudah menonton film tersebut memutuskan menonton
rating/review
Rating/review bisa diberikan Sistem hanya mengizinkan Rating dan review menjadi
oleh siapa saja (termasuk yang pengguna yang memiliki riwayat lebih kredibel dan dapat
belum menonton), sehingga pemesanan dengan status dipercaya oleh calon
tidak mencerminkan kualitas "dibayar" atau "selesai" untuk penonton lainnya
film sebenarnya memberikan rating dan review
Dengan adanya identifikasi masalah yang komprehensif ini, tahap
selanjutnya adalah melakukan pemodelan bisnis yang mencakup identifikasi aktor,
business worker, use case bisnis, serta diagram activity untuk menggambarkan alur
proses bisnis yang akan dirancang.
3.1.3 Usecase Bisnis
Business use case atau use case bisnis adalah representasi dari proses-proses
bisnis yang terjadi dalam suatu organisasi, tanpa mempertimbangkan teknologi
sistem yang akan dibangun. Menurut Kendall & Kendall (2020), use case bisnis
menggambarkan interaksi antara business actor (pelaku bisnis) dengan business
worker (pekerja bisnis) untuk mencapai tujuan bisnis tertentu. Rospricilia & Ma'ady
(2024) menjelaskan bahwa dalam pemodelan use case untuk sistem yang

terintegrasi, penting untuk membedakan antara business use case (tingkat bisnis) dan
system use case (tingkat sistem).
Pada pengembangan aplikasi web Cinema Booking untuk bioskop sederhana,
pemodelan use case bisnis dilakukan untuk memahami alur proses bisnis yang
sedang berjalan sebelum sistem diimplementasikan. Hal ini penting agar sistem yang
dibangun benar-benar sesuai dengan kebutuhan bisnis bioskop.
A. Identifikasi Aktor
Business actor adalah pihak-pihak di luar organisasi yang berinteraksi
dengan proses bisnis namun tidak termasuk sebagai bagian dari organisasi itu
sendiri. Menurut Rosa & Shalahuddin (2018), aktor bisnis dapat berupa
pelanggan, pemasok, atau pihak eksternal lainnya yang memicu atau menerima
hasil dari suatu proses bisnis.
Berdasarkan analisis proses bisnis pemesanan tiket pada bioskop
sederhana, berikut adalah Tabel 3.2 Identifikasi Business actor yang terlibat:
Tabel 3.2. Identifikasi Business actor
Aktor Deskripsi Peran
- Melihat daftar film
- Melihat detail film
Individu yang ingin mencari - Memesan tiket
Pengguna (Calon Penonton) informasi film dan memesan - Memberi rating & review
tiket secara online - Melihat riwayat pemesanan
- Melakukan pembayaran via
WhatsApp
- Menawarkan film baru ke
bioskop
Pihak yang menyediakan atau - Menentukan jadwal rilis film
Pemasok Film (film
mendistribusikan film ke - Memberikan lisensi
Distributor/Supplier)
bioskop penayangan film
- Menentukan harga minimum
tiket
Firmansyah & Voutama (2024) dalam penelitiannya mengidentifikasi
bahwa aktor utama dalam sistem pemesanan tiket bioskop berbasis web adalah
pengguna (calon penonton) dan admin (pengelola).
B. Identifikasi Business Worker

Business worker adalah pihak-pihak di dalam organisasi yang
berinteraksi atau terlibat dalam proses bisnis organisasi. Menurut Dennis,
Wixom, & Roth (2019), business worker adalah individu atau peran di dalam
perusahaan (karyawan, manajer, dll.) yang bertanggung jawab menjalankan
proses bisnis. Tujuannya adalah untuk mengetahui siapa saja peranan dalam
organisasi yang terlibat di dalam proses bisnis organisasi serta bagaimana
mereka berinteraksi dengan proses bisnis tersebut.
Berdasarkan analisis proses bisnis pada bioskop sederhana setelah
implementasi sistem web Cinema Booking, berikut adalah Tabel 3.3 identifikasi
business worker pada sistem Cinema Booking yang terlibat:
Tabel 3.3 Identifikasi Business Worker
Peranan dalam Proses
Business Worker Deskripsi
Bisnis
- Mengelola data film
(tambah, edit, hapus, upload
poster)
- Mengelola jadwal tayang
film
- Memvalidasi bukti
Karyawan yang bertugas pembayaran dari pengguna
Admin (Pengelola Bioskop) mengelola sistem web via WhatsApp
Cinema Booking - Mengubah status
pemesanan (menunggu
pembayaran → menunggu
validasi → dibayar)
- Melihat dan mengekspor
laporan pemesanan (harian,
film terlaris, pendapatan)
- Menentukan jadwal tayang
film
Karyawan yang bertugas
Pengelola Data Film (Film - Menentukan harga tiket per
menentukan film dan jadwal
Manager) film
yang akan ditayangkan
- Berkoordinasi dengan
pemasok film
- Mengawasi kinerja admin
dalam mengelola sistem
Karyawan yang bertugas
Manajer Operasional - Menyusun laporan berkala
mengawasi operasional
(Operational Manager) untuk pimpinan
bioskop
- Mengatasi keluhan
pelanggan
- Menetapkan harga tiket
Pimpinan atau dewan direksi - Menyetujui jadwal tayang
Pimpinan Bioskop (Cinema
yang menetapkan kebijakan film
Director)
bisnis - Mengawasi kinerja
bioskop secara keseluruhan

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

C. Identifikasi Usecase Business
Use case business adalah aktivitas utama organisasi (fungsi bisnis) yang
dilakukan oleh organisasi sebagai respons terhadap permintaan aktor. Menurut
Pressman & Maxim (2020), penulisan use case business diawali dengan kata
kerja dan merupakan proses bisnis lengkap yang memberikan nilai nyata bagi
aktor, bukan aktivitas teknis kecil. Tujuannya adalah untuk mengetahui apa saja
yang dilakukan atau dikerjakan oleh organisasi.
Berdasarkan identifikasi aktor dan business worker di atas, berikut adalah
tabel 3.4 identifikasi Usecase Business pada sistem Cinema Booking:
Tabel 3.4 Identifikasi Usecase Business
| Usecase Business  | Deskripsi  | Aktor Terkait  | Business Worker  |     |
| ----------------- | ---------- | -------------- | ---------------- | --- |
Terkait
Bioskop menyediakan
| Menyediakan       | informasi film yang    |                  |                   |     |
| ----------------- | ---------------------- | ---------------- | ----------------- | --- |
|                   |                        | Pengguna (Calon  | Admin, Pengelola  |     |
| Informasi Jadwal  | sedang tayang beserta  |                  |                   |     |
|                   |                        | Penonton)        | Data Film         |     |
| Film Online       | jadwalnya melalui      |                  |                   |     |
aplikasi web
Bioskop menyediakan
fitur pemesanan tiket
Menyediakan
|                  | melalui aplikasi web     | Pengguna (Calon  |        |     |
| ---------------- | ------------------------ | ---------------- | ------ | --- |
| Pemesanan Tiket  |                          |                  | Admin  |     |
|                  | sehingga calon penonton  | Penonton)        |        |     |
Online
dapat memesan dari
rumah
Bioskop menerima
pembayaran tiket dari
Menerima
|                 | calon penonton melalui  | Pengguna (Calon  |        |     |
| --------------- | ----------------------- | ---------------- | ------ | --- |
| Pembayaran via  |                         |                  | Admin  |     |
|                 | transfer manual yang    | Penonton)        |        |     |
WhatsApp
dikonfirmasi via
WhatsApp
Bioskop
menyelenggarakan
| Menyelenggarakan  | penayangan film di  | Pengguna (Calon  |     |     |
| ----------------- | ------------------- | ---------------- | --- | --- |
Manajer Operasional
| Penayangan Film  | studio sesuai dengan  | Penonton)  |     |     |
| ---------------- | --------------------- | ---------- | --- | --- |
jadwal yang telah
ditentukan
Bioskop mengelola data
|     | film yang akan  |     | Admin, Pengelola  |     |
| --- | --------------- | --- | ----------------- | --- |
Mengelola Data
|     | ditayangkan, termasuk  | Pemasok Film  | Data Film, Pimpinan  |     |
| --- | ---------------------- | ------------- | -------------------- | --- |
Film dan Jadwal
|     | jadwal, harga tiket, dan  |     | Bioskop  |     |
| --- | ------------------------- | --- | -------- | --- |
poster film
Bioskop menyusun
| Menyusun   | laporan pemesanan tiket  |           |                 |     |
| ---------- | ------------------------ | --------- | --------------- | --- |
|            |                          | Pimpinan  | Admin, Manajer  |     |
| Laporan    | secara berkala untuk     |           |                 |     |
|            |                          | Bioskop   | Operasional     |     |
| Pemesanan  | keperluan evaluasi       |           |                 |     |
bisnis
| Memvalidasi  | Bioskop memverifikasi  |     |     |     |
| ------------ | ---------------------- | --- | --- | --- |
Pengguna (Calon
| Pembayaran  | bukti pembayaran yang  |     | Admin  |     |
| ----------- | ---------------------- | --- | ------ | --- |
Penonton)
| Pengguna  | dikirim pengguna dan  |     |     |     |
| --------- | --------------------- | --- | --- | --- |
|           |                       |     |     |     |

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

mengupdate status
pemesanan
Bioskop menangani
| Menangani  | keluhan dari calon  |     |     |     |
| ---------- | ------------------- | --- | --- | --- |
Pengguna (Calon
| Keluhan  | penonton terkait  |     | Manajer Operasional  |     |
| -------- | ----------------- | --- | -------------------- | --- |
Penonton)
| Pelanggan  | pelayanan, pemesanan,  |     |     |     |
| ---------- | ---------------------- | --- | --- | --- |
atau tiket
D. Diagram Usecase Business
Diagram  use  case  business  adalah  representasi  grafis  yang
menggambarkan interaksi antara business actor (pihak eksternal) dan business
worker (pihak internal) dalam menjalankan business use case (proses bisnis).
Menurut  Sommerville  (2016),  diagram  use  case  business  berguna  untuk
memvisualisasikan cakupan proses bisnis dan komunikasi antar pihak yang
terlibat.
Diagram use case business pada sistem Cinema Booking (proses bisnis bioskop
setelah implementasi web) digambarkan sebagai berikut:

Gambar 3.1 Usecase Diagram
Dari diagram Usecase Business di atas, dapat dijelaskan bahwa:
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

1. Pengguna (Calon Penonton) sebagai aktor eksternal utama berinteraksi
dengan 6 use case: mencari informasi jadwal, memesan tiket, melakukan
pembayaran via WA, menonton film, meminta validasi pembayaran, dan
menyampaikan keluhan.
2. Pemasok Film berinteraksi dengan 1 use case: menyediakan data film baru
yang akan dikelola oleh bioskop.
3. Pimpinan Bioskop berinteraksi dengan 1 use case: menerima laporan
pemesanan untuk evaluasi bisnis.
4. Admin sebagai business worker internal memiliki peran paling banyak,
yaitu mengelola 6 use case yang berkaitan dengan operasional web
(informasi, pemesanan, pembayaran, manajemen data, laporan, validasi).
5. Pengelola Data Film hanya fokus pada 1 use case yaitu mengelola data film
dan jadwal.
6. Manajer Operasional bertanggung jawab pada 3 use case: penayangan
film, laporan, dan keluhan pelanggan.
3.1.4 Diagram Activity
Diagram activity adalah salah satu diagram UML yang digunakan untuk
memodelkan aliran kerja (workflow) atau proses bisnis secara dinamis. Menurut
Dennis, Wixom, & Roth (2019), diagram activity sangat berguna untuk
menggambarkan urutan aktivitas dalam suatu proses, termasuk percabangan
(decision), penggabungan (merge), serta aktivitas paralel (fork dan join). Rosa &
Shalahuddin (2018) menjelaskan bahwa diagram activity memiliki simbol-simbol
utama seperti initial node (titik awal), activity (aktivitas), decision node (keputusan),
fork node dan join node untuk aktivitas paralel, serta final node (titik akhir).
Pada pengembangan aplikasi web Cinema Booking, diagram activity
digunakan untuk memodelkan alur proses bisnis yang terjadi dalam sistem. Berikut
adalah diagram activity untuk beberapa proses utama:
A. Diagram Activity Pemesanan Tiket
Diagram activity ini menggambarkan alur pemesanan tiket mulai dari
pengguna membuka halaman web hingga pemesanan berhasil.

Gambar 3.2 Activity Diagram Pemesanan Tiket
Alur:
1. Tahap Awal: Pengguna membuka web dan melihat daftar film.
2. Tahap Pemilihan: Pengguna memilih film, jadwal tayang, dan kursi.
Terdapat validasi ketersediaan kursi (jika full, pengguna harus memilih
kursi lain).
3. Tahap Konfirmasi: Pengguna mengkonfirmasi pesanan setelah melihat
total harga dan barcode pembayaran.
4. Tahap Pembayaran: Pengguna melakukan transfer ke admin dan
mengirim bukti transfer via WhatsApp.
5. Tahap Validasi Admin: Admin memverifikasi pembayaran. Jika tidak
dikonfirmasi, pesanan batal. Jika dikonfirmasi, pesanan diproses.
6. Tahap Akhir: Sistem menyimpan pesanan ke database dan menerbitkan
tiket digital.
B. Diagram Activity Validasi Pembayaran oleh Admin
Diagram activity ini menggambarkan alur admin memvalidasi
pembayaran dari pengguna setelah pengguna melakukan transfer via WhatsApp.

Gambar 3.3 Diagram Activity Validasi Pembayaran oleh Admin
Gambar diagram activity validasi pembayaran di atas menunjukkan alur
yang dimulai dari admin login ke dashboard. Sistem menampilkan daftar
pesanan masuk, lalu admin memilih pesanan dengan status "menunggu validasi".
Sistem menampilkan detail pesanan dan bukti pembayaran. Admin kemudian
memverifikasi bukti pembayaran dan mengubah status pemesanan menjadi
"dibayar". Sistem mengupdate status pemesanan di database dan menampilkan
notifikasi bahwa status telah berhasil diupdate. Alur berakhir setelah notifikasi
ditampilkan.
C. Diagram Activity Memberi Rating & Review
Diagram activity ini menggambarkan alur pengguna memberikan rating
dan review pada film yang sudah ditonton.

Gambar 3.4 Diagram Activity Memberi Rating & Review
Gambar diagram activity memberi rating & review di atas menunjukkan
alur yang dimulai dari pengguna login ke aplikasi. Pengguna membuka halaman
riwayat pemesanan, sistem menampilkan daftar tiket yang pernah dipesan.
Pengguna memilih film yang sudah ditonton (status "dibayar" atau "selesai"),
kemudian sistem menampilkan form rating & review.
Pengguna memilih rating bintang (1-5), menulis review teks (opsional),
dan menekan tombol "Kirim Review". Sistem memvalidasi hak rating untuk
memastikan pengguna sudah menonton film tersebut.
Terdapat percabangan (decision node):
• Jika valid: Sistem menyimpan rating & review ke database, memperbarui
rata-rata rating film, dan menampilkan notifikasi "Review berhasil dikirim".
• Jika tidak valid: Sistem menampilkan pesan error "Anda belum menonton
film ini" dan alur berakhir.
3.1.5 Business Entity
Business Entity merupakan objek atau data utama yang digunakan dan dikelola
dalam proses bisnis. Menurut pendekatan OOAD, business entity berfungsi sebagai
representasi informasi yang dibutuhkan oleh organisasi untuk mendukung aktivitas bisnis.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Berdasarkan hasil identifikasi business actor, business worker, use case bisnis, serta
activity diagram pada sistem Cinema Booking, diperoleh beberapa business entity yang
berperan  dalam  proses  pemesanan  tiket  film,  pengelolaan  jadwal,  pembayaran,  dan
pelaporan.
Tabel 3.5 Identifikasi Business Entity
|     | Business Entity  |     | Deskripsi  | Atribut Utama  |     |
| --- | ---------------- | --- | ---------- | -------------- | --- |
Pengguna  Data calon penonton yang  id_pengguna, nama, email,
|     |     | menggunakan layanan  |     | password, no_telepon  |     |
| --- | --- | -------------------- | --- | --------------------- | --- |
Cinema Booking untuk
melihat film dan melakukan
pemesanan tiket.
|     | Film  | Data film yang ditayangkan  |     | id_film, judul, sinopsis,  |     |
| --- | ----- | --------------------------- | --- | -------------------------- | --- |
oleh bioskop.
genre, durasi, harga_tiket,
poster
|     | Jadwal Tayang  |                            | Informasi jadwal  | id_jadwal, id_film,          |     |
| --- | -------------- | -------------------------- | ----------------- | ---------------------------- | --- |
|     |                | penayangan setiap film di  |                   | tanggal_tayang, jam_tayang,  |     |
|     |                |                            | bioskop.          | studio, kapasitas_kursi      |     |
Pemesanan
|     |     | Data transaksi pemesanan   |            | id_pemesanan,               |     |
| --- | --- | -------------------------- | ---------- | --------------------------- | --- |
|     |     | tiket yang dilakukan oleh  |            | id_pengguna, id_jadwal,     |     |
|     |     |                            | pengguna.  | jumlah_tiket, total_harga,  |     |
tanggal_pemesanan,
status_pemesanan
Tiket
|     |     | Bukti pemesanan yang  |                      | id_tiket, id_pemesanan,     |     |
| --- | --- | --------------------- | -------------------- | --------------------------- | --- |
|     |     |                       | diterbitkan setelah  | kode_tiket, tanggal_terbit  |     |
pembayaran berhasil
diverifikasi.
Pembayaran
|     |     | Data pembayaran yang  |            | id_pembayaran,     |     |
| --- | --- | --------------------- | ---------- | ------------------ | --- |
|     |     | dikirimkan pengguna   |            | id_pemesanan,      |     |
|     |     | melalui transfer dan  |            | tanggal_bayar,     |     |
|     |     | dikonfirmasi melalui  |            | bukti_pembayaran,  |     |
|     |     |                       | WhatsApp.  | status_validasi    |     |
Rating dan Review
|     |     | Data penilaian dan ulasan  |     | id_review, id_pengguna,     |     |
| --- | --- | -------------------------- | --- | --------------------------- | --- |
|     |     | yang diberikan pengguna    |     | id_film, rating, komentar,  |     |
|     |     | terhadap film yang telah   |     | tanggal_review              |     |
ditonton.
Laporan Pemesanan  Data rekapitulasi transaksi  id_laporan, periode,
|     |               | yang digunakan untuk      |                     | total_pemesanan,       |     |
| --- | ------------- | ------------------------- | ------------------- | ---------------------- | --- |
|     |               | keperluan evaluasi dan    |                     | total_pendapatan,      |     |
|     |               |                           | monitoring bisnis.  | film_terlaris          |     |
|     | Pemasok Film  | Data distributor atau     |                     | id_pemasok,            |     |
|     |               | pemasok yang menyediakan  |                     | nama_pemasok, kontak,  |     |
film kepada bioskop.  alamat

3.2 Analisis Sistem
Analisis  sistem  merupakan  tahap  untuk  mengidentifikasi  dan  menganalisis
kebutuhan-kebutuhan yang harus dipenuhi oleh sistem yang akan dibangun. Menurut
Pressman  &  Maxim  (2020),  analisis  sistem  bertujuan  untuk  memahami  kebutuhan
pengguna secara mendalam sehingga sistem yang dikembangkan benar-benar sesuai
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

dengan harapan pengguna. Sommerville (2016) juga menambahkan bahwa analisis sistem
meliputi identifikasi fungsi-fungsi sistem, identifikasi data yang dikelola, serta identifikasi
pengguna yang akan menggunakan sistem.
Pada pengembangan aplikasi web Cinema Booking, analisis sistem dilakukan
berdasarkan hasil identifikasi masalah, wawancara dengan product owner dan stakeholder,
serta studi literatur. Hasil analisis ini akan digunakan sebagai dasar untuk menyusun
product backlog dan sprint backlog dalam metode Scrum.
3.2.1 Analisa kebutuhan Fungsi
Analisa kebutuhan fungsi bertujuan untuk mengidentifikasi fitur-fitur apa
saja yang harus disediakan oleh sistem berdasarkan kebutuhan pengguna (calon
penonton) dan admin (pengelola bioskop). Menurut Kendall & Kendall (2020),
kebutuhan fungsi (functional requirements) adalah pernyataan tentang apa yang
harus dilakukan sistem, termasuk bagaimana sistem harus bereaksi terhadap input
tertentu dan bagaimana perilaku sistem dalam situasi tertentu.
Firmansyah & Voutama (2024) dalam penelitiannya tentang sistem
pemesanan tiket bioskop berbasis website mengidentifikasi bahwa kebutuhan fungsi
utama meliputi registrasi, login, manajemen film, pemesanan tiket, dan pelaporan.
Prayoga et al. (2023) menambahkan bahwa kebutuhan fungsi seperti rating, review,
dan validasi pembayaran juga penting untuk meningkatkan kualitas layanan.
Berdasarkan analisis kebutuhan sistem Cinema Booking, berikut adalah tabel
3.6 analisa kebutuhan fungsi yang terbagi berdasarkan jenis pengguna:
Tabel 3.6 Analisa Kebutuhan Fungsi
Pengguna Kebutuhan Fungsi
Registrasi akun
Login ke apliasi
Melihat daftar film yang sedang tayang
Melihat detail film (sinopsis, durasi, harga, jadwal, sisa
tiket, rating)
Filter film berdasarkan jam tayang (pagi, siang, sore,
Pengguna (Calon Penonton)
malam)
Memesan tiket (memilih film, jadwal, jumlah tiket)
Melihat sisa tiket secara real-time
Melihat total harga otomatis berdasarkan jumlah tiket
Melakukan pembayaran via WhatsApp (mendapatkan
nomor admin)
Memberi rating & review pada film yang sudah ditonton
Melihat riwayat pemesanan
Admin (Pengelola Bioskop) Login sebagai admin

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Menambah data film baru (termasuk upload poster/cover)
Mengedit data film
Menghapus data film
Mengelola jadwal tayang (tambah, edit, hapus)
Melihat daftar pesanan yang masuk
Memvalidasi pembayaran pengguna (ubah status pesanan)
|     | Melihat  | laporan  | pemesanan  | (harian,  | film  terlaris,  |     |
| --- | -------- | -------- | ---------- | --------- | ---------------- | --- |
pendapatan)
Mengekspor laporan ke PDF/Excel
Validasi ketersediaan tiket sebelum pemesanan
Menampilkan total harga berdasarkan jumlah tiket
| Sistem   | Mengurangi stok tiket setelah pemesanan  |      |                 |           |              |     |
| -------- | ---------------------------------------- | ---- | --------------- | --------- | ------------ | --- |
|          | Validasi                                 | hak  | rating  (hanya  | pengguna  | yang  sudah  |     |
menonton yang bisa rating)
Menampilkan rata-rata rating pada setiap film
3.2.2 Story Product Backlog
Product  backlog  adalah  daftar  prioritas  dari  fitur-fitur  atau  kebutuhan
fungsional yang akan dikerjakan dalam pengembangan sistem. Menurut Rosa &
Shalahuddin  (2018),  product  backlog  berisi  story  (cerita  pengguna),  estimasi
tingkat  kesulitan,  dan  prioritas  pengerjaan.  Dennis,  Wixom,  &  Roth  (2019)
menambahkan bahwa product backlog bersifat dinamis dan dapat berubah sesuai
dengan masukan dari product owner.
Berdasarkan analisis kebutuhan fungsi pada Tabel 3.5, berikut adalah tabel
3.7 story product backlog untuk sistem Cinema Booking:
Tabel 3.7 Story Product Backlog
Estimasi (Tingkat
| ID  | Story  |     |     |     | Prioritas  |     |
| --- | ------ | --- | --- | --- | ---------- | --- |
Kesulitan)
| 1  Membuat sistem registrasi akun pengguna  |     |     |     | 2   | 1   |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- |
(calon penonton)
| 2  Membuat fitur login untuk pengguna (calon  |     |     |     | 2   | 2   |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- |
penonton)
| 3   |     |     |     | 2   | 3   |     |
| --- | --- | --- | --- | --- | --- | --- |
Membuat fitur login untuk admin bioskop
| 4   |     |     |     | 1   | 4   |     |
| --- | --- | --- | --- | --- | --- | --- |
Membuat user interface halaman daftar film
| 5  Membuat user interface halaman detail film  |     |     |     | 1   | 5   |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                                |     |     |     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |

Membuat halaman daftar film yang sedang
| 6   |     | 2   | 6   |
| --- | --- | --- | --- |
tayang
Membuat halaman detail film beserta jadwal
| 7   |     | 2   | 7   |
| --- | --- | --- | --- |
tayang
| 8   |     | 3   | 8   |
| --- | --- | --- | --- |
Membuat fitur pemesanan tiket
Membuat fitur yang menampilkan sisa
| 9   |     | 3   | 9   |
| --- | --- | --- | --- |
ketersediaan tiket secara real-time
Membuat fitur perhitungan harga berdasarkan
| 10  |     | 2   | 10  |
| --- | --- | --- | --- |
jumlah tiket
Membuat fitur pengurangan stok tiket setelah
| 11  |     | 3   | 11  |
| --- | --- | --- | --- |
pemesanan berhasil
Membuat halaman riwayat pemesanan
| 12  |     | 2   | 12  |
| --- | --- | --- | --- |
pengguna
Membuat fitur manajemen data film (admin) -
| 13  |     | 3   | 13  |
| --- | --- | --- | --- |
CRUD
| 14  Membuat fitur manajemen jadwal tayang film  |     | 3   | 14  |
| ----------------------------------------------- | --- | --- | --- |
(admin) - CRUD
Membuat halaman daftar pesanan masuk
| 15  |     | 2   | 15  |
| --- | --- | --- | --- |
(admin)
Membuat fitur upload gambar poster/cover film
| 16  |     | 2   | 16  |
| --- | --- | --- | --- |
(admin)
Membuat fitur filter film berdasarkan jam
| 17  |     | 2   | 17  |
| --- | --- | --- | --- |
tayang (pagi, siang, sore, malam)
| 18  Membuat fitur rating & review film (pengguna)  |     | 3   | 18  |
| -------------------------------------------------- | --- | --- | --- |
Membuat fitur validasi hak rating (hanya yang
| 19  |     | 2   | 19  |
| --- | --- | --- | --- |
sudah menonton)
Membuat fitur pembayaran via WhatsApp
| 20  |     | 2   | 20  |
| --- | --- | --- | --- |
(menampilkan nomor admin)
Membuat fitur validasi pembayaran oleh admin
| 21  |     | 2   | 21  |
| --- | --- | --- | --- |
(ubah status pemesanan)
Membuat fitur laporan pemesanan admin
| 22  |     | 3   | 22  |
| --- | --- | --- | --- |
(harian, film terlaris, pendapatan)
|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     | Jumlah  |     | 48  |     |     |
| --- | ------- | --- | --- | --- | --- |
3.2.3 Sprint Backlog (dan pembagian sprint nya)
Sprint backlog adalah daftar story dari product backlog yang dipilih untuk
dikerjakan dalam satu iterasi (sprint). Menurut Pressman & Maxim (2020), sprint
backlog  disusun  berdasarkan  prioritas  dan  kesepakatan  dalam  sprint  planning
meeting antara product owner, scrum master, dan development team. Sommerville
(2016) menambahkan bahwa sprint backlog berisi story yang sudah dipecah menjadi
tugas-tugas yang lebih kecil dan dapat diselesaikan dalam satu sprint (biasanya 1-2
minggu).
Berdasarkan dokumen Scrum Cinema, ditentukan bahwa pengembangan
sistem ini dilakukan dalam 2 kali iterasi (sprint). Berikut adalah pembagian sprint
backlog untuk masing-masing iterasi:
Sprint Planning Iterasi Pertama
Sprint planning pada iterasi pertama dilakukan bersama product owner untuk
menentukan sprint goal dan memilih fitur prioritas tinggi dari product backlog.
Sprint ini difokuskan pada pembangunan pondasi sistem aplikasi pemesanan tiket
film (Cinema Booking), termasuk sistem autentikasi, tampilan utama aplikasi, serta
fitur dasar penayangan informasi film.
Sprint Goal Iterasi Pertama yaitu, membangun sistem dasar aplikasi yang
dapat  digunakan  oleh  pengguna  untuk  melihat  informasi  film  dan  melakukan
autentikasi akun.
Tabel 3.8 Sprint Backlog – Iterasi 1
ID
|     | Story  | Fungsi  |     | Tujuan  |     |
| --- | ------ | ------- | --- | ------- | --- |
Membuat sistem
Pengguna dapat
|     | registrasi akun  | Menyimpan data user ke  |     |     |     |
| --- | ---------------- | ----------------------- | --- | --- | --- |
melakukan
1
|     | pengguna (calon  | dalam database  |     |     |     |
| --- | ---------------- | --------------- | --- | --- | --- |
registrasi akun
penonton)
Membuat fitur login
|     |     | Validasi autentikasi  | Pengguna dapat  |     |     |
| --- | --- | --------------------- | --------------- | --- | --- |
untuk pengguna (calon
2
|     |     | pengguna  | masuk ke sistem  |     |     |
| --- | --- | --------- | ---------------- | --- | --- |
penonton)
|     | Membuat fitur login  |     | Admin dapat  |     |     |
| --- | -------------------- | --- | ------------ | --- | --- |
3  Validasi autentikasi admin
|     | untuk admin bioskop  |     | mengakses  |     |     |
| --- | -------------------- | --- | ---------- | --- | --- |
|     |                      |     |            |     |     |

halaman
pengelolaan
Membuat user Pengguna dapat
Menampilkan data film dari
interface halaman melihat film yang
4
database
daftar film sedang tayang
Membuat user Pengguna dapat
Menampilkan sinopsis,
interface halaman melihat informasi
5
harga, jadwal
detail film lengkap film
Membuat halaman Pengguna dapat
Mengambil data film dari
6 daftar film yang melihat film
database
sedang tayang tersedia
Membuat halaman Pengguna dapat
Menampilkan detail
detail film beserta melihat jadwal
7
berdasarkan film terpilih
jadwal tayang tayang film
Membuat fitur upload Admin dapat
Menyimpan file gambar
gambar poster/cover menambahkan
16
poster ke server
film (admin) poster film
Pengguna dapat
Membuat fitur filter
Menyaring data film mencari film
17 film berdasarkan jam
berdasarkan jam sesuai waktu
tayang
luang
Sprint Planning Iterasi Kedua
Pada sprint planning iterasi kedua, fokus pengembangan adalah lanjutan dari
sistem yang telah dibuat pada iterasi pertama. Pada tahap ini dilakukan penambahan
fitur utama berupa pemesanan tiket, rating & review, pembayaran via WhatsApp,
pengelolaan data oleh admin, serta penyempurnaan fitur sistem seperti validasi tiket,
riwayat pemesanan, dan laporan.
Sprint Goal Iterasi Kedua yaitu, menyelesaikan seluruh fitur inti aplikasi agar
sistem Cinema Booking dapat digunakan secara lengkap oleh pengguna dan admin.
Tabel 3.9 Sprint Backlog – Iterasi 2
ID Story Fungsi Tujuan
Proses pemilihan Pengguna dapat
Membuat fitur
8 film, jadwal, melakukan
pemesanan tiket
jumlah tiket pemesanan tiket

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Membuat fitur yang
Mengambil dan
|     |     | menampilkan sisa    |                   | Pengguna mengetahui   |     |
| --- | --- | ------------------- | ----------------- | --------------------- | --- |
|     | 9   |                     | memperbarui stok  |                       |     |
|     |     | ketersediaan tiket  |                   | jumlah tiket tersisa  |     |
tiket
secara real-time
Membuat fitur
|     |     | perhitungan harga  | Kalkulasi harga  | Pengguna mengetahui  |     |
| --- | --- | ------------------ | ---------------- | -------------------- | --- |
10
|     |     | berdasarkan jumlah  | otomatis  | total pembayaran  |     |
| --- | --- | ------------------- | --------- | ----------------- | --- |
tiket
Membuat fitur
Sistem menjaga
|     |     | pengurangan stok  | Update database  |                     |     |
| --- | --- | ----------------- | ---------------- | ------------------- | --- |
|     | 11  |                   |                  | konsistensi jumlah  |     |
|     |     | tiket setelah     | stok tiket       |                     |     |
tiket
pemesanan berhasil
|     |     | Membuat halaman  | Menampilkan  |     |     |
| --- | --- | ---------------- | ------------ | --- | --- |
Pengguna dapat
|     | 12  | riwayat pemesanan  | data transaksi  |     |     |
| --- | --- | ------------------ | --------------- | --- | --- |
melihat riwayat tiket
pengguna  user
|     |     | Membuat fitur  | CRUD data film  |     |     |
| --- | --- | -------------- | --------------- | --- | --- |
Admin dapat
|     | 13  | manajemen data film  | (tambah, edit,  |     |     |
| --- | --- | -------------------- | --------------- | --- | --- |
mengelola data film
|     |     | (admin) - CRUD  | hapus)  |     |     |
| --- | --- | --------------- | ------- | --- | --- |
Membuat fitur
Admin dapat
|     |     | manajemen jadwal       | CRUD jadwal  |                  |     |
| --- | --- | ---------------------- | ------------ | ---------------- | --- |
|     | 14  |                        |              | mengatur jadwal  |     |
|     |     | tayang film (admin) -  | tayang film  |                  |     |
bioskop
CRUD
|     |     | Membuat halaman       | Menampilkan      | Admin dapat  |     |
| --- | --- | --------------------- | ---------------- | ------------ | --- |
|     | 15  | daftar pesanan masuk  | semua transaksi  | memonitor    |     |
|     |     | (admin)               | user             | pemesanan    |     |
|     |     | Membuat fitur rating  | Menyimpan        |              |     |
Pengguna dapat
|     | 18  | & review film  | rating dan review  |     |     |
| --- | --- | -------------- | ------------------ | --- | --- |
memberi ulasan film
|     |     | (pengguna)  | ke database  |     |     |
| --- | --- | ----------- | ------------ | --- | --- |
Membuat fitur
|     |     |     | Memeriksa  | Rating hanya dari  |     |
| --- | --- | --- | ---------- | ------------------ | --- |
validasi hak rating
|     | 19  |     | riwayat  | penonton yang sudah  |     |
| --- | --- | --- | -------- | -------------------- | --- |
(hanya yang sudah
|     |     |     | pemesanan user  | menonton  |     |
| --- | --- | --- | --------------- | --------- | --- |
menonton)
Menampilkan
|     |     | Membuat fitur  |     | Pengguna dapat  |     |
| --- | --- | -------------- | --- | --------------- | --- |
nomor WA admin
|     | 20  | pembayaran via  |     | melakukan  |     |
| --- | --- | --------------- | --- | ---------- | --- |
dan instruksi
|     |     | WhatsApp  |     | pembayaran manual  |     |
| --- | --- | --------- | --- | ------------------ | --- |
transfer
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

(menampilkan nomor
admin)
Membuat fitur
Admin dapat
|     |     | validasi pembayaran  |     | Mengupdate        |                |     |
| --- | --- | -------------------- | --- | ----------------- | -------------- | --- |
|     | 21  |                      |     |                   | memverifikasi  |     |
|     |     | oleh admin (ubah     |     | status pemesanan  |                |     |
pembayaran
status pemesanan)
|     |     | Membuat fitur      |     | Mengambil data  |                      |     |
| --- | --- | ------------------ | --- | --------------- | -------------------- | --- |
|     |     | laporan pemesanan  |     | transaksi dan   | Admin dapat melihat  |     |
22
|     |     | admin (harian, film    |     | menyusun  | statistik penjualan  |     |
| --- | --- | ---------------------- | --- | --------- | -------------------- | --- |
|     |     | terlaris, pendapatan)  |     | laporan   |                      |     |

3.3 Pemodelan Usecase Sistem
3.3.1 Usecase Sistem
Use case sistem digunakan untuk menggambarkan interaksi antara aktor dengan
sistem  yang  akan  dibangun.  Menurut  Rosa  &  Shalahuddin  (2018),  use  case  sistem
berfungsi  untuk  menunjukkan  layanan  atau  fungsi  yang  disediakan  sistem  kepada
pengguna. Pada aplikasi web Cinema Booking, use case sistem disusun berdasarkan
kebutuhan fungsional yang telah diidentifikasi pada tahap analisis sistem.
A. Identifikasi Aktor
Berdasarkan hasil analisis kebutuhan sistem Cinema Booking, terdapat dua aktor
utama yang berinteraksi langsung dengan sistem, yaitu pengguna (calon penonton)
dan admin (pengelola bioskop).
Tabel 3.11 Identifikasi Aktor Sistem
|     | Aktor  |     | Deskripsi  |     | Peran dalam Sistem  |     |
| --- | ------ | --- | ---------- | --- | ------------------- | --- |
Pengguna (Calon Penonton)  Individu yang menggunakan  - Registrasi akun
|     |     | aplikasi Cinema Booking untuk     |          |                                   | - Login ke sistem      |     |
| --- | --- | --------------------------------- | -------- | --------------------------------- | ---------------------- | --- |
|     |     | mencari informasi film dan        |          |                                   | - Melihat daftar film  |     |
|     |     | melakukan pemesanan tiket secara  |          | - Melihat detail film dan jadwal  |                        |     |
|     |     |                                   | online.  |                                   | tayang                 |     |
- Memesan tiket
- Melakukan pembayaran via
WhatsApp
- Melihat riwayat pemesanan
- Memberikan rating dan review
Admin (Pengelola Bioskop)  Karyawan yang bertugas  - Login admin
|     |     | mengelola operasional aplikasi  |                  |     | - Mengelola data film (CRUD)  |     |
| --- | --- | ------------------------------- | ---------------- | --- | ----------------------------- | --- |
|     |     |                                 | Cinema Booking.  |     | - Mengelola jadwal tayang     |     |
(CRUD)
- Melihat daftar pesanan
- Memvalidasi pembayaran
pengguna
- Mengelola laporan pemesanan

B. Identifikasi Usecase
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Use case merupakan fungsi atau layanan yang disediakan sistem bagi aktor. Use
case diturunkan dari kebutuhan fungsional yang telah diidentifikasi pada tahap
analisis sistem.
Tabel 3.12 Identifikasi Use Case Sistem
|     | Use Case         |                             | Deskripsi  | Aktor Terkait  |     |
| --- | ---------------- | --------------------------- | ---------- | -------------- | --- |
|     | Registrasi Akun  | Pengguna membuat akun baru  |            | Pengguna       |     |
pada sistem.
|     | Login Pengguna  | Pengguna masuk ke sistem  |     | Pengguna  |     |
| --- | --------------- | ------------------------- | --- | --------- | --- |
menggunakan akun yang telah
terdaftar.
Melihat Daftar Film  Pengguna melihat daftar film yang  Pengguna
sedang tayang.
Melihat Detail Film  Pengguna melihat informasi detail  Pengguna
film, jadwal tayang, harga tiket,
dan rating.
|     | Memesan Tiket  | Pengguna memilih film, jadwal  |     | Pengguna  |     |
| --- | -------------- | ------------------------------ | --- | --------- | --- |
tayang, dan jumlah tiket yang
ingin dipesan.
Melakukan Pembayaran via  Pengguna memperoleh informasi  Pengguna
|     | WhatsApp  | pembayaran dan mengirim bukti  |     |     |     |
| --- | --------- | ------------------------------ | --- | --- | --- |
transfer melalui WhatsApp.
Melihat Riwayat Pemesanan  Pengguna melihat daftar tiket  Pengguna
yang pernah dipesan beserta
statusnya.
Memberikan Rating dan Review  Pengguna memberikan rating dan  Pengguna
ulasan terhadap film yang telah
ditonton.
|     | Login Admin  | Admin masuk ke halaman  |     | Admin  |     |
| --- | ------------ | ----------------------- | --- | ------ | --- |
administrasi sistem.
| Mengelola Data Film  |     | Admin menambah, mengubah,  |     | Admin  |     |
| -------------------- | --- | -------------------------- | --- | ------ | --- |
dan menghapus data film.
| Mengelola Jadwal Tayang  |     | Admin menambah, mengubah,  |     | Admin  |     |
| ------------------------ | --- | -------------------------- | --- | ------ | --- |
dan menghapus jadwal tayang
film.
| Melihat Daftar Pesanan  |     | Admin melihat seluruh data  |     | Admin  |     |
| ----------------------- | --- | --------------------------- | --- | ------ | --- |
pemesanan tiket pengguna.
| Memvalidasi Pembayaran  |     | Admin memverifikasi bukti  |     | Admin  |     |
| ----------------------- | --- | -------------------------- | --- | ------ | --- |
pembayaran yang dikirim
pengguna.
Mengelola Laporan Pemesanan  Admin melihat dan mengekspor  Admin
laporan pemesanan serta
pendapatan bioskop.

C. Diagram Usecase Sistem
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Gambar 3.6 Use Case Diagram Sistem Cinema Booking
Penjelasan Diagram Use Case Sistem:
1. Pengguna (Calon Penonton) berinteraksi dengan delapan use case utama, yaitu
registrasi akun, login, melihat daftar film, melihat detail film, memesan tiket,
melakukan pembayaran via WhatsApp, melihat riwayat pemesanan, serta memberikan
rating dan review.
2. Admin (Pengelola Bioskop) berinteraksi dengan enam use case utama, yaitu login
admin, mengelola data film, mengelola jadwal tayang, melihat daftar pesanan,
memvalidasi pembayaran, dan mengelola laporan pemesanan.
3. Use case Memesan Tiket memiliki hubungan include dengan Melihat Detail Film
karena pengguna harus melihat informasi film sebelum melakukan pemesanan.
4. Use case Memberikan Rating dan Review memiliki hubungan include dengan
Melihat Riwayat Pemesanan untuk memastikan hanya pengguna yang pernah
menonton film yang dapat memberikan ulasan.
5. Use case Memvalidasi Pembayaran memiliki hubungan include dengan Melihat
Daftar Pesanan karena admin perlu melihat data pesanan sebelum melakukan validasi
pembayaran.
3.4 Desain
3.4.1 Diagram Interaksi (sekuensial atau kolaborasi)

3.4.2 Diagram kelas
3.4.3 Diagram IPO
3.4.4 Rancangan UI/UX
Wireframe adalah kerangka dasar atau "cetak biru" (blueprint) visual dari sebuah
antarmuka website atau aplikasi. Wireframe biasanya dibuat dengan warna hitam, putih,
atau abu-abu, menggunakan kotak dan garis untuk merepresentasikan elemen seperti
gambar, teks, dan tombol, tanpa memedulikan detail desain grafis seperti warna, tipografi,
atau animasi.
Pentingnya Wireframe dalam Pembangunan Website:
• Fokus pada Fungsi & Struktur: Membantu pengembang dan pemangku kepentingan
(stakeholders) untuk fokus pada tata letak, fungsionalitas, dan penempatan
informasi tanpa terdistraksi oleh elemen estetika.
• Efisiensi Waktu & Biaya: Merevisi tata letak pada tahap wireframe jauh lebih cepat
dan murah dibandingkan merombak website yang sudah setengah jadi di tahap
coding atau desain visual tingkat tinggi (High-Fidelity).
• Validasi Alur Pengguna (User Flow): Memastikan perjalanan pengguna—dari
halaman depan hingga proses checkout—terasa intuitif, logis, dan tidak
membingungkan.
A. Halaman Home
Ini adalah etalase utama website. Desainnya difokuskan pada navigasi cepat dan
penemuan konten. Terdapat bilah pencarian dan tombol akses akun di bagian
atas, disusul oleh hero banner utama untuk promosi. Di bawahnya, terdapat
katalog "Sedang Tayang" berbentuk grid yang menampilkan poster, judul,
informasi dasar film, dan tombol aksi (Detail) untuk memancing konversi
pengguna.
B. Halaman Login

Halaman ini bertugas sebagai pintu gerbang autentikasi. Tampilannya sengaja
dibuat bersih dan terpusat (centered) untuk menghilangkan distraksi. Halaman
ini memuat kolom input esensial (Email dan Password), opsi pengingat sesi
("Ingat saya"), tautan pemulihan password, serta pemicu untuk berpindah ke
halaman pendaftaran bagi pengguna baru.
C. Halaman Pemesanan
Ini adalah antarmuka transaksional inti. Halaman ini menggunakan tata letak layar
terbagi (split layout):
• Kiri: Denah visual kursi bioskop yang interaktif, dilengkapi legenda status kursi
(Tersedia, Dipilih, Terjual) untuk mencegah kesalahan pemesanan.
• Kanan: Ringkasan pesanan (Order Summary) yang terus diperbarui, menampilkan
detail film, lokasi, nomor kursi yang dipilih, kalkulasi harga, dan tombol konfirmasi
untuk melangkah ke tahap pembayaran.
D. Halaman History

Berfungsi sebagai dasbor personal bagi pengguna untuk melacak transaksi
mereka. Halaman ini menampilkan daftar tiket dengan indikator visual yang
sangat jelas terkait status pesanan. Misalnya, pesanan "Lunas" diberi warna hijau
dengan opsi melihat tiket, sedangkan pesanan "Pending" diberi peringatan visual
untuk segera memicu tindakan pembayaran (Bayar Sekarang).
E. Halaman Admin
Tampilan ini adalah panel kontrol khusus pengelola (backend). Tata letaknya
memisahkan menu navigasi di sidebar (Kelola Film, Pesanan Masuk, Laporan)
dengan area kerja utama. Pada bagian "Kelola Film", admin dapat melihat daftar
film lengkap dengan metrik instan yang menunjukkan rasio kursi "Tersedia" dan
"Terjual", serta tombol aksi cepat untuk mengedit atau menghapus data film dari
sistem.
3.4.5 Site Map dan Gambaran Sistem
3.5 Implementasi
Implementasi merupakan tahap dimana seluruh perencanaan dan desain sistem
diterjemahkan ke dalam kode program yang siap dijalankan. Dalam metode Scrum,
implementasi dilakukan secara iteratif melalui serangkaian sprint. Setiap sprint memiliki
tahapan daily scrum untuk memantau kemajuan harian, sprint review untuk mengevaluasi
hasil yang telah dicapai, serta sprint retrospective untuk melakukan perbaikan proses

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

pada sprint berikutnya. Menurut Pressman & Maxim (2020), implementasi dalam Scrum
menekankan  pada  kolaborasi  tim,  adaptasi  terhadap  perubahan,  serta  pengiriman
perangkat lunak secara bertahap namun fungsional.
Pada pengembangan aplikasi web Cinema Booking, implementasi dilakukan
dalam 2 kali iterasi (sprint). Berikut adalah laporan pelaksanaan implementasi untuk
masing-masing sprint.
3.5.1 Daily Scrum report
Daily scrum adalah pertemuan harian yang dilakukan selama 15 menit untuk
melaporkan kemajuan pekerjaan, rencana pekerjaan selanjutnya, serta kendala yang
dihadapi oleh setiap anggota tim pengembang. Menurut Rosa & Shalahuddin (2018),
daily scrum bertujuan untuk menyelaraskan tim dan mengidentifikasi hambatan
sejak dini. Sommerville (2016) menambahkan bahwa daily scrum membantu tim
untuk tetap fokus pada sprint goal yang telah ditentukan.
Pada proyek Cinema Booking, daily scrum dilaksanakan setiap hari kerja
selama durasi sprint. Berikut adalah laporan  daily scrum untuk masing-masing
sprint.
Tabel Daily Scrum (Sprint  - Iterasi Pertama)
Sprint  Goal  Iterasi  1:  Membangun  sistem  dasar  aplikasi  yang  dapat
digunakan oleh pengguna untuk melihat informasi film dan melakukan autentikasi
akun.
Tabel 3.10 Daily Scrum (Sprint 1 - Iterasi Pertama)
|     | To Do  | In Progress  | Done  |     |
| --- | ------ | ------------ | ----- | --- |
Membuat sistem registrasi akun
|     |     | -   |     |     |
| --- | --- | --- | ---- | --- |
pengguna
| Membuat fitur login untuk pengguna  |     | -   |     |     |
| ----------------------------------- | --- | --- | ---- | --- |
Membuat fitur login untuk admin
|     |     | -   |     |     |
| --- | --- | --- | ---- | --- |
bioskop
Membuat user interface halaman
|     |     | -   |     |     |
| --- | --- | --- | ---- | --- |
daftar film
Membuat user interface halaman
|     |     | -   |     |     |
| --- | --- | --- | ---- | --- |
detail film
Membuat halaman daftar film yang
|     |     | -   |     |     |
| --- | --- | --- | ---- | --- |
sedang tayang
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Membuat halaman detail film beserta
|     |     |     | -   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
jadwal tayang
Membuat fitur upload gambar poster
|     |     |     | -   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
film (admin)
Membuat fitur filter film berdasarkan
|     |     |     | -   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
jam tayang
|     | Hari/Tanggal:  | Selasa,  |     | 5   | Mei  | 2026  |     |
| --- | -------------- | -------- | --- | --- | ---- | ----- | --- |
Nama: Arif
|     | 1.  Apa  | yang  |     | sudah  |     | dikerjakan?  |     |
| --- | -------- | ----- | --- | ------ | --- | ------------ | --- |
Setup environment project, database awal, dan struktur folder.
|     | 2.  Apa  | yang  |     | akan  |     | dikerjakan?  |     |
| --- | -------- | ----- | --- | ----- | --- | ------------ | --- |
Membuat sistem registrasi akun pengguna dan fitur login untuk pengguna.
|     | 3.  Kendala  |     | yang  |     |     | dihadapi?  |     |
| --- | ------------ | --- | ----- | --- | --- | ---------- | --- |
Tidak ada, persiapan awal dan konfigurasi database berjalan lancar.
|     | Hari/Tanggal:  | Rabu,  |     | 6   | Mei  | 2026  |     |
| --- | -------------- | ------ | --- | --- | ---- | ----- | --- |
Nama: Arif
|     | 1.  Apa  | yang  |     | sudah  |     | dikerjakan?  |     |
| --- | -------- | ----- | --- | ------ | --- | ------------ | --- |
Membuat sistem registrasi akun pengguna dan fitur login untuk pengguna.
|     | 2.  Apa  | yang  |     | akan  |     | dikerjakan?  |     |
| --- | -------- | ----- | --- | ----- | --- | ------------ | --- |
Membuat fitur login untuk admin bioskop dan membuat user interface halaman
daftar film.
|     | 3.  Kendala  |     | yang  |     |     | dihadapi?  |     |
| --- | ------------ | --- | ----- | --- | --- | ---------- | --- |
Memisahan hak akses token (JWT) antara login user biasa dan admin bioskop
agar tidak tertukar.

|     | Hari/Tanggal:  | Kamis,  |     | 7   | Mei  | 2026  |     |
| --- | -------------- | ------- | --- | --- | ---- | ----- | --- |
Nama: Arif
|     | 1.  Apa  | yang  |     | sudah  |     | dikerjakan?  |     |
| --- | -------- | ----- | --- | ------ | --- | ------------ | --- |
Membuat fitur login untuk admin bioskop dan user interface halaman daftar
film.
|     | 2.  Apa  | yang  |     | akan  |     | dikerjakan?  |     |
| --- | -------- | ----- | --- | ----- | --- | ------------ | --- |
Membuat user interface halaman detail film dan membuat halaman daftar film
yang sedang tayang.
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     | 3.  | Kendala  |     | yang  |     |     | dihadapi?  |     |
| --- | --- | -------- | --- | ----- | --- | --- | ---------- | --- |
Tampilan  antarmuka  daftar  film  masih  sangat  sederhana  (menggunakan
komponen UI standar) karena mengejar fungsionalitas dasar.
|     | Hari/Tanggal:  |     | Jumat,  |     | 8   | Mei  |     | 2026  |
| --- | -------------- | --- | ------- | --- | --- | ---- | --- | ----- |
Nama: Guntur
|     | 1.  | Apa  | yang  |     | sudah  |     | dikerjakan?  |     |
| --- | --- | ---- | ----- | --- | ------ | --- | ------------ | --- |
Membuat user interface halaman detail film dan membuat halaman daftar film
yang sedang tayang.
|     | 2.  | Apa  | yang  |     | akan  |     | dikerjakan?  |     |
| --- | --- | ---- | ----- | --- | ----- | --- | ------------ | --- |
Membuat halaman detail film beserta jadwal tayang.
|     | 3.  | Kendala  |     | yang  |     |     | dihadapi?  |     |
| --- | --- | -------- | --- | ----- | --- | --- | ---------- | --- |
Tata letak tombol jadwal tayang masih kaku dan penyesuaian resolusi layar
tablet/HP belum maksimal.
|     | Hari/Tanggal:  |     | Sabtu,  |     | 9   | Mei  |     | 2026  |
| --- | -------------- | --- | ------- | --- | --- | ---- | --- | ----- |
Nama: Guntur
|     | 1.  | Apa  | yang  |     | sudah  |     | dikerjakan?  |     |
| --- | --- | ---- | ----- | --- | ------ | --- | ------------ | --- |
Membuat halaman detail film beserta jadwal tayang (menyambungkan data
statis dari database).
|     | 2.  | Apa  | yang  |     | akan  |     | dikerjakan?  |     |
| --- | --- | ---- | ----- | --- | ----- | --- | ------------ | --- |
Pelaksanaan Sprint Review Iterasi Pertama.
|     | 3.  | Kendala  |     | yang  |     |     | dihadapi?  |     |
| --- | --- | -------- | --- | ----- | --- | --- | ---------- | --- |
Berdasarkan  hasil  review  bersama  Scrum  Master  dan  Product  Owner,
ditemukan banyak kekurangan: belum ada sistem pemesanan, validasi stok,
riwayat user, admin belum bisa kelola film/jadwal mandiri, dan UI masih terlalu
sederhana. Masukan ini akan langsung diperbaiki di Sprint 2.
Tabel Daily Scrum (Sprint  - Iterasi Pertama)
Sprint Goal Iterasi 2 yaitu, menyelesaikan seluruh fitur inti aplikasi agar
sistem Cinema Booking dapat digunakan secara lengkap oleh pengguna dan admin.
Tabel 3.11 Daily Scrum (Sprint - Iterasi Pertama)
|                                |     | To Do  |     | In Progress  |     |     | Done  |     |
| ------------------------------ | --- | ------ | --- | ------------ | --- | --- | ----- | --- |
| Membuat fitur pemesanan tiket  |     |        |     | -            |     |     |      |     |
Membuat fitur sisa ketersediaan tiket
|     |     |     |     | -   |     |     |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

real-time
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

Membuat fitur perhitungan harga
|     | -   |     |     |
| --- | --- | ---- | --- |
otomatis
Membuat fitur pengurangan stok
-

tiket
Membuat halaman riwayat
|     | -   |     |     |
| --- | --- | ---- | --- |
pemesanan pengguna
Membuat fitur manajemen data film
|     | -   |     |     |
| --- | --- | ---- | --- |
(admin) - CRUD
Membuat fitur manajemen jadwal
|     | -   |     |     |
| --- | --- | ---- | --- |
tayang (admin) - CRUD
Membuat halaman daftar pesanan
-

masuk (admin)
| Membuat fitur rating & review film  | -   |     |     |
| ----------------------------------- | --- | ---- | --- |
| Membuat fitur validasi hak rating   | -   |      |     |

Membuat fitur pembayaran via
|     | -   |     |     |
| --- | --- | ---- | --- |
WhatsApp
Membuat fitur validasi pembayaran
|     | -   |     |     |
| --- | --- | ---- | --- |
oleh admin
Membuat fitur laporan pemesanan
-

admin
Hari/Tanggal: Minggu, 10 Mei 2026
Nama: Guntur
1.  Apa yang sudah dikerjakan?
Memulai Sprint 2 dengan merancang tabel database baru untuk pemesanan
dan kursi.
2.  Apa yang akan dikerjakan?
Fitur Pemesanan Tiket (pilih film, jadwal, input jumlah, ringkasan pesanan)
dan Fitur Sisa Ketersediaan Tiket Real-time.
3.  Kendala yang dihadapi?
Logika backend untuk memastikan ringkasan pesanan muncul dengan benar
sebelum konfirmasi final dilakukan oleh pengguna.
Hari/Tanggal: Senin, 11 Mei 2026
Nama: Nathan
|     |     |     |     |
| --- | --- | --- | --- |

1. Apa yang sudah dikerjakan?
Fitur Pemesanan Tiket dan Fitur Menampilkan sisa tiket secara real-time di
halaman jadwal.
2. Apa yang akan dikerjakan?
Fitur Perhitungan Harga Otomatis dan Fitur Pengurangan Stok Tiket.
3. Kendala yang dihadapi?
Menyelaraskan harga tiket yang berbeda-beda antar film secara dinamis ke
dalam komponen perhitungan total harga otomatis.
Hari/Tanggal: Selasa, 12 Mei 2026
Nama: Nathan
1. Apa yang sudah dikerjakan?
Fitur Perhitungan harga otomatis berdasarkan jumlah tiket dan Fitur
otomatisasi pengurangan stok tiket di database setelah pemesanan berhasil.
2. Apa yang akan dikerjakan?
Fitur Halaman Riwayat Pemesanan Pengguna dan melakukan perbaikan
tampilan antarmuka (UI/UX) agar lebih menarik dan responsif.
3. Kendala yang dihadapi?
Keamanan database transaction saat stok dikurangi, guna menghindari race
condition jika ada dua user membeli tiket terakhir bersamaan.
Hari/Tanggal: Rabu, 13 Mei 2026
Nama: Nathan
1. Apa yang sudah dikerjakan?
Fitur Halaman Riwayat Pemesanan Pengguna (detail film, jadwal, jumlah,
total harga, status) serta penyempurnaan UI frontend menjadi lebih responsif.
2. Apa yang akan dikerjakan?
Fitur Manajemen Data Film (Admin) dan Fitur Manajemen Jadwal Tayang
Film (Admin).
3. Kendala yang dihadapi?
Query penarikan data riwayat pemesanan pengguna cukup kompleks karena
harus melakukan join banyak tabel sekaligus.
Hari/Tanggal: Kamis, 14 Mei 2026
Nama: Nathan
1. Apa yang sudah dikerjakan?
Fitur CRUD data film (judul, sinopsis, poster, dll) dan pengelolaan jadwal
tayang (tanggal, jam, studio, stok awal) oleh Admin secara mandiri, serta fitur

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

upload gambar poster, fitur rating & review, filter jam tayang, pembayaran via
WhatsApp, validasi payment, dan laporan admin.
2.  Apa yang akan dikerjakan?
Fitur Halaman Daftar Pesanan Masuk (Admin) dan melakukan Final Testing
sistem.
3.  Kendala yang dihadapi?
Validasi input pada manajemen jadwal admin agar tidak terjadi bentrok studio
pada jam tayang yang sama. Kendala berhasil diatasi di sisi backend sebelum
penutupan proyek hari ini.
3.5.2 Sprint Review
Sprint review merupakan tahap presentasi hasil produk yang telah dikerjakan
kepada product owner untuk mengevaluasi kesesuaian dengan kesepakatan awal.
Menurut  Dennis,  Wixom,  &  Roth  (2019),  sprint  review  bertujuan  untuk
mendapatkan  umpan  balik  dari  product  owner  dan  stakeholder  sehingga  tim
pengembang dapat melakukan perbaikan pada sprint berikutnya. Firmansyah &
Voutama (2024) menambahkan bahwa sprint review juga berfungsi sebagai ajang
demo fitur-fitur yang telah selesai.
Sprint Review Iterasi Pertama
Sprint review pada iterasi pertama menghasilkan aplikasi web pemesanan
tiket film (Cinema Booking) yang sudah dapat melakukan registrasi dan login untuk
pengguna serta admin, serta dapat menampilkan daftar film dan detail film beserta
jadwal tayang, dilengkapi dengan fitur filter jam tayang dan upload poster film oleh
admin.
Tabel 3.12 Kesesuaian Story Dengan Fitur Aplikasi (Iterasi 1)
|     | No  | ID Story  |                      | Fitur dan Deskripsi  |         |               |     |
| --- | --- | --------- | -------------------- | -------------------- | ------- | ------------- | --- |
|     |     |           | Fitur:               | Registrasi           | Akun    | Pengguna      |     |
|     |     |           | Deskripsi:           | Pengguna             | (calon  | penonton)     |     |
|     | 1   | 1         | dapat  mendaftarkan  |                      | akun    | baru  dengan  |     |
|     |     |           | mengisi              | email,  username,    | dan     | password.     |     |
Data tersimpan ke dalam database.
|     |     |     | Fitur:        | Login     |           | Pengguna     |     |
| --- | --- | --- | ------------- | --------- | --------- | ------------ | --- |
|     |     |     | Deskripsi:    | Pengguna  | (calon    | penonton)    |     |
|     | 2   | 2   |               |           |           |              |     |
|     |     |     | dapat  masuk  | ke        | aplikasi  | menggunakan  |     |
email dan password yang sudah terdaftar.
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     | Fitur:  |     | Login  |     | Admin  |     |
| --- | --- | --- | ------- | --- | ------ | --- | ------ | --- |
Deskripsi: Admin bioskop dapat masuk ke
|     | 3   | 3   |          |        |              |     |             |     |
| --- | --- | --- | -------- | ------ | ------------ | --- | ----------- | --- |
|     |     |     | halaman  | admin  | menggunakan  |     | kredensial  |     |
khusus yang telah ditentukan.
|     |     |     | Fitur:  | Halaman  |     | Daftar  | Film  |     |
| --- | --- | --- | ------- | -------- | --- | ------- | ----- | --- |
Deskripsi: Menampilkan semua film yang
|     | 4   | 4,6  | sedang   | tayang  | dalam              | bentuk  | grid  atau  |     |
| --- | --- | ---- | -------- | ------- | ------------------ | ------- | ----------- | --- |
|     |     |      | daftar.  | Setiap  | film  menampilkan  |         | judul,      |     |
poster, dan jam tayang.
|     |     |      | Fitur:      | Halaman  |              | Detail  | Film       |     |
| --- | --- | ---- | ----------- | -------- | ------------ | ------- | ---------- | --- |
|     |     |      | Deskripsi:  |          | Menampilkan  |         | informasi  |     |
|     | 5   | 5,7  |             |          |              |         |            |     |
lengkap film (sinopsis, durasi, harga tiket,
genre, dan daftar jadwal tayang).
|     |     |     | Fitur:       | Upload        | Gambar      |         | Poster  Film  |     |
| --- | --- | --- | ------------ | ------------- | ----------- | ------- | ------------- | --- |
|     |     |     | Deskripsi:   | Admin         |             | dapat   | mengunggah    |     |
|     | 6   | 16  | gambar       | poster/cover  |             |         | film  saat    |     |
|     |     |     | menambahkan  |               | film  baru  | dengan  | validasi      |     |
format dan ukuran file.
Fitur: Filter Film Berdasarkan Jam Tayang
|     |     |     | Deskripsi:                                 | Pengguna  |     | dapat  | menyaring   |     |
| --- | --- | --- | ------------------------------------------ | --------- | --- | ------ | ----------- | --- |
|     | 7   | 17  | daftar film berdasarkan jam tayang (pagi,  |           |     |        |             |     |
|     |     |     | siang,  sore,                              | malam)    |     | untuk  | memudahkan  |     |
mencari film sesuai waktu luang.
Kesimpulan Review Iterasi Pertama
Berdasarkan hasil diskusi dan evaluasi oleh scrum master, product owner, dan
development team, terdapat beberapa kekurangan pada sistem yang perlu diperbaiki
pada iterasi kedua:
1.  Belum ada fitur pemesanan tiket secara online.
2.
Belum ada validasi stok tiket (pengguna tidak tahu sisa tiket tersisa berapa).
3.  Belum ada halaman riwayat pemesanan untuk pengguna.
4.  Admin belum bisa mengelola data film dan jadwal tayang secara mandiri
(CRUD sudah ada, tetapi perlu penyempurnaan).
5.  Belum ada fitur rating & review film.
6.  Belum ada sistem pembayaran (via WhatsApp) dan validasi pembayaran oleh
admin.
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

7.  Belum ada laporan pemesanan untuk admin.
8.  Tampilan antarmuka masih sederhana dan perlu penyempurnaan.
Sprint Review Iterasi Kedua
Pada sprint review iterasi kedua, dilakukan demo fitur-fitur lanjutan yang
merupakan kelanjutan dari iterasi pertama. Seluruh fitur yang direncanakan telah
berhasil diimplementasikan.
Tabel 3.13 Kesesuaian Story Dengan Fitur Aplikasi (Iterasi 2)
|     | No  | ID Story  |         | Fitur dan Deskripsi  |            |     |        |     |
| --- | --- | --------- | ------- | -------------------- | ---------- | --- | ------ | --- |
|     |     |           | Fitur:  |                      | Pemesanan  |     | Tiket  |     |
Deskripsi: Pengguna dapat memesan tiket
|     |     |     | dengan  | memilih  | film,  | memilih  | jadwal  |     |
| --- | --- | --- | ------- | -------- | ------ | -------- | ------- | --- |
|     | 1   | 8   |         |          |        |          |         |     |
tayang, dan mengisi jumlah tiket. Sistem
menampilkan ringkasan pesanan sebelum
konfirmasi.
Fitur: Sisa Ketersediaan Tiket Real-time
|     |     |     | Deskripsi:  | Sistem  | menampilkan  |     | jumlah  |     |
| --- | --- | --- | ----------- | ------- | ------------ | --- | ------- | --- |
sisa tiket yang tersedia untuk setiap jadwal
|     | 2   | 9   |         |         |           |     |              |     |
| --- | --- | --- | ------- | ------- | --------- | --- | ------------ | --- |
|     |     |     | tayang  | secara  | langsung  |     | (real-time)  |     |
sehingga pengguna tahu apakah tiket masih
tersedia.
|     |     |     | Fitur:      | Perhitungan  |     | Harga   | Otomatis  |     |
| --- | --- | --- | ----------- | ------------ | --- | ------- | --------- | --- |
|     |     |     | Deskripsi:  | Sistem       |     | secara  | otomatis  |     |
menghitung total harga yang harus dibayar
|     | 3   | 10  |              |         |        |              |              |     |
| --- | --- | --- | ------------ | ------- | ------ | ------------ | ------------ | --- |
|     |     |     | berdasarkan  | jumlah  |        | tiket  yang  | dipilih      |     |
|     |     |     | pengguna.    | Harga   | tiket  | per          | film  dapat  |     |
berbeda.
|     |     |     | Fitur:      | Pengurangan  |     | Stok    | Tiket     |     |
| --- | --- | --- | ----------- | ------------ | --- | ------- | --------- | --- |
|     |     |     | Deskripsi:  | Sistem       |     | secara  | otomatis  |     |
mengurangi stok tiket di database setiap
|     | 4   | 11  | kali        | pengguna  | berhasil     |          | melakukan  |     |
| --- | --- | --- | ----------- | --------- | ------------ | -------- | ---------- | --- |
|     |     |     | pemesanan.  | Stok      | yang         | tersisa  | akan       |     |
|     |     |     | terupdate   | dan       | ditampilkan  | ke       | pengguna   |     |
lain.
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     | Fitur:  | Halaman  | Riwayat  |     | Pemesanan  |     |     |
| --- | --- | --- | ------- | -------- | -------- | --- | ---------- | --- | --- |
Pengguna
Deskripsi: Pengguna dapat melihat daftar
|     | 5   | 12  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tiket yang pernah dipesan beserta detailnya
seperti judul film, jadwal tayang, jumlah
tiket, total harga, dan status pemesanan.
|     |     |     | Fitur:      | Manajemen  |              | Data   | Film       | (Admin)  |     |
| --- | --- | --- | ----------- | ---------- | ------------ | ------ | ---------- | -------- | --- |
|     |     |     | Deskripsi:  |            | Admin        | dapat  | melakukan  |          |     |
|     |     |     | operasi     | CRUD       | (Create,     |        | Read,      | Update,  |     |
|     | 6   | 13  |             |            |              |        |            |          |     |
|     |     |     | Delete)     | pada       | data  film,  |        | meliputi   | judul,   |     |
sinopsis, durasi, harga, genre, dan poster
film.
|     |     |     | Fitur:  | Manajemen  |     | Jadwal  | Tayang  | Film  |     |
| --- | --- | --- | ------- | ---------- | --- | ------- | ------- | ----- | --- |
(Admin)
|     |     |     | Deskripsi:  |     | Admin  | dapat  | menambah,  |     |     |
| --- | --- | --- | ----------- | --- | ------ | ------ | ---------- | --- | --- |
|     | 7   | 14  |             |     |        |        |            |     |     |
mengedit, dan menghapus jadwal tayang
|     |     |     | untuk  | setiap  | film.  | Jadwal  | mencakup  |     |     |
| --- | --- | --- | ------ | ------- | ------ | ------- | --------- | --- | --- |
tanggal, jam tayang, studio, dan stok tiket
awal.
|     |     |     | Fitur:  | Halaman  | Daftar  | Pesanan  |     | Masuk  |     |
| --- | --- | --- | ------- | -------- | ------- | -------- | --- | ------ | --- |
(Admin)
|     |     |     | Deskripsi:  | Admin  | dapat  |     | melihat  | semua  |     |
| --- | --- | --- | ----------- | ------ | ------ | --- | -------- | ------ | --- |
transaksi pemesanan tiket yang dilakukan
|     | 8   | 15  |           |            |        |           |      |            |     |
| --- | --- | --- | --------- | ---------- | ------ | --------- | ---- | ---------- | --- |
|     |     |     | oleh      | pengguna,  |        | termasuk  |      | informasi  |     |
|     |     |     | pemesan,  | film       | yang   | dipesan,  |      | jadwal,    |     |
|     |     |     | jumlah    | tiket,     | total  | harga,    | dan  | status     |     |
pembayaran.
|     |     |     | Fitur:      | Rating  | &         | Review      |       | Film    |     |
| --- | --- | --- | ----------- | ------- | --------- | ----------- | ----- | ------- | --- |
|     |     |     | Deskripsi:  |         | Pengguna  |             | yang  | sudah   |     |
|     |     |     | menonton    | dapat   |           | memberikan  |       | rating  |     |
|     | 9   | 18  |             |         |           |             |       |         |     |
bintang (1-5) dan review teks pada film.
|     |     |     | Rating  | dan  review  |     | akan  | ditampilkan  |     | di  |
| --- | --- | --- | ------- | ------------ | --- | ----- | ------------ | --- | --- |
halaman detail film.
|     |     |     | Fitur:      | Validasi  |       | Hak       |              | Rating   |     |
| --- | --- | --- | ----------- | --------- | ----- | --------- | ------------ | -------- | --- |
|     | 10  | 19  | Deskripsi:  | Sistem    |       | hanya     | mengizinkan  |          |     |
|     |     |     | pengguna    |           | yang  | memiliki  |              | riwayat  |     |
|     |     |     |             |           |       |           |              |          |     |

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

pemesanan dengan status "dibayar" atau
|     |     |     |     |     | "selesai"  | untuk  | memberikan  |     | rating  | dan  |
| --- | --- | --- | --- | --- | ---------- | ------ | ----------- | --- | ------- | ---- |
review pada film yang bersangkutan.
|     |     |     |     |     | Fitur:  | Pembayaran  |     | via  | WhatsApp  |     |
| --- | --- | --- | --- | --- | ------- | ----------- | --- | ---- | --------- | --- |
Deskripsi: Pengguna mendapatkan nomor
|     |     |     |     |     | WhatsApp  | admin      |        | yang  dapat  | dihubungi  |      |
| --- | --- | --- | --- | --- | --------- | ---------- | ------ | ------------ | ---------- | ---- |
|     | 11  |     |     | 20  |           |            |        |              |            |      |
|     |     |     |     |     | untuk     | melakukan  |        | transfer     | manual,    |      |
|     |     |     |     |     | mengirim  |            | bukti  | pembayaran,  |            | dan  |
melakukan konfirmasi.
Fitur: Validasi Pembayaran oleh Admin
Deskripsi: Admin dapat memverifikasi
|     | 12  |     |     | 21  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bukti pembayaran yang dikirim pengguna
dan mengubah status pemesanan dari
"menunggu validasi" menjadi "dibayar".
Fitur: Laporan Pemesanan Admin
Deskripsi: Admin dapat melihat dan
|     | 13  |     |     | 22  | mengekspor laporan pemesanan yang  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
meliputi laporan harian, laporan film
terlaris, dan laporan pendapatan.
3.5.3 Sprint Retrospective
Sprint retrospective adalah tahap evaluasi yang dilakukan di akhir sprint
untuk membahas kekurangan dan kelebihan selama proses pengembangan. Menurut
Pressman  &  Maxim  (2020),  sprint  retrospective  bertujuan  untuk  melakukan
perbaikan berkelanjutan (continuous improvement) pada proses, bukan hanya pada
produk. Sommerville (2016) menambahkan bahwa retrospective melibatkan seluruh
tim untuk mengidentifikasi apa yang berjalan baik dan apa yang perlu diperbaiki.
Pada  proyek  Cinema  Booking,  sprint  retrospective  dilakukan  setelah
masing-masing sprint selesai. Berikut adalah hasil evaluasinya.
Tabel 3.14 Perbandingan iterasi 1 dan 2 pada sprint retrospective
|     | Iterasi  |                         | Fitur  |     | Status  |     |     | Improvement  |     |     |
| --- | -------- | ----------------------- | ------ | --- | ------- | --- | --- | ------------ | --- | --- |
|     | 1        | Pemesanan Tiket Online  |        |     | Buruk   |     |     |              | -   |     |
Penambahan fitur pemesanan
|     | 2   | Pemesanan Tiket Online  |     |     | Baik  |     |     |     |     |     |
| --- | --- | ----------------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
tiket online dengan validasi stok
|     | 1   | Validasi Stok Tiket  |     |     | Buruk  |     |     |     | -   |     |
| --- | --- | -------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |                      |     |     |        |     |     |     |     |     |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Penambahan fitur validasi stok
| 2   | Validasi Stok Tiket  | Baik  |     |     |     |
| --- | -------------------- | ----- | --- | --- | --- |
tiket secara real-time
| 1   | Riwayat Pemesanan  | Buruk  |     | -   |     |
| --- | ------------------ | ------ | --- | --- | --- |
Penambahan halaman riwayat
| 2   | Riwayat Pemesanan  | Baik  |     |     |     |
| --- | ------------------ | ----- | --- | --- | --- |
pemesanan pengguna
Manajemen Data Film
| 1   |     | Cukup  |     | -   |     |
| --- | --- | ------ | --- | --- | --- |
(Admin)
Penambahan fitur CRUD
Manajemen Data Film
| 2   |     | Baik  | mandiri oleh admin dan upload  |     |     |
| --- | --- | ----- | ------------------------------ | --- | --- |
(Admin)
poster
| 1   | Rating & Review  | Buruk  |     | -   |     |
| --- | ---------------- | ------ | --- | --- | --- |
Penambahan fitur rating &
| 2   | Rating & Review  | Baik  | review dengan validasi hak  |     |     |
| --- | ---------------- | ----- | --------------------------- | --- | --- |
rating
| 1   | Pembayaran  | Buruk  |     | -   |     |
| --- | ----------- | ------ | --- | --- | --- |
Penambahan fitur pembayaran
2  Pembayaran via WhatsApp  Baik  via WhatsApp dan validasi oleh
admin
| 1   | Laporan Admin  | Buruk  |     | -   |     |
| --- | -------------- | ------ | --- | --- | --- |
Penambahan fitur laporan
| 2   | Laporan Admin  | Baik  | pemesanan (harian, film terlaris,  |     |     |
| --- | -------------- | ----- | ---------------------------------- | --- | --- |
pendapatan)
| 1   | Tampilan Antarmuka  | Cukup  |     | -   |     |
| --- | ------------------- | ------ | --- | --- | --- |
Perbaikan tampilan antarmuka
| 2   | Tampilan Antarmuka  | Baik  | menjadi lebih responsif dan  |     |     |
| --- | ------------------- | ----- | ---------------------------- | --- | --- |
menarik
Hasil Sprint Retrospective Keseluruhan
Apa yang berjalan dengan baik:
Pengembangan aplikasi web Cinema Booking berjalan dengan baik setelah
dilakukan evaluasi pada iterasi pertama. Penambahan fitur pemesanan tiket online,
validasi stok tiket secara real-time, halaman riwayat pemesanan, fitur rating &
review, serta pembayaran via WhatsApp membantu meningkatkan pengalaman
pengguna dalam melakukan pemesanan tiket bioskop secara lebih cepat dan efisien.
Selain itu, fitur pengelolaan data film dan jadwal tayang oleh admin, upload poster,
validasi  pembayaran,  serta  laporan  pemesanan  juga  berjalan  sesuai  kebutuhan
sistem. Seluruh story yang direncanakan (22 story) berhasil diselesaikan tepat waktu.
Apa yang perlu diperbaiki:
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Optimalisasi performa sistem masih perlu ditingkatkan terutama pada proses
pemesanan tiket ketika banyak pengguna mengakses sistem secara bersamaan
(mencegah race condition). Selain itu, tampilan antarmuka pada beberapa halaman
masih memerlukan penyempurnaan agar lebih konsisten dan mudah digunakan oleh
pengguna maupun admin. Proses validasi pembayaran via WhatsApp masih bersifat
manual, sehingga ke depannya dapat ditambahkan notifikasi otomatis.
Action plan untuk sprint berikutnya (jika ada):
Melakukan peningkatan performa aplikasi dan keamanan sistem,
menambahkan fitur notifikasi otomatis via WhatsApp Gateway, melakukan optimasi
tampilan antarmuka (UI/UX) secara menyeluruh, serta melakukan pengujian sistem
secara menyeluruh untuk memastikan seluruh fitur berjalan stabil dan sesuai
kebutuhan pengguna.
3.5.4 Tampilan Aplikasi beserta penjelasannya

3.6 Daftar Pustaka
[1] R. S. Pressman and B. R. Maxim, Software Engineering: A Practitioner's Approach, 9th
ed. New York: McGraw-Hill Education, 2020.
[2] A. S. Rosa and M. Shalahuddin, Rekayasa Perangkat Lunak Terstruktur dan Berorientasi
Objek. Bandung: Informatika, 2018.
[3] J. Enterprise, Pengenalan Pemrograman Berbasis Web. Jakarta: Elex Media Komputindo,
2019.
[4] K. E. Kendall and J. E. Kendall, Systems Analysis and Design, 10th ed. Boston: Pearson,
2020.
[5] I. Sommerville, Software Engineering, 10th ed. Essex: Pearson Education, 2016.
[6] A. Dennis, B. H. Wixom, and R. M. Roth, Systems Analysis and Design, 7th ed. Hoboken:
John Wiley & Sons, 2019.
[7] Firmansyah, S., & Voutama, A. (2024). Penerapan UML dalam Sistem Pemesanan Tiket
Bioskop Berbasis Website. JATI (Jurnal Mahasiswa Teknik Informatika), 8(6). [Online]
Available: https://mail.ejournal.itn.ac.id/jati/article/view/11731 [Accessed: 02-06-2026].
[8] Prayoga, E., Anandita, C. A. R., Putri, S. A., & Sumantri, R. B. B. (2023). Rancang Bangun
Aplikasi Pemesanan Tiket Bioskop XXI Cibaduyut Berbasis Website. Jurnal Sistem Informasi
dan Komputer (JSIK), 1(1), 12–24.
https://jurnal.kaputama.ac.id/index.php/JSIK/article/view/70
[9] Nasikhin, T. K., Putra, W. H. N., & Pramono, D. (2019). Analisis dan Perancangan Sistem
Informasi Reservasi Tour and Travel Menggunakan Metode OOAD pada Warok Tour and
Travel. Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer (J-PTIIK), 3(11),
10659–10666. http://j-ptiik.ub.ac.id/index.php/j-ptiik/article/view/6745
[10] Rospricilia, T. A., & Ma'ady, M. N. P. (2024). Pemodelan Integration Use Case (IUC):
Perancangan Use Case Diagram (UML) untuk Sistem-sistem yang Terintegrasi. INTEGER:
Journal of Information Technology, 9(2). https://ejurnal.itats.ac.id/integer/article/view/6345

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |
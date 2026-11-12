# Pembaruan galeri, pendaftaran, dan pemesanan

Pembaruan 12 November 2026. Bagian ini menggantikan batasan galeri/pendaftaran/pemesanan pada observasi awal di bawah.

- Seluruh 58 foto dari 8 album galeri asli telah disalin menjadi aset lokal. Album: Field Trips (7), Check-up Dokter Gigi dan Umum (5), Pesta Budaya (10), New Year Party (8), Imlek (6), Kemerdekaan (6), Portofolio Anak (4), Science Camp (12).
- Coba gratis, pendaftaran sekolah, dan pemesanan menyimpan data langsung ke database GPT Sites. Setiap permintaan mendapat nomor referensi dan status awal menunggu konfirmasi. Tidak ada jaminan penerimaan siswa atau slot otomatis.
- Halaman status menampilkan permintaan milik akun sendiri; pengelola yang dikonfigurasi di server dapat melihat dan mengubah status. Tidak ada pemberian hak pengelola otomatis kepada pengunjung pertama.
- Dokumen disimpan dalam penyimpanan privat GPT Sites (R2), dengan pemeriksaan hak akses pada setiap unggah/unduh. PDF/JPG/PNG maksimal 5 MB per berkas dan 10 berkas per permintaan.
- Pengujian lokal: 22 pemeriksaan API lulus, mencakup autentikasi, isolasi data pengguna, pencegahan duplikasi, pendaftaran, pemesanan, konflik versi status, unggah/unduh dokumen. Browser: pendaftaran contoh berhasil tersimpan dan bertahan setelah muat ulang, pengelola dapat mengonfirmasi, filter album dan navigasi foto bekerja. Semua data uji bersifat contoh dan hanya berada pada database lokal.
- Tidak ada gateway pembayaran, pemberitahuan email otomatis, atau integrasi kalender eksternal. Sekolah meninjau dan mengonfirmasi melalui halaman pengelolaan.
- Audiens situs tetap privat sesuai pengaturan sebelumnya. Belum dibuka untuk calon orang tua umum.

---

# Observasi dan pembuatan ulang Sekolah Pelangi Indonesia

Diamati 12 November 2026, Asia/Jakarta. Sumber: https://www.pi-education.com/ dan lima sitemap resmi Wix.

## Cakupan
122 URL pada sitemap berhasil diambil, 121 halaman kanonik unik: 22 halaman umum/kategori, 14 artikel, 26 detail kursus, serta 59 URL acara termasuk formulir acara. Angka ini menunjukkan inventaris konten publik, bukan bukti bahwa setiap layar/fitur sudah diuji interaktif satu per satu. Pemeriksaan browser dilakukan pada beranda dan galeri sumber, serta pratinjau hasil pembangunan.

## Hasil pengamatan
Identitas asli: logo lingkaran hijau, tagline Smart and Balanced Kids, menu Tentang (Tentang Kami, Program, Tenaga Pengajar), Sekolah (Pre-School, Homeschooling SD, SMP–SMA), Kursus, Psikologi, Pendaftaran, Galeri, FAQ, Blog. Beranda: slideshow 4 panel, profil dan 3 video YouTube, feed Instagram, informasi event kosong, 9 posisi testimoni, formulir kontak, peta, tautan sosial, akun anggota, chat Wix.

Pre-School mencakup Baby Class, Orange, Yellow, Green, Blue, PAUD Khusus, Half Day/Full Day, serta fasilitas. Homeschooling dan psikologi memiliki uraian kurikulum, metode, program dan layanan. Kursus memuat kelas berdasarkan kampus, deskripsi, durasi, tombol pemesanan, serta program animasi. Pendaftaran berisi coba gratis, panduan orang tua, harga via Drive, formulir unduhan dan dokumen pendaftaran. FAQ berisi inklusi, bahasa pengantar, trial, biaya, fasilitas, jadwal, agama, pakaian, perlengkapan, barang hilang. Blog memiliki artikel, kategori, pencarian dan profil penulis. Sitemap juga memuat arsip acara, halaman privasi, syarat, forum, dan live video.

## Pemetaan fungsi
| Fitur | Implementasi hasil | Batasan |
|---|---|---|
| Konten dan navigasi | 121 rute sumber + kontak dan arsip acara, menu desktop/ponsel | Tata letak disusun ulang, tidak identik piksel |
| Pencarian | Pencarian lokal seluruh teks halaman | Tidak memakai indeks Wix |
| FAQ | Buka-tutup jawaban | Isi mengikuti sumber |
| Kursus | Daftar, filter kampus/balet, tampilkan lebih banyak, detail | Kalender/pemesanan tetap Wix |
| Artikel | Daftar, detail, pencarian | Komentar, suka, akun tetap layanan asli |
| Arsip acara | Daftar dan detail beserta formulir sumber | Tidak menjanjikan acara lama masih dapat didaftarkan |
| Galeri | Foto dari halaman program dan pembesaran foto | 8 album dinamis Wix belum tersalin lengkap |
| Video | 3 embed YouTube dari sumber | Memerlukan layanan YouTube tersedia |
| Kontak | Form menyiapkan WhatsApp sesuai kampus | Tidak menyimpan/mengirim ke inbox Wix; pengguna menekan kirim sendiri |
| Peta | Tautan Google Maps kedua kampus | Bukan widget peta Wix |
| Pendaftaran | Informasi dan tautan formulir resmi | Form, unggah dokumen, database tetap di Wix |
| Unduhan | Tautan dokumen sumber dan folder Drive | Dokumen belum disalin; akses mengikuti penyedia |
| Akun, forum, chat | Tautan website asli; chat pengganti kontak WhatsApp | Bukan migrasi akun/riwayat/chat Wix |
| Instagram | Tautan sosial resmi | Feed langsung tidak dimigrasikan |
| Testimoni/slideshow | Kutipan asli dan susunan beranda baru | Semua panel/slideshow lama tidak direplikasi |

## Temuan yang perlu diperhatikan
Forum menampilkan Widget Didn't Load pada konten sumber. Jadwal kursus pada HTML publik masih Memuat hari…. Beranda, FAQ, dan halaman sekolah memiliki keterangan bahasa pengantar yang tidak sepenuhnya konsisten; tidak dinormalisasi tanpa konfirmasi sekolah. Promosi dan acara historis tidak dianggap masih berlaku. Informasi biaya/jadwal perlu konfirmasi admin. Tidak ada data anak, akun pengguna, atau pesan yang dikirim saat observasi dan pengujian.

## Inventaris halaman
| Halaman | Sumber |
|---|---|
| PAUD dan Homeschooling | [/](https://www.pi-education.com/) |
| Homeschooling SMP-SMA | [/about-6](https://www.pi-education.com/about-6) |
| Blog | [/blog](https://www.pi-education.com/blog) |
| Event Edukatif | [/blog/categories/event-edukatif](https://www.pi-education.com/blog/categories/event-edukatif) |
| Syarat dan Ketentuan | [/copy-of-kebijakan-privasi](https://www.pi-education.com/copy-of-kebijakan-privasi) |
| Pendaftaran | [/dokumen-pendaftaran-siswa-baru](https://www.pi-education.com/dokumen-pendaftaran-siswa-baru) |
| Bazaar dan Openday Sekolah Pelangi Indonesia | [/event-details/bazaar-dan-openday-sekolah-pelangi-indonesia](https://www.pi-education.com/event-details/bazaar-dan-openday-sekolah-pelangi-indonesia) |
| Family Sport Day (Openday) | [/event-details/family-sport-day-openday](https://www.pi-education.com/event-details/family-sport-day-openday) |
| FESTIVAL KREASI ANAK HEBAT PELANGI INDONESIA | [/event-details/festival-kreasi-anak-hebat-pelangi-indonesia](https://www.pi-education.com/event-details/festival-kreasi-anak-hebat-pelangi-indonesia) |
| FESTIVAL KREASI ANAK HEBAT PELANGI INDONESIA | [/event-details/festival-kreasi-anak-hebat-pelangi-indonesia-1](https://www.pi-education.com/event-details/festival-kreasi-anak-hebat-pelangi-indonesia-1) |
| First Aid on Mental Health (P3K Jiwa) | [/event-details/first-aid-on-mental-health-p3k-jiwa](https://www.pi-education.com/event-details/first-aid-on-mental-health-p3k-jiwa) |
| Kelas Green | [/event-details/kelas-green](https://www.pi-education.com/event-details/kelas-green) |
| Kelas Green (Dummy) | [/event-details/kelas-green-dummy](https://www.pi-education.com/event-details/kelas-green-dummy) |
| KOPPITZ-2 Sistem Skoring Tes Integrasi Visual Motor Bender Gestalt | [/event-details/koppitz-2-sistem-skoring-tes-integrasi-visual-motor-bender-gestalt](https://www.pi-education.com/event-details/koppitz-2-sistem-skoring-tes-integrasi-visual-motor-bender-gestalt) |
| lah | [/event-details/lah](https://www.pi-education.com/event-details/lah) |
| Layanan Konseling Online Gratis bagi Tenaga Kesehatan | [/event-details/layanan-konseling-online-gratis-bagi-tenaga-kesehatan](https://www.pi-education.com/event-details/layanan-konseling-online-gratis-bagi-tenaga-kesehatan) |
| Liburan Anak Hebat | [/event-details/liburan-anak-hebat](https://www.pi-education.com/event-details/liburan-anak-hebat) |
| Liburan Anak Hebat di Yogyakarta | [/event-details/liburan-anak-hebat-di-yogyakarta](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta) |
| Liburan Anak Hebat di Yogyakarta Desember 2022 | [/event-details/liburan-anak-hebat-di-yogyakarta-desember-2022](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-desember-2022) |
| Liburan Anak Hebat di Yogyakarta Desember 2023 | [/event-details/liburan-anak-hebat-di-yogyakarta-desember-2023](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-desember-2023) |
| Liburan Anak Hebat di Yogyakarta Desember 2024 | [/event-details/liburan-anak-hebat-di-yogyakarta-desember-2024](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-desember-2024) |
| Liburan Anak Hebat di Yogyakarta Desember 2025 | [/event-details/liburan-anak-hebat-di-yogyakarta-desember-2025](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-desember-2025) |
| Liburan Anak Hebat di Yogyakarta Juni 2023 | [/event-details/liburan-anak-hebat-di-yogyakarta-juni-2023](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-juni-2023) |
| Liburan Anak Hebat di Yogyakarta Juni 2024 | [/event-details/liburan-anak-hebat-di-yogyakarta-juni-2024](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-juni-2024) |
| Liburan Anak Hebat di Yogyakarta Juni 2025 | [/event-details/liburan-anak-hebat-di-yogyakarta-juni-2025](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-juni-2025) |
| Liburan Anak Hebat di Yogyakarta Juni-Juli 2026 | [/event-details/liburan-anak-hebat-di-yogyakarta-juni-juli-2026](https://www.pi-education.com/event-details/liburan-anak-hebat-di-yogyakarta-juni-juli-2026) |
| Membangun Resiliensi Gen Z | [/event-details/membangun-resiliensi-gen-z](https://www.pi-education.com/event-details/membangun-resiliensi-gen-z) |
| Mini Openday Pelangi Indonesia School | [/event-details/mini-openday-pelangi-indonesia-school](https://www.pi-education.com/event-details/mini-openday-pelangi-indonesia-school) |
| Montessori for Babies (1-2 tahun) | [/event-details/montessori-for-babies-1-2-tahun](https://www.pi-education.com/event-details/montessori-for-babies-1-2-tahun) |
| Montessori itu Mudah dan Murah | [/event-details/montessori-itu-mudah-dan-murah](https://www.pi-education.com/event-details/montessori-itu-mudah-dan-murah) |
| Multicultural Party: Arjuna Melawan Pandemi | [/event-details/multicultural-party-arjuna-melawan-pandemi](https://www.pi-education.com/event-details/multicultural-party-arjuna-melawan-pandemi) |
| Njajal | [/event-details/njajal](https://www.pi-education.com/event-details/njajal) |
| nyoba lagi | [/event-details/nyoba-lagi](https://www.pi-education.com/event-details/nyoba-lagi) |
| OPEN DAY PELANGI INDONESIA | [/event-details/open-day-pelangi-indonesia](https://www.pi-education.com/event-details/open-day-pelangi-indonesia) |
| Open Day Sekolah Pelangi Indonesia 4 Oktober 2025 | [/event-details/open-day-sekolah-pelangi-indonesia-4-oktober-2025](https://www.pi-education.com/event-details/open-day-sekolah-pelangi-indonesia-4-oktober-2025) |
| Open Recruitment | [/event-details/open-recruitment](https://www.pi-education.com/event-details/open-recruitment) |
| Openday | [/event-details/openday](https://www.pi-education.com/event-details/openday) |
| Openday | [/event-details/openday-2](https://www.pi-education.com/event-details/openday-2) |
| Openday and Fun Walk 2026 Pelangi Indonesia | [/event-details/openday-and-fun-walk-2026-pelangi-indonesia](https://www.pi-education.com/event-details/openday-and-fun-walk-2026-pelangi-indonesia) |
| Openday Pelangi Indonesia School | [/event-details/openday-pelangi-indonesia-school](https://www.pi-education.com/event-details/openday-pelangi-indonesia-school) |
| Openday Pelangi Indonesia School | [/event-details/openday-pelangi-indonesia-school-2](https://www.pi-education.com/event-details/openday-pelangi-indonesia-school-2) |
| Openday Pelangi Indonesia School | [/event-details/openday-pelangi-indonesia-school-4](https://www.pi-education.com/event-details/openday-pelangi-indonesia-school-4) |
| Openday Pelangi Indonesia School | [/event-details/openday-pelangi-indonesia-school-5](https://www.pi-education.com/event-details/openday-pelangi-indonesia-school-5) |
| Openday Pelangi Indonesia School | [/event-details/openday-pelangi-indonesia-school-6](https://www.pi-education.com/event-details/openday-pelangi-indonesia-school-6) |
| Pelangi Indonesia | [/event-details/pelangi-indonesia](https://www.pi-education.com/event-details/pelangi-indonesia) |
| Pelatihan Tes Deteksi Dini Disleksia | [/event-details/pelatihan-tes-deteksi-dini-disleksia](https://www.pi-education.com/event-details/pelatihan-tes-deteksi-dini-disleksia) |
| Pelatihan Tes Deteksi Dini Disleksia (Tes 3D) | [/event-details/pelatihan-tes-deteksi-dini-disleksia-tes-3d](https://www.pi-education.com/event-details/pelatihan-tes-deteksi-dini-disleksia-tes-3d) |
| Pemeriksaan Perkembangan dan Gangguan Perkembangan Anak: Denver II, Suryakanti, KPSP, CHAT, KMME, GPPH | [/event-details/pemeriksaan-perkembangan-dan-gangguan-perkembangan-anak-denver-ii-suryakanti-kpsp-chat-kmme-gpph](https://www.pi-education.com/event-details/pemeriksaan-perkembangan-dan-gangguan-perkembangan-anak-denver-ii-suryakanti-kpsp-chat-kmme-gpph) |
| Pemeriksaan Perkembangan dan Gangguan Perkembangan Anak: Tes VABS/VSMS | [/event-details/pemeriksaan-perkembangan-dan-gangguan-perkembangan-anak-tes-vabs-vsms](https://www.pi-education.com/event-details/pemeriksaan-perkembangan-dan-gangguan-perkembangan-anak-tes-vabs-vsms) |
| PERKEMBANGAN ANAK : MEMAHAMI TUMBUH KEMBANG ANAK SESUAI USIA | [/event-details/perkembangan-anak-memahami-tumbuh-kembang-anak-sesuai-usia](https://www.pi-education.com/event-details/perkembangan-anak-memahami-tumbuh-kembang-anak-sesuai-usia) |
| Seni Mencintai Diri dengan Self Compassion | [/event-details/seni-mencintai-diri-dengan-self-compassion](https://www.pi-education.com/event-details/seni-mencintai-diri-dengan-self-compassion) |
| Student Camp Pelangi Indonesia | [/event-details/student-camp-pelangi-indonesia](https://www.pi-education.com/event-details/student-camp-pelangi-indonesia) |
| Student Camp Pelangi Indonesia | [/event-details/student-camp-pelangi-indonesia-2](https://www.pi-education.com/event-details/student-camp-pelangi-indonesia-2) |
| Student Camp Pelangi Indonesia  Juli 2026 | [/event-details/student-camp-pelangi-indonesia-juli-2026](https://www.pi-education.com/event-details/student-camp-pelangi-indonesia-juli-2026) |
| Student Camp Pelangi Indonesia  Juni 2025 | [/event-details/student-camp-pelangi-indonesia-juni-2025](https://www.pi-education.com/event-details/student-camp-pelangi-indonesia-juni-2025) |
| Temukan Cara Membangun Bisnis Kursus | [/event-details/temukan-cara-membangun-bisnis-kursus](https://www.pi-education.com/event-details/temukan-cara-membangun-bisnis-kursus) |
| TES BENDER GESTALT: KOPPITZ-2 | [/event-details/tes-bender-gestalt-koppitz-2](https://www.pi-education.com/event-details/tes-bender-gestalt-koppitz-2) |
| Tes Kepribadian | [/event-details/tes-kepribadian](https://www.pi-education.com/event-details/tes-kepribadian) |
| Tes Minat-Bakat-Karir | [/event-details/tes-minat-bakat-karir](https://www.pi-education.com/event-details/tes-minat-bakat-karir) |
| Test | [/event-details/test](https://www.pi-education.com/event-details/test) |
| Webinar Sehat Mental Mengawali Resolusi Tahun Baru | [/event-details/webinar-sehat-mental-mengawali-resolusi-tahun-baru](https://www.pi-education.com/event-details/webinar-sehat-mental-mengawali-resolusi-tahun-baru) |
| Webinar TES FUNGSI EMOSI DAN TINGKAT PSIKOPATOLOGI | [/event-details/webinar-tes-fungsi-emosi-dan-tingkat-psikopatologi](https://www.pi-education.com/event-details/webinar-tes-fungsi-emosi-dan-tingkat-psikopatologi) |
| Webinar Tes Proyeksi CHaD | [/event-details/webinar-tes-proyeksi-chad](https://www.pi-education.com/event-details/webinar-tes-proyeksi-chad) |
| Workshop Online: TES FUNGSI EMOSI DAN TINGKAT PSIKOPATOLOGI | [/event-details/workshop-online-tes-fungsi-emosi-dan-tingkat-psikopatologi](https://www.pi-education.com/event-details/workshop-online-tes-fungsi-emosi-dan-tingkat-psikopatologi) |
| WORKSHOP PENANGANAN TERINTEGRASI ANAK DENGAN AUTISM SPECTRUM DISORDER | [/event-details/workshop-penanganan-terintegrasi-anak-dengan-autism-spectrum-disorder](https://www.pi-education.com/event-details/workshop-penanganan-terintegrasi-anak-dengan-autism-spectrum-disorder) |
| Frequently Asked Questions (FAQ) | [/faq](https://www.pi-education.com/faq) |
| Blank | [/form-coba-gratis](https://www.pi-education.com/form-coba-gratis) |
| Forum | [/forum](https://www.pi-education.com/forum) |
| Galeri Foto | [/gallery](https://www.pi-education.com/gallery) |
| Kebijakan Privasi | [/general-4](https://www.pi-education.com/general-4) |
| Metode Pembelajaran | [/homeschooling-sd-smp-1](https://www.pi-education.com/homeschooling-sd-smp-1) |
| Kursus Anak Jogja | [/kursus](https://www.pi-education.com/kursus) |
| Kursus Anak Jogja | [/kursus-3a-pelangi-indonesia](https://www.pi-education.com/kursus-3a-pelangi-indonesia) |
| Live Video | [/live-video](https://www.pi-education.com/live-video) |
| Pendaftaran | [/pendaftaran](https://www.pi-education.com/pendaftaran) |
| Anak Kita Pasti Cerdas | [/post/anak-kita-pasti-cerdas](https://www.pi-education.com/post/anak-kita-pasti-cerdas) |
| Bumiku Hanya Satu | [/post/bumiku-hanya-satu](https://www.pi-education.com/post/bumiku-hanya-satu) |
| Gardening Pelangi Indonesia, Menanam Sansivieria | [/post/gardening-pelangi-indonesia-menanam-sansivieria](https://www.pi-education.com/post/gardening-pelangi-indonesia-menanam-sansivieria) |
| KOPPITZ-2 Sistem Skoring Tes Integrasi Visual Motor Bender Gestalt | [/post/koppitz-2-sistem-skoring-tes-integrasi-visual-motor-bender-gestalt](https://www.pi-education.com/post/koppitz-2-sistem-skoring-tes-integrasi-visual-motor-bender-gestalt) |
| Merayakan Kemenangan dalam Keberagaman: Indahnya Kebersamaan Idul Fitri di Sekolah Pelangi Indonesia | [/post/merayakan-kemenangan-dalam-keberagaman-indahnya-kebersamaan-idul-fitri-di-sekolah-pelangi-indonesia](https://www.pi-education.com/post/merayakan-kemenangan-dalam-keberagaman-indahnya-kebersamaan-idul-fitri-di-sekolah-pelangi-indonesia) |
| Ngobrol dengan Anak | [/post/ngobrol-dengan-anak](https://www.pi-education.com/post/ngobrol-dengan-anak) |
| Pelatihan Tes Deteksi Dini Disleksia | [/post/pelatihan-tes-deteksi-dini-disleksia](https://www.pi-education.com/post/pelatihan-tes-deteksi-dini-disleksia) |
| Pentingnya Anak Belajar Memasak | [/post/pentingnya-anak-belajar-memasak](https://www.pi-education.com/post/pentingnya-anak-belajar-memasak) |
| Read Aloud for Parents | [/post/read-aloud-for-parents](https://www.pi-education.com/post/read-aloud-for-parents) |
| Selamat Datang di Blog Pelangi Indonesia | [/post/selamat-datang-di-blog-pelangi-indonesia](https://www.pi-education.com/post/selamat-datang-di-blog-pelangi-indonesia) |
| Separation Anxiety | [/post/separation-anxiety](https://www.pi-education.com/post/separation-anxiety) |
| Separation Anxiety | [/post/separation-anxiety-1](https://www.pi-education.com/post/separation-anxiety-1) |
| Training Karyawan : Resiliensi di Masa Pandemi | [/post/training-karyawan-resiliensi-di-masa-pandemi](https://www.pi-education.com/post/training-karyawan-resiliensi-di-masa-pandemi) |
| Workhop Penanganan Terintegrasi Perilaku Bermasalah Pada Anak | [/post/workhop-penanganan-terintegrasi-perilaku-bermasalah-pada-anak](https://www.pi-education.com/post/workhop-penanganan-terintegrasi-perilaku-bermasalah-pada-anak) |
| Metode Pembelajaran | [/pre-school](https://www.pi-education.com/pre-school) |
| Program | [/program](https://www.pi-education.com/program) |
| Layanan Psikologi | [/s-projects-side-by-side](https://www.pi-education.com/s-projects-side-by-side) |
| Sekolah | [/sekolah](https://www.pi-education.com/sekolah) |
| Les Baca Tulis Jogja | [/service-page/baca-tulis-3a-bantul](https://www.pi-education.com/service-page/baca-tulis-3a-bantul) |
| Ballet Baby Class (Bantul) | [/service-page/ballet-baby-class-bantul](https://www.pi-education.com/service-page/ballet-baby-class-bantul) |
| Ballet Baby Class (Jogja) | [/service-page/ballet-baby-class-jogja](https://www.pi-education.com/service-page/ballet-baby-class-jogja) |
| Ballet Grade 1 (Bantul) | [/service-page/ballet-grade-1-bantul](https://www.pi-education.com/service-page/ballet-grade-1-bantul) |
| Ballet Grade 1 (Jogja) | [/service-page/ballet-grade-1-jogja](https://www.pi-education.com/service-page/ballet-grade-1-jogja) |
| Ballet Grade 2 (Bantul) | [/service-page/ballet-grade-2-bantul](https://www.pi-education.com/service-page/ballet-grade-2-bantul) |
| Ballet Grade 2 (Jogja) | [/service-page/ballet-grade-2-jogja-1](https://www.pi-education.com/service-page/ballet-grade-2-jogja-1) |
| Ballet Grade 3 (Bantul) | [/service-page/ballet-grade-3-bantul](https://www.pi-education.com/service-page/ballet-grade-3-bantul) |
| Ballet Grade 3 (Jogja) | [/service-page/ballet-grade-3-jogja](https://www.pi-education.com/service-page/ballet-grade-3-jogja) |
| Ballet Grade 4 (Jogja) | [/service-page/ballet-grade-4-jogja](https://www.pi-education.com/service-page/ballet-grade-4-jogja) |
| Ballet Grade 5 (Jogja) | [/service-page/ballet-grade-5-jogja](https://www.pi-education.com/service-page/ballet-grade-5-jogja) |
| Ballet Grade 6 (Jogja) | [/service-page/ballet-grade-6-jogja](https://www.pi-education.com/service-page/ballet-grade-6-jogja) |
| Ballet Intermediate Foundation (Jogja) | [/service-page/ballet-intermediate-foundation-jogja](https://www.pi-education.com/service-page/ballet-intermediate-foundation-jogja) |
| Ballet Pre Primary (Bantul) | [/service-page/ballet-pre-primary-bantul](https://www.pi-education.com/service-page/ballet-pre-primary-bantul) |
| Ballet Pre Primary (Jogja) | [/service-page/ballet-pre-primary-jogja](https://www.pi-education.com/service-page/ballet-pre-primary-jogja) |
| Ballet Pre School (Bantul) | [/service-page/ballet-pre-school-bantul](https://www.pi-education.com/service-page/ballet-pre-school-bantul) |
| Ballet Pre School (Jogja) | [/service-page/ballet-pre-school-jogja](https://www.pi-education.com/service-page/ballet-pre-school-jogja) |
| Ballet Primary (Bantul) | [/service-page/ballet-primary-bantul](https://www.pi-education.com/service-page/ballet-primary-bantul) |
| Ballet Primary (Jogja) | [/service-page/ballet-primary-jogja](https://www.pi-education.com/service-page/ballet-primary-jogja) |
| Bimbingan Belajar (Bimbel) Jogja | [/service-page/bimbingan-belajar-bimbel-jogja](https://www.pi-education.com/service-page/bimbingan-belajar-bimbel-jogja) |
| Les Baca Tulis Jogja | [/service-page/kelas-baca-tulis-3a-jogja](https://www.pi-education.com/service-page/kelas-baca-tulis-3a-jogja) |
| Les Tae Kwon Do Jogja | [/service-page/kelas-tae-kwon-do-3A-jogja](https://www.pi-education.com/service-page/kelas-tae-kwon-do-3A-jogja) |
| Les Tae Kwon Do Jogja | [/service-page/kelas-tae-kwon-do-bantul](https://www.pi-education.com/service-page/kelas-tae-kwon-do-bantul) |
| Kursus Matematika Jogja | [/service-page/kursus-matematika-3a](https://www.pi-education.com/service-page/kursus-matematika-3a) |
| Kursus Tari Tradisional Jogja | [/service-page/kursus-tari-tradisional-jogja](https://www.pi-education.com/service-page/kursus-tari-tradisional-jogja) |
| Kursus Sempoa Jogja | [/service-page/sempoa-jogja](https://www.pi-education.com/service-page/sempoa-jogja) |
| Tenaga Pengajar | [/tenaga-pengajar](https://www.pi-education.com/tenaga-pengajar) |
| Tentang Kami | [/tentang-kami](https://www.pi-education.com/tentang-kami) |

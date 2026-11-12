# Sekolah Pelangi Indonesia

Website GPT Sites berdasarkan konten publik pi-education.com. Desain mengikuti HTML dan CSS asli per halaman pi-education.com, dengan galeri lengkap serta pendaftaran dan pemesanan mandiri.

## Halaman utama
- `/gallery`: 8 album dan 58 foto asli.
- `/pendaftaran`: pilihan pendaftaran, coba gratis, dokumen.
- `/daftar`: pendaftaran sekolah.
- `/form-coba-gratis`: coba gratis.
- `/pemesanan`: usulan jadwal kursus, psikologi, atau kunjungan.
- `/status-pendaftaran`: data milik akun, status dan dokumen.
- `/pengelola`: daftar dan pembaruan status khusus pengelola.

## Operasional
Data disimpan di D1 (`DB`), dokumen privat di R2 (`BUCKET`). Setel `ADMIN_EMAIL` melalui runtime secret Sites untuk pengelola. Identitas pengunjung berasal dari autentikasi ChatGPT milik Sites. Jangan menambahkan OAuth atau logika pengelola pertama.

Permintaan awal berstatus pending dan harus dikonfirmasi sekolah. Tidak ada tagihan, pembayaran, email otomatis atau sinkronisasi kalender. Audiens tetap privat.

## Pengembangan
`npm run dev` untuk pratinjau; `npm run build` untuk build; `npm run db:generate` setelah perubahan schema. Migrasi tersimpan di drizzle/. `tests/integration.py` hanya untuk Worker produksi lokal pada 127.0.0.1:5174 dengan identitas uji dan ADMIN_EMAIL=seedy@sites.test; jangan menjalankan terhadap produksi. Database lokal dan runtime produksi terpisah.

Aset dan konten frontend di public/, shell di shell.html dan app/shell.ts, endpoint di app/api/. public/app.js mempertahankan tampilan lama; public/features.js menyediakan alur pendaftaran dan galeri terbaru.

## Replikasi tampilan asli
121 rute desktop dan 120 versi mobile dipertahankan di public/original dan public/original-mobile; rute mobile yang tidak tersedia memakai versi desktop. CSS asli dideduplikasi ke public/original/styles. Skrip dan data runtime Wix dihapus. Adapter mandiri menangani menu, slideshow, video, pencarian, chat kampus dan album foto. Header/footer/formulir backend memakai identitas visual yang sama; akun dan penyimpanan tetap memakai ChatGPT/GPT Sites, bukan akun Wix.

app/original-routes.json dan app/original-mobile-routes.json memilih dokumen sesuai rute dan perangkat. Binding ASSETS melayani dokumen lewat Worker tanpa mengubah DB/BUCKET. shell.ts dan shell-mobile.ts membungkus fitur pendaftaran yang sudah ada. Referensi mentah research/ dan research-mobile/ tidak dipublikasikan.


## Formulir, akun, dan chat

Formulir coba gratis, pendaftaran sekolah, serta pemesanan menggunakan tampilan dua tahap dengan bidang abu-abu mengikuti situs asal. Kolom nama panggilan ditambahkan secara kompatibel ke pendaftaran yang sudah ada. Panel Masuk/Daftar mengikuti susunan asli; penyedia autentikasi tetap ChatGPT. `/akun` memuat identitas akun dan pintasan pendaftaran, dokumen, serta chat.

Chat Langsung menyimpan pesan pada D1, bukan Wix atau penyimpanan browser. Pengunjung harus masuk sebelum mengirim atau membaca percakapan. Setiap percakapan terikat pada identitas pemilik; hanya pemilik dan pengelola yang dikonfigurasi dapat membacanya. Pengelola membalas melalui bagian Pesan Orang Tua di `/pengelola`. Pesan memuat teks saja, dirender dengan escaping, dibatasi panjang dan laju, serta mensyaratkan asal permintaan yang sama. Tampilan tidak mengklaim petugas sedang online. Tidak ada notifikasi eksternal atau balasan otomatis.

Migrasi `0001_chemical_magus.sql` hanya menambahkan tabel chat beserta indeks dan kolom nama panggilan; dokumen R2 serta data pendaftaran lama tetap menggunakan penyimpanan dan otorisasi yang sama. Jangan menyimpan data pendaftar, pesan, dokumen, atau rahasia runtime ke Git.

Pengujian lokal: `python3 tests/integration.py` (22 pemeriksaan) dan `python3 tests/chat.py` (15 pemeriksaan). Kedua skrip hanya memakai Worker lokal pada port 5174 dan identitas fiktif. Jangan jalankan terhadap produksi.

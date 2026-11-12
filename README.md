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

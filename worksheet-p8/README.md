# PABW — Amadeus Dharma Akbarindra — NIM25523253

Repo ini memuat Daftar Film yang sudah saya tonton.
Struktur berupa nama film, tahun rilis, sutradara, dan rating di IMDb.

## Pertemuan 3 — Halaman profil saya

Topik halaman saya: Daftar Film yang Pernah Saya Tonton

- Judul halaman: Daftar Film yang Pernah Saya Tonton
- Deskripsi: Halaman ini menampilkan daftar film yang pernah saya tonton beserta tahun rilis, sutradara, dan rating IMDb.
- Tautan navigasi: Beranda, Daftar Film, Tentang Saya
- Dua bagian utama: Daftar Film dan Tambah List Film
- Kolom tabel: Judul Film, Tahun Rilis, Sutradara, Rating IMDb
- Kolom form: Judul Film, Tahun Rilis, Sutradara, Rating IMDb
- Gambar: poster film Inception

## Catatan penggunaan AI

Tidak memakai AI. Semua isi halaman, struktur, data film, dan konten dibuat sendiri.

## Pertemuan 4 - Design Token Halaman Profil

- Berkas gaya yang digunakan: tokens.css, base.css, layout.css, komponen.css, dan tema.css.
- Warna utama yang dipilih adalah merah #B91C1C karena memberikan tampilan yang sederhana dan tegas pada halaman daftar film.
- Design token digunakan agar perubahan warna, jarak, ukuran huruf, dan tampilan komponen dapat dilakukan secara terpusat.
- Kriteria selesai: perubahan warna utama pada token dapat diterapkan ke komponen yang menggunakan token semantik.

## Catatan penggunaan AI

Tidak memakai AI. Semua isi halaman, struktur, data film, dan konten dibuat sendiri.

## Pertemuan 5 — Layout Modern: Flexbox dan Grid

### Lembar A — Kerangka Halaman dan Penentuan Sumbu
- **A.1 Kerangka Halaman**:
  - Baris pertama (Header): `auto` (tinggi mengikuti isi).
  - Baris kedua (Isi): `1fr` (mengisi sisa tinggi layar).
  - Baris ketiga (Footer): `auto` (tinggi mengikuti isi).
  - Kolom isi: `16rem 1fr` (sidebar tetap 16rem, konten utama lentur 1fr).
- **A.2 Sumbu dan Arah Flexbox**:
  - Navbar: arah baris (*row*), sumbu utama horizontal, sumbu silang vertikal.
  - Baris info/kaki kartu: arah baris (*row*), sumbu utama horizontal, sumbu silang vertikal.
  - Kartu sidebar: arah kolom (*column*), sumbu utama vertikal, sumbu silang horizontal.
- **A.3 Kapan Flex, Kapan Grid**:
  - Kepala halaman: Flex (penataan satu baris antara brand dan tautan navigasi).
  - Isi dua kolom: Grid (kerangka 2 dimensi membagi area sidebar dan konten).
  - Galeri kartu: Grid (multi-kolom adaptif responsif dengan `auto-fit` dan `minmax`).
  - Isi di dalam kartu: Flex (penataan berderet elemen keterangan dan tombol).

### Lembar B & C — Penerapan Layout & Komponen
- `layout.css`: Kerangka `.page` menggunakan CSS Grid `auto 1fr auto` dengan `min-height: 100dvh`. Navbar menggunakan Flexbox dengan `gap: var(--space-4)`. Kolom `.isi` menggunakan CSS Grid `16rem 1fr`.
- `komponen.css`: Galeri menggunakan `repeat(auto-fit, minmax(16rem, 1fr))` sehingga jumlah kolom otomatis menyesuaikan tanpa media query. Isi kartu (`.kartu__kaki` dan `.kartu__info`) menggunakan Flexbox berderet.
- Semua jarak antar-elemen menggunakan `gap`, tanpa margin tempelan dan tanpa `float`.

### Lembar D — Penempatan Khusus (*Span* & *Area Bernama*)
- Area bernama pada `.isi`:
  - `grid-template-areas: "sisi utama" "sisi bawah";`
  - `.sisi` menggunakan `grid-area: sisi;` (menjangkau 2 baris).
  - `.utama` menggunakan `grid-area: utama;`.
  - `.bawah` menggunakan `grid-area: bawah;`.
- *Span*: Kartu sorotan film pertama (`.sorotan`) menggunakan `grid-column: span 2;` pada layar yang mencukupi.

### Lembar E — Penanganan Kasus Meluber & Ketidakteraturan
- Menggunakan `min-height: 14rem` dan `align-content: start` pada `.galeri .kartu` agar tinggi kartu seragam.
- Menambahkan `min-width: 0;` pada `.kartu__isi` dan `overflow-wrap: anywhere;` pada `.kartu__judul` untuk mencegah teks panjang melebarkan kolom secara paksa.

### Lembar F — Tiket Keluar & Evaluasi
1. **Bagian halaman yang memakai Flex**: Navbar dan bagian kaki kartu (`.kartu__kaki`), karena menyusun elemen secara satu arah (horizontal) dengan distribusi ruang yang rapi.
2. **Bagian halaman yang memakai Grid**: Kerangka halaman (`.page`), area isi (`.isi`), dan `.galeri`, karena membagi tata letak dua dimensi (baris dan kolom) serta mendukung penyesuaian kolom otomatis tanpa media query.
3. **Kasus meluber dan perbaikannya**: Teks panjang yang mendorong lebar kolom secara bawaan, diperbaiki dengan memberikan `min-width: 0` pada elemen anak grid/flex dan `overflow-wrap: anywhere`.
4. **Hasil Pengujian**:
   - Diuji pada resolusi **360 px** (HP) dan **1280 px** (Desktop): nol elemen meluber (0 horizontal overflow).
   - Fitur tema gelap dari Pertemuan 4 tetap berfungsi dengan baik.

## Pertemuan 6 — Responsif Mobile-First

- Berkas tambahan baru: responsif.css
- Meta viewport terpasang di profil.html: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
- Pendekatan Mobile-First: gaya dasar ditulis untuk layar sempit tanpa media query (default 1 kolom).
- Dua titik henti (breakpoint) menggunakan `min-width` dan satuan `rem`:
  - `48rem` (~768px): Galeri kartu bertransformasi menjadi 2 kolom.
  - `60rem` (~960px): Sidebar bersanding di samping konten utama (`16rem 1fr`) dan galeri bertransformasi menjadi 3 kolom.
- Pembatasan media: `max-width: 100%` dan `height: auto` pada elemen gambar, `.table-wrap` dengan `overflow-x: auto`.
- Hasil Pengujian:
  - Layar 360 px: Tampilan satu kolom rapi, teks proporsional, 0 gulir mendatar.
  - Layar 768 px: Galeri kartu 2 kolom seimbang, 0 gulir mendatar.
  - Layar 1 280 px: Sidebar dan konten bersanding dengan 3 kolom kartu, 0 gulir mendatar.

## Catatan penggunaan AI

Tidak memakai AI. Semua isi halaman, struktur, data film, dan konten dibuat sendiri.

## Pertemuan 8 — JavaScript Modern ES6+, Struktur Data, dan Array Methods

Pertemuan ini berfokus pada transformasi data halaman dari teks statis di dalam HTML menjadi struktur data JavaScript (ES6+) yang modular, bersih, dan dinamis di dalam berkas `js/app.js`.

### 1. Lembar A — Menyambungkan Skrip ke Halaman
- Dibuat folder `js/` yang memuat berkas `app.js`.
- Skrip dihubungkan tepat sebelum tag penutup `</body>` pada `profil.html` menggunakan atribut modul:
  ```html
  <script type="module" src="js/app.js"></script>
  ```
- Halaman dijalankan melalui server lokal (`http://localhost:8000` via Python `http.server` atau Live Server VS Code) untuk mematuhi kebijakan keamanan modul ES6 (mencegah galat CORS `file://`).
- Console peramban dipastikan bersih tanpa galat merah maupun status 404.

### 2. Lembar B — Data Halaman sebagai Variabel
- Data identitas profil dipindahkan menjadi objek JavaScript menggunakan `const`:
  ```javascript
  const profil = {
    nama: "Amadeus Dharma Akbarindra",
    nim: "25523253",
    peran: "Mahasiswa Informatika yang belajar front-end & mengulas film",
    keahlian: ["HTML", "CSS", "JavaScript", "Analisis Film", "Kurasi Konten"],
    jumlahFilm: 4,
    kontak: {
      email: "herizor5008@gmail.com",
      github: "indraa-dharma",
      kota: "Yogyakarta"
    }
  };
  ```
- Deklarasi `let` digunakan secara spesifik untuk nilai yang dapat berubah (misalnya penanda filter: `let filterStatusAktif = "semua"`).
- Penyusunan kalimat dinamis menggunakan template literal (backtick dan `${...}`).
- Penerapan operator modern JavaScript:
  - *Nullish Coalescing Operator* (`??`) untuk menangani nilai bawaan saat bernilai `null` atau `undefined`.
  - *Optional Chaining Operator* (`?.`) untuk mengakses properti bersarang secara aman tanpa memicu `TypeError`.

### 3. Lembar C — Dua Fungsi Murni (Pure Functions)
- Dibuat dua fungsi murni yang deterministik, hanya bergantung pada argumen yang dikirim, dan tidak menghasilkan efek samping (*side effects*):
  1. `buatPerkenalan({ nama, peran })`: Menyusun kalimat perkenalan dari satu objek profil menggunakan teknik *destructuring*.
  2. `formatKeahlian = (daftar) => daftar.join(" · ")`: Merapikan array daftar keahlian menjadi satu baris teks dengan pemisah titik tengah.

### 4. Lembar D — Struktur Data dan Array Methods
- Seluruh koleksi film dikelola dalam struktur *Array of Objects* (`daftarFilm` / `daftarProyek`).
- Setiap objek film memuat atribut: `id`, `judul`, `tahun`, `sutradara`, `rating`, `genre`, `selesai`, dan `sinopsis`.
- Pengujian dan manipulasi data menggunakan array methods:
  - `console.table(daftarProyek)`: Menampilkan seluruh baris data ke dalam format tabel rapi di Console.
  - `filter`: Menyaring film yang sudah ditonton (`selesai: true`), menghasilkan 3 film yang cocok.
  - `find`: Mencari film dengan judul tertentu (`"Inception"`), menghasilkan 1 objek lengkap.
  - `map`: Mentransformasi array objek menjadi array ringkasan string format `"${judul} (${tahun}) - IMDb ${rating}"`.
  - `sort` tanpa mutasi: Menggunakan spread operator `[...daftarFilm].sort((a, b) => b.rating - a.rating)` sehingga urutan data asli tetap utuh dan aman.

### 5. Lembar E — Penanganan Galat & Kebersihan Console
- Tiga kasus sulit JavaScript ditangani secara terstruktur:
  1. Penanganan properti `undefined` / `null` dengan *Optional Chaining* (`?.`) dan *Nullish Coalescing* (`??`).
  2. Penanganan `querySelector` yang bernilai `null` dengan pengondisian `if (formElemen)` sebelum mengakses properti elemen.
  3. Konversi nilai input form dari teks ke angka menggunakan `Number(input.value)` sebelum dilakukan penjumlahan agar terhindar dari konkatenasi teks.
- Disimpan tiga tangkapan layar Console di repositori:
  - `screenshot_galat.png`: Kondisi saat galat muncul di Console (demonstrasi TypeError).
  - `screenshot_diperbaiki.png`: Kondisi Console bersih tanpa galat setelah perbaikan.
  - `screenshot_tabel.png`: Kondisi Console saat menampilkan tabel data via `console.table`.

### 6. Lembar F — Tiket Keluar & Dokumen Worksheet Terisi
- Seluruh evaluasi mandiri, catatan pengampu, dan jawaban tiket keluar diisi secara mendalam.
- Berkas dokumen Microsoft Word terisi lengkap disimpan sebagai `AMADEUS DHARMA AKBARINDRA - 25523253 - 8. Worksheet_PABW_Pertemuan8.docx`.

## Catatan Penggunaan AI (Pertemuan 8)

- **Bagian yang dibantu AI**:
  - Asistensi pembuatan skrip otomasi pengisian dan penyusunan berkas lembar kerja Word (`build_completed_worksheet.py`) untuk menyalin template secara presisi, memformat tabel, dan menyisipkan tangkapan layar.
  - Diskusi penjelasan konsep perbedaan referensi objek shallow copy `{ ...profil }` vs referensi pointer `salinan = profil`.
  - Bantuan pengecekan sintaks safe navigation operator (`?.` dan `??`) agar sesuai standar modern ES6+.
- **Bagian yang dikerjakan sendiri**:
  - Konseptualisasi dan perancangan topik halaman profil (Daftar Film Favorit yang Pernah Ditonton).
  - Penulisan seluruh isi objek data profil dan daftar film (`Inception`, `The Shawshank Redemption`, `The Dark Knight`, `Interstellar`) beserta metadata tahun, sutradara, rating, dan sinopsis.
  - Implementasi fungsi murni `buatPerkenalan` dan `formatKeahlian`.
  - Pengujian manual eksekusi kode di peramban lokal dan verifikasi output tabel pada DevTools Console.
  - Perumusan refleksi pembelajaran dan catatan untuk pengampu pada Lembar F.


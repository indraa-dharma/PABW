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

---

## Pertemuan 9 — DOM, Event, dan Interaktivitas

Pertemuan ini berfokus pada integrasi data dinamis JavaScript ke antarmuka halaman HTML (DOM manipulation), penerapan pola perenderan berbasis data murni tanpa `innerHTML`, *event delegation* satu pendengar di induk, penanganan status kosong (*empty state*), serta validasi formulir interaktif di sisi klien tanpa memuat ulang halaman (*single-page interaction*).

### 1. Lembar A — Memilih Elemen di Halaman
- **Pembersihan HTML**: Menghapus seluruh elemen kartu film yang sebelumnya ditulis statis (hardcoded) di dalam `<section id="film">`.
- **Wadah Dinamis**: Menambahkan elemen penampung kosong:
  - `<div id="filter">`: Berisi tombol-tombol filter kategori (`semua`, `Action`, `Drama`, `Sci-Fi`, dan kategori uji kosong `Komedi`).
  - `<ul id="daftar" class="galeri grid"></ul>`: Wadah tempat perenderan kartu proyek/film dinamis.
  - `<p id="pesan-kosong" hidden>Tidak ada proyek pada kategori itu.</p>`: Paragraf notifikasi saat hasil filter tidak menemukan item yang cocok.
- **Pemisahan Modul**:
  - Berkas `js/dom.js` dibuat dan dipisahkan dari `js/app.js`.
  - Pada `js/app.js`, ditambahkan kata kunci `export` pada data profil dan daftar proyek (`export const daftarProyek = daftarFilm;`).
  - Pada `js/dom.js`, data diimpor menggunakan `import { daftarProyek } from "./app.js";`.
  - Kedua skrip dihubungkan berurutan sebelum penutup `</body>` dengan `type="module"`.
- **Uji Pemilih di Console**: Seluruh pemilih (`#daftar`, `#filter`, `#pesan-kosong`, formulir, dan kolom input) dipastikan menghasilkan elemen DOM valid (0 nilai `null`).

### 2. Lembar B — Menyusun Elemen dari Data
- **Pencegahan Celah XSS**: Pembuatan kartu dilakukan murni menggunakan API DOM standar: `document.createElement()`, `element.textContent`, dan `element.append()`. Penggunaan `innerHTML` dihindari sepenuhnya sehingga data input tidak dapat disusupi skrip asing.
- **Fungsi `buatKartu(proyek)`**: Membangun elemen kartu `<li class="kartu">` lengkap dengan judul (`.kartu__judul`), sinopsis, tahun & kategori (`.kartu__kaki`), dan sutradara (`.kartu__info`).
- **Pembersihan Wadah**: Fungsi render diawali dengan `wadah.textContent = ""` agar kartu tidak berlipat ganda setiap kali fungsi render dipanggil.
- **Verifikasi**: Sebanyak 4 kartu tampil tepat sesuai panjang array `daftarProyek`, dengan judul kartu pertama adalah "Inception".

### 3. Lembar C — Satu Pendengar untuk Semua Tombol (Event Delegation)
- **Satu Pendengar di Induk**: Menggunakan teknik *event delegation* dengan memasang satu `addEventListener("click")` pada container `#filter`, bukan memasang pendengar pada setiap tombol secara terpisah.
- **Deteksi Tombol & Pembacaan Dataset**:
  - Menggunakan `event.target.closest("button")` untuk mendeteksi tombol target meskipun bagian ikon/teks di dalamnya yang terkena klik.
  - Mengabaikan klik jika terjadi di ruang kosong di luar tombol (`if (!tombol) return;`).
  - Membaca target kategori secara deklaratif melalui `tombol.dataset.kategori`.
- **Penanda Tombol Aktif**:
  - Dibuat fungsi `tandaiTombolAktif(tombolAktif)` yang memanfaatkan `classList.toggle("aktif", tombol === tombolAktif)`.
  - Ditambahkan aturan CSS `.aktif { outline: 2px solid currentColor; outline-offset: 2px; }` pada `komponen.css` untuk visual indikator yang kontras dan aksesibel.
- **Penyaringan Reaktif**: Memanggil `render(terpilih)` di mana data disaring menggunakan `daftarProyek.filter(...)`.

### 4. Lembar D — Pola Render dan Validasi Form
- **Prinsip Tampilan adalah Fungsi dari Data**:
  - Logika perenderan dipusatkan dalam satu fungsi tunggal `render(daftar)`.
  - Tiga langkah berurutan: (1) Mengosongkan wadah (`wadah.textContent = ""`), (2) Memeriksa keadaan kosong (`if (daftar.length === 0) { kosong.hidden = false; return; }`), dan (3) Mengisi ulang wadah (`daftar.forEach(...)`).
- **Validasi Formulir Interaktif**:
  - `event.preventDefault()` dipanggil di baris paling awal penangan `submit` untuk mencegah muat ulang halaman.
  - Pembersihan spasi menggunakan `input.value.trim()`.
  - Validasi per kolom mencakup: Judul (tidak kosong), Tahun Rilis (angka valid antara 1800–2100), Sutradara (tidak kosong), dan Rating IMDb (angka 0–10).
  - Menandai kolom tidak sah secara semantik aksesibilitas dengan `setAttribute("aria-invalid", "true")`.
  - Tombol submit dinonaktifkan (`tombolSubmit.disabled = !semuaSah`) dan hanya aktif saat seluruh kolom valid.
  - Mengarahkan fokus otomatis menggunakan `kolom.focus()` pada kolom bermasalah pertama saat pengiriman.
  - Saat form berhasil dikirim, objek data film baru ditambahkan ke `daftarProyek`, daftar otomatis dirender ulang secara reaktif, dan formulir direset.

### 5. Lembar E — Membaca Gejala dan Penanganan Tiga Kasus Sulit
- **Kasus 1 (Pemilih Menghasilkan Null)**:
  - Gejala: Skrip berhenti dengan pesan `Cannot read properties of null`.
  - Solusi: Memeriksa ejaan id/kelas pada panel Elements DevTools dan memastikan berkas JavaScript dipanggil dengan `type="module"` tepat sebelum `</body>` sehingga seluruh pohon DOM telah selesai diurai peramban.
- **Kasus 2 (Pendengar Ganda)**:
  - Gejala: Satu klik menjalankan aksi berkali-kali atau kartu bertambah eksponensial.
  - Solusi: Memastikan `addEventListener` dipasang hanya sekali di induk di luar fungsi `render()`, bukan di dalam fungsi perenderan ulang.
- **Kasus 3 (Isi Daftar Kosong)**:
  - Gejala: Saat memfilter kategori tanpa data, tampilan terlihat seperti macet/rusak tanpa penjelasan.
  - Solusi: Menangani kondisi `daftar.length === 0` di dalam fungsi `render()` dengan mengaktifkan elemen pesan kosong (`kosong.hidden = false`).
- **Dokumentasi Tangkapan Layar**:
  - `screenshot_event_listeners.png`: Tampilan DevTools Elements dan panel Event Listeners yang membuktikan hanya ada 1 pendengar klik di induk `#filter`.
  - `screenshot_diperbaiki.png`: Tampilan antarmuka halaman normal dengan DevTools Console bersih tanpa pesan galat merah (0 galat, pemilih valid).
  - `screenshot_filter.png`: Tampilan antarmuka saat fitur filter kategori (misal: "Sci-Fi") aktif bekerja menyaring data film secara instan.

### 6. Lembar F — Tiket Keluar & Dokumen Word Terisi
- Seluruh 5 pertanyaan konsep Tiket Keluar dijawab secara tuntas dan mendalam.
- Matriks evaluasi mandiri terisi penuh (100/100) dilengkapi bukti lokasi berkas dan baris kode pendukung.
- Dokumen Word resmi dengan tata letak, gaya visual, font Carlito, dan palet warna identik PDF dibuat dan disimpan sebagai:
  `AMADEUS DHARMA AKBARINDRA - 25523253 - 9. Worksheet_PABW_Pertemuan9.docx`.

## Catatan Penggunaan AI (Pertemuan 9)

- **Bagian yang dibantu AI**:
  - Asistensi perancangan skrip generator Word (`build_p9_docx.py`) menggunakan `python-docx` untuk menyusun dokumen 19 halaman yang presisi secara tipografi, tata letak tabel, dan pewarnaan header/footer sesuai template PDF resmi PABW.
  - Otomasi pengujian fungsionalitas DOM dan penangkapan layar DevTools resolusi tinggi menggunakan skrip headless browser.
  - Pengecekan standar aksesibilitas pada atribut formulir (`aria-invalid`, `novalidate`, dan `role`).
- **Bagian yang dikerjakan sendiri**:
  - Penyesuaian struktur markup `<div id="filter">`, `<ul id="daftar">`, dan `<p id="pesan-kosong">` pada `profil.html`.
  - Perancangan kategori film (`Action`, `Drama`, `Sci-Fi`, `Komedi`) agar selaras dengan data film pribadi di `js/app.js`.
  - Penulisan logika `buatKartu`, pola fungsi tunggal `render`, dan teknik *event delegation* pada `js/dom.js`.
  - Implementasi validasi formulir client-side, pencegahan muat ulang via `preventDefault()`, serta manipulasi array `daftarProyek`.
  - Pengujian interaktif seluruh fitur (filter, status tombol, reset form, pesan kosong) di browser lokal.
  - Perumusan refleksi dan analisis mendalam pada lembar evaluasi dan Tiket Keluar.

---

## Pertemuan 10 — JavaScript Asinkron: fetch, Promise, dan JSON

Pertemuan ini berfokus pada integrasi data asinkron dari API eksternal menggunakan `fetch` API, penanganan `Promise` modern dengan sintaks `async/await`, penguraian badan balasan JSON dua arah (`json()` dan `stringify()`), pemisahan ketat antara lapisan data (`js/api.js`) dan lapisan antarmuka (`js/dom.js` & `js/app.js`), serta implementasi lengkap empat keadaan antarmuka (*loading*, *success*, *error*, dan *empty state*).

### 1. Lembar A — Panggilan Pertama dan Status Balasan
- **Pemeriksaan Berkas Awal (A.1)**:
  - Seluruh berkas dari pertemuan sebelumnya dipastikan lengkap di `worksheet-p10/`: `profil.html` (209 baris), 6 berkas CSS (543 baris), `js/app.js` (215 baris), dan `js/dom.js` (315 baris).
- **Alamat Tunggal (A.2)**:
  - Dibuat berkas baru `js/api.js`.
  - Alamat API dideklarasikan satu kali saja di baris paling atas: `const ALAMAT = "https://ghibliapi.vercel.app/films";`.
  - Memenuhi seluruh kriteria: skema `https`, tanpa token/kunci akses rahasia di kode sumber, dan terpusat di `js/api.js`.
  - Disediakan berkas lokal `film.json` sebagai alternatif luring jika jaringan laboratorium kampus terbatas.
- **Pemeriksaan `respons.ok` (A.3)**:
  - Pemanggilan `fetch(ALAMAT)` diperiksa terlebih dahulu dengan `if (!respons.ok) throw new Error('status ' + respons.status)`.
  - Hasil panggilan pada panel Network DevTools:
    - Alamat: `https://ghibliapi.vercel.app/films`
    - Status balasan: `200 OK`
    - Nilai `respons.ok`: `true`
    - Jenis isi (*Content-Type*): `application/json; charset=utf-8`

### 2. Lembar B — async, await, dan Penanganan Galat
- **Satu try/catch Menutup Seluruh Rantai (B.1)**:
  - Fungsi `export async function ambilFilm()` ditulis secara mendatar menggunakan `async/await`.
  - Seluruh langkah dibungkus blok `try/catch`. Pada blok `catch`, galat dicatat (`console.error`) dan dilempar kembali (`throw galat`) agar lapisan pemanggil dapat menampilkannya di halaman.
- **Penanganan Tiga Kegagalan (B.2)**:
  1. *Jaringan mati / alamat salah*: Promise ditolak -> ditangkap blok `catch`, pesan galat ditampilkan ke halaman.
  2. *Status 404 / 500*: Promise tetap dianggap berhasil oleh fetch -> ditangani dengan pemeriksaan `respons.ok`, lalu melempar galat sendiri.
  3. *Badan bukan JSON*: `respons.json()` menolak -> ditangkap blok `catch` pemanggil.
  4. *Balasan sah tanpa butir*: Promise berhasil dengan larik kosong `[]` -> ditangani dengan memeriksa `daftar.length === 0` untuk menampilkan keadaan kosong.
- **Uji Penangkapan Galat (B.3)**:
  - Alamat diubah ke URL tidak ada (`404`): pesan galat *"Gagal memuat data: status 404"* tampil di wadah `#daftar`.
  - Jaringan dimatikan (*Offline* di panel Network): pesan galat *"Gagal memuat data: Failed to fetch"* tampil di halaman.
  - Alamat dikembalikan semula: daftar kartu film kembali tampil normal secara otomatis.

### 3. Lembar C — Membaca JSON Dua Arah
- **Arah Nilai dan Teks (C.1)**:
  - `respons.json()`: teks respons jaringan -> objek/larik JavaScript (membaca data peladen).
  - `JSON.parse(teks)`: teks JSON string -> nilai JavaScript (membaca berkas lokal atau localStorage).
  - `JSON.stringify(nilai)`: nilai JavaScript -> teks JSON (mengirim payload ke peladen atau menyimpan ke localStorage).
- **Peta Struktur Data API (C.2)**:
  - Objek: satu entitas film `{ id, title, director, release_date, rt_score, description }` diakses melalui `data[0]`.
  - Larik: kumpulan data film `[ {...}, {...} ]` diakses melalui `data.forEach(film => ...)`.
  - Teks atau angka: `film.title`, `film.release_date`, `film.rt_score` diakses melalui `film.title`.
  - Benar/salah atau null: status ketersediaan atau properti validasi diakses via `Boolean(film.id)` atau `film.selesai`.

### 4. Lembar D — Menampilkan Data ke Halaman & Batas Lapisan
- **Pemisahan Lapisan**:
  - `js/api.js`: Hanya bertugas mengambil data via `fetch`, memeriksa status, dan mengekspor fungsi `ambilFilm`.
  - `js/app.js` & `js/dom.js`: Bertugas sebagai pemanggil data dan penyusun tampilan DOM. Tidak ada kata kunci `fetch` di dalam berkas ini.
- **Empat Keadaan Antarmuka (D.2)**:
  1. *Memuat*: Menampilkan teks `"Memuat data film dari API..."` pada elemen `#daftar` sebelum data diterima.
  2. *Berhasil*: Menghapus teks pembuat (`wadah.textContent = ""`), lalu membuat elemen `<li class="kartu">` via `createElement` dan `textContent`.
  3. *Gagal*: Menampilkan teks `"Gagal memuat data: " + galat.message` pada antarmuka saat penolakan terjadi.
  4. *Kosong*: Menampilkan pesan `"Belum ada film yang tersedia."` saat array berukuran 0.
- **Keamanan XSS**: Semua data teks dari jaringan dimasukkan menggunakan `element.textContent`, tanpa `innerHTML`.

### 5. Lembar E — Tiga Kasus Sulit
- **E.1 Status 404 Tidak Melempar Galat**: Ditutup dengan pemeriksaan eksplisit `if (!respons.ok) throw new Error(...)`.
- **E.2 await di Luar Fungsi async**: Seluruh pemanggilan `await` diisolasi di dalam fungsi `async function tampilkan()` dan `async function inisialisasiDataAPI()`.
- **E.3 Balasan Sah Tanpa Butir**: Ditangani secara eksplisit pada percabangan `if (daftarFilmAktif.length === 0)` sebelum pemanggilan fungsi render.

### 6. Lembar F — Bukti Tangkapan Layar & Tiket Keluar
- Seluruh 10 butir daftar periksa mandiri (F.1) berstatus **Lolos (Centang)**.
- Tiga bukti tangkapan layar antarmuka resolusi tinggi:
  - `screenshot_berhasil.png`: Keadaan Berhasil (kartu film tampil rapi dari API, 0 galat di DevTools).
  - `screenshot_gagal.png`: Keadaan Gagal (pesan galat status 404 tampil di halaman).
  - `screenshot_memuat_kosong.png`: Keadaan Memuat dan Keadaan Kosong (pesan informatif tanpa layar putih).
- Evaluasi mandiri bernilai 100/100 dengan rujukan berkas dan baris kode lengkap.
- Dokumen Word resmi terisi lengkap sesuai format dan layout PDF disimpan sebagai:
  `AMADEUS DHARMA AKBARINDRA - 25523253 - 10. Worksheet_PABW_Pertemuan10.docx`.

## Catatan Penggunaan AI (Pertemuan 10)

- **Bagian yang dibantu AI**:
  - Perancangan skrip generator Word (`build_p10_docx.py`) berbasis `python-docx` untuk menghasilkan dokumen 13 halaman dengan layout, margin A4, tipografi Carlito, dan pewarnaan tabel yang identik dengan lembar kerja PDF resmi P10.
  - Otomasi pengujian status peramban melalui instrumen Chrome DevTools (pengujian HTTP 200, simulasi status 404, dan pengambilan tangkapan layar resolusi 1920x806).
  - Verifikasi ketat pemisahan lapisan arsitektur data (*separation of concerns*) antara `api.js` dan antarmuka.
- **Bagian yang dikerjakan sendiri**:
  - Pemilihan topik halaman profil pribadi (*Daftar Film yang Pernah Saya Tonton*) dan pemilihan endpoint API publik HTTPS Studio Ghibli serta pembuatan dataset lokal `film.json`.
  - Penulisan fungsi `ambilFilm()` dengan pemeriksaan `respons.ok` dan pelemparan galat di `js/api.js`.
  - Integrasi penanganan 4 keadaan antarmuka (*loading*, *success*, *error*, *empty*) murni berbasis DOM API di `js/dom.js`.
  - Pemanggilan lapisan data pada pemanggil sekunder dengan blok `try/catch` di `js/app.js`.
  - Pengujian manual interaksi filter kategori, formulir penambahan film baru, dan pengetikan fungsi konsol `gambar([])`.
  - Perumusan refleksi dan jawaban analitis untuk lembar Tiket Keluar dan catatan untuk pengampu.

---

## Pertemuan 11 — Modul, State, dan Penyimpanan Klien

Pertemuan ini berfokus pada dekomposisi berkas JavaScript menjadi lima modul independen dengan prinsip *single responsibility*, pemisahan tegas keadaan aplikasi (*state*) dari antarmuka (*DOM*), penerapan pola perenderan reaktif murni `render(state)`, penyimpanan pilihan pengguna di peramban menggunakan `localStorage` dan serialisasi JSON, serta pertahanan sistem terhadap simpanan rusak dan ketidakcocokan skema (*schema versioning*).

### 1. Lembar A — Memeriksa Berkas dan Menggambar Susunan Modul
- **Pemeriksaan Berkas Awal (A.1)**:
  - `profil.html` (209 baris).
  - 6 berkas CSS: `tokens.css`, `base.css`, `layout.css`, `komponen.css`, `tema.css`, `responsif.css` (464 baris).
  - `js/app.js` (216 baris) dan `js/dom.js` (316 baris).
- **Berkas Tambahan Pertemuan 10 (A.2)**:
  - Berkas `js/api.js` dari Pertemuan 10 dipertahankan fungsinya sebagai lapisan data masuk tanpa menulis ke DOM, diimpor ke `app.js` tanpa bentrok.
- **Penghitungan Sentuhan ke Halaman (A.3)**:
  - `js/app.js`: 3 baris menyentuh halaman (pengecekan formulir).
  - `js/dom.js`: 48 baris menyentuh halaman (pemilih elemen, manipulasi DOM, render, event delegation, validasi form).
- **Rencana Dekomposisi 5 Modul (A.4)**:
  1. `js/data.js`: Data mentah (`profil`, `daftarFilm`/`daftarProyek`) dan fungsi murni pemformat (`buatPerkenalan`, `formatKeahlian`, `formatTanggal`).
  2. `js/state.js`: Objek state tunggal (`state`), persistensi (`simpan`, `muat`, `aturUlang`), dan fungsi pengubah state (`pilihKategori`, `tambahFilm`, `aturUlangPilihan`).
  3. `js/dom.js`: Seluruh sentuhan ke halaman (pemilih elemen, `buatKartu`, `saring(state)`, `tandaiTombolAktif`, `render(state)`, validasi form).
  4. `js/events.js`: Pemasangan seluruh pendengar peristiwa (`pasangPendengar`: event delegation filter, tombol reset, submit form, validasi live).
  5. `js/app.js`: Perakit (*assembler*) yang mengimpor seluruh modul, membaca simpanan awal, menginisialisasi listener, dan memicu render pertama.

### 2. Lembar B — Memecah Berkas dan Menyambungkannya Kembali
- **Aturan Impor ES Modules (B.1)**:
  - Seluruh jalur impor relatif wajib diawali `./` dan berakhiran `.js` (contoh: `import { state } from './state.js';`).
  - Menggunakan *named exports* secara eksplisit untuk menjaga keterbacaan kode.
- **Penyederhanaan `profil.html` (B.2)**:
  - Tag skrip ganda dari P9 disederhanakan menjadi satu baris modul tunggal:
    ```html
    <script type="module" src="js/app.js"></script>
    ```
- **Hasil Pemecahan (B.5)**:
  - DevTools Console: Bersih tanpa galat merah maupun peringatan kuning (0 *import error*, 0 *syntax error*).
  - Perilaku Halaman: Berjalan normal persis seperti akhir P9; seluruh filter, validasi form, dan rendering dinamis tetap utuh.
  - Tanggung Jawab Modul: `app.js` murni menjadi perakit tanpa logika DOM.

### 3. Lembar C — Memindahkan Keadaan Keluar dari Halaman
- **Prinsip Tampilan adalah Fungsi dari Keadaan (C.1 & C.2)**:
  - Keadaan aktif filter tidak lagi disimpan di DOM (seperti kelas CSS `.aktif` pada tombol), melainkan murni bersumber dari `state.kategoriAktif`.
  - Fungsi perenderan diubah menjadi `render(state)` dengan tiga urutan kerja mutlak:
    1. Mengosongkan wadah (`wadah.textContent = ""`).
    2. Memeriksa keadaan kosong (`const tampil = saring(state); if (tampil.length === 0) { kosong.hidden = false; ... return; }`).
    3. Mengisi ulang elemen kartu dari state (`tampil.forEach(...)`).
- **Satu Pintu Masuk Perubahan (C.3)**:
  - Tidak ada penulisan state langsung di `events.js`. Setiap mutasi keadaan dilakukan melalui fungsi pengubah bernama di `state.js` (`pilihKategori`, `tambahFilm`, `aturUlangPilihan`) yang secara otomatis memicu pembaruan persistensi dan pemanggilan `render(state)`.
  - Uji deterministik: Memanggil `render(state)` berulang kali tidak menyebabkan kartu berlipat atau state hilang.

### 4. Lembar D — Halaman yang Mengingat Pilihan
- **Penyimpanan Klien dengan `localStorage` (D.1)**:
  - Objek status diserialisasi menjadi teks JSON menggunakan `JSON.stringify(isi)` sebelum disimpan dengan `localStorage.setItem(KUNCI, ...)`.
  - Saat dibaca, teks diurai kembali menjadi objek menggunakan `JSON.parse(localStorage.getItem(KUNCI))`.
- **Nilai Bawaan & Tombol Atur Ulang (D.2)**:
  - Pada kunjungan pertama (saat `getItem` bernilai `null`), nilai bawaan diterapkan secara aman (`kategoriAktif: "semua"`).
  - Ditambahkan tombol antarmuka `<button type="button" id="tombol-reset" class="tombol-reset">Atur Ulang Pilihan</button>` pada `profil.html` untuk menghapus simpanan (`localStorage.removeItem(KUNCI)`) dan mengembalikan tampilan ke default.
- **Pilihan Data Disimpan vs Dikecualikan (D.4)**:
  - Disimpan: `kategoriAktif` (preferensi filter pengguna agar tetap bertahan saat berpindah tab atau memuat ulang halaman).
  - Sengaja Tidak Disimpan: Kata kunci pencarian sementara, input draf formulir yang belum disubmit, serta token otentikasi/data pribadi (mencegah risiko keamanan XSS dan pembengkakan kuota penyimpanan).

### 5. Lembar E — Simpanan Rusak dan Jalan Pulangnya
- **Pertahanan Simpanan Korup (E.1 & E.2)**:
  - Fungsi `muat()` dibungkus dalam blok `try/catch`. Jika isi simpanan bukan JSON yang sah, blok `catch` otomatis membuang kunci korup dengan `localStorage.removeItem(KUNCI)` dan mengembalikan `null`.
  - Diterapkan nomor versi skema `const VERSI = 2`. Jika data memiliki skema lama (`isi?.versi !== VERSI`), simpanan lama dibuang dan nilai bawaan digunakan.
- **Hasil Pengujian Kerusakan Mandiri (E.3)**:
  - Uji string korup `localStorage.setItem("pabw-p11", "bukan-json")`: Tertangkap blok `catch`, simpanan dibuang, halaman tetap terbuka normal dengan nilai bawaan.
  - Uji skema tidak cocok `localStorage.setItem("pabw-p11", "{}")`: Terdeteksi versi usang, simpanan lama dihapus, nilai bawaan terpasang.
  - Evaluasi `window.muat()`: Mengembalikan `null` dengan aman tanpa menghentikan eksekusi skrip peramban.
- **Dokumentasi Tangkapan Layar**:
  - `screenshot_simpanan_rusak.png`: Pengujian simpanan rusak dan versi lama di DevTools Console beserta penanganannya.
  - `screenshot_pulih_bawaan.png`: Tampilan antarmuka yang pulih sempurna dengan nilai bawaan dan DevTools Console bersih tanpa galat.

### 6. Lembar F — Tiket Keluar, PR Node.js, dan Evaluasi Mandiri
- **Pekerjaan Rumah Sebelum Pertemuan 12 (F.2)**:
  - Versi Node.js: `node -v` -> `v26.3.0` (LTS siap pakai).
  - Versi npm: `npm -v` -> `11.16.0`.
  - Status: Berhasil terpasang dan dikenali secara global di terminal.
- **Satu Baris untuk Diingat (F.3)**:
  > *"Tampilan hanyalah cerminan dari objek state; jangan pernah mengubah elemen DOM secara manual atau membaca keadaan kembali dari antarmuka halaman."*
- **Penilaian Mandiri (F.4)**:
  - Nilai Mandiri: **100 / 100** (Pemecahan modul: 25, Pemisahan state: 25, LocalStorage: 25, Penanganan simpanan rusak: 15, Kebersihan kode & deklarasi AI: 10).
- **Dokumen Worksheet Word**:
  - Dokumen Word resmi terisi lengkap 100% presisi identik dengan template PDF PABW disimpan sebagai:
    `AMADEUS DHARMA AKBARINDRA - 25523253 - 11. Worksheet_PABW_Pertemuan11 - ID.docx`.

## Catatan Penggunaan AI (Pertemuan 11)

- **Bagian yang dibantu AI**:
  - Asistensi perancangan skrip pengisian dokumen Word otomatis (`fill_p11_docx.py`) berbasis `python-docx` untuk mengisi seluruh tabel, pertanyaan tiket keluar, checkbox status, dan evaluasi mandiri pada template resmi dosen.
  - Otomasi pengujian instrumen peramban melalui Chrome DevTools Protocol (CDP) untuk simulasi persistensi `localStorage`, pengujian string rusak, dan penangkapan layar resolusi tinggi 1920x806 (`screenshot_simpanan_rusak.png` dan `screenshot_pulih_bawaan.png`).
  - Verifikasi diagram alur ketergantungan modul (*Directed Acyclic Graph*) agar terhindar dari *circular dependency* antara `state.js`, `dom.js`, dan `events.js`.
- **Bagian yang dikerjakan sendiri**:
  - Perancangan arsitektur pemisahan 5 modul JavaScript (`data.js`, `state.js`, `dom.js`, `events.js`, `app.js`).
  - Pemindahan data profil, daftar film pribadi, dan fungsi-fungsi murni pemformat ke `js/data.js`.
  - Implementasi fungsi render murni `render(state)`, fungsi penyaring `saring(state)`, dan penanda visual tombol aktif di `js/dom.js`.
  - Penulisan logika pengubah keadaan tunggal, serialisasi JSON, dan validasi versi skema di `js/state.js`.
  - Penyusunan integrasi penangan peristiwa *event delegation* dan validasi formulir di `js/events.js`.
  - Perakitan alur inisialisasi aplikasi pada `js/app.js` dan penyesuaian markup `<script type="module">` serta tombol reset di `profil.html`.
  - Pengujian manual pada browser lokal (Chrome/Edge) untuk memastikan tab dapat ditutup dan dibuka kembali dengan pilihan filter yang tetap diingat.
  - Perumusan refleksi pembelajaran dan jawaban tiket keluar secara analitis dan mendalam.





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

---

## Pertemuan 12 — Build Tooling, npm, dan Framework SPA: Dari Berkas Lepas ke Proyek Komponen yang Dibangun

- **Nama**: Amadeus Dharma Akbarindra
- **NIM**: 25523253
- **Kelas**: SIF302 / B
- **Topik Proyek**: Daftar Film yang Pernah Saya Tonton

---

### 1. Lembar A — Memeriksa Perkakas Sebelum Bekerja
- **Hasil Pemeriksaan Perkakas Terminal (A.1)**:
  - `node -v` : `v26.3.0` (memenuhi syarat minimum Node.js LTS 20.19+ / 22.12+)
  - `npm -v` : `11.16.0`
- **Pemeriksaan Berkas Aset Pertemuan 11 (A.2)**:
  - `profil.html` : Ada (lengkap dengan kerangka halaman dan elemen DOM semantik).
  - Enam berkas CSS (P04–P06) : Lengkap (`tokens.css`, `base.css`, `layout.css`, `komponen.css`, `tema.css`, `responsif.css`).
  - Lapisan data & modul JS : Lengkap (`data.js`, `api.js`, `state.js`, `events.js`, `app.js`, `dom.js`).
  - Berkas JSON & Gambar : `film.json` dan `images (3).jpg`.
- **Pemeriksaan Folder Kerja (A.3)**:
  - Folder `worksheet-p12/` disiapkan sebagai repositori komponen mandiri.
  - Status Git bersih sebelum migrasi dimulai.

---

### 2. Lembar B — Membuat Proyek Baru di Folder Baru
- **Inisialisasi Kerangka Proyek (B.1)**:
  - Inisialisasi Vite + Vue 3 menggunakan template resmi:
    `npm create vite@latest . -- --template vue`
  - Dependensi dipasang menggunakan `npm install`.
- **Konfigurasi `.gitignore` Sebelum Komit Pertama (B.4)**:
  - Folder `node_modules/` dan `dist/` sengaja diabaikan agar tidak mengotori repositori dengan puluhan ribu berkas biner/artefak sementara.
  - Berkas `package.json` dan `package-lock.json` wajib disimpan dan di-commit untuk mengunci versi dependensi secara deterministik.
- **Hasil Verifikasi `npm run dev` Awal (B.5)**:
  - Server pengembangan Vite berjalan normal pada port lokal (`http://localhost:5173/`).
  - Console browser bersih tanpa pesan kesalahan.

---

### 3. Lembar C — Memindahkan Aset Pertemuan 11
- **Aturan Pemindahan Tanpa Mengubah Perilaku (C.1 & C.2)**:
  - Seluruh 6 berkas CSS asli dipindahkan ke dalam direktori `src/` tanpa mengubah satu baris pun nilai token maupun aturan gayanya.
  - Berkas CSS diimpor secara terpusat pada `src/main.js` dengan urutan persis:
    1. `./tokens.css`
    2. `./base.css`
    3. `./layout.css`
    4. `./komponen.css`
    5. `./tema.css`
    6. `./responsif.css`
  - Berkas `profil.html` lama disederhanakan menjadi `index.html` tunggal di akar proyek yang hanya memuat `<div id="app"></div>` dan `<script type="module" src="/src/main.js"></script>`.
  - Berkas statis (`film.json` dan gambar poster) ditempatkan di direktori `public/`.
  - Berkas contoh bawaan Vite (`HelloWorld.vue`) dihapus seluruhnya.
  - Berkas `src/data.js` dan `src/api.js` dipindahkan dengan isi tetap utuh; setiap butir pada data telah dilengkapi atribut `id` unik.

---

### 4. Lembar D — Memecah Halaman Menjadi Empat Komponen
Halaman dipecah secara modular menjadi 4 Single File Component (SFC) di dalam `src/components/`:

1. **`KepalaProfil.vue`**:
   - Menampilkan bagian identitas atas halaman (header, brand nama & peran, tombol pengalih tema gelap berbasis CSS murni, dan navigasi utama).
   - Menerima data secara deklaratif dari induk (`App.vue`) melalui `props`:
     ```vue
     <script setup>
     const props = defineProps({
       profil: { type: Object, required: true },
     })
     </script>
     ```
   - Sifat props strictly *read-only* (hanya dibaca oleh komponen anak).

2. **`TombolFilter.vue`**:
   - Menampilkan deretan tombol kategori filter (`Semua`, `Action`, `Drama`, `Sci-Fi`, `Komedi`) serta tombol `Atur Ulang Pilihan`.
   - Menggunakan state bersama dari `state.js`.
   - Menandai tombol aktif secara reaktif menggunakan pengikatan kelas `:class="{ aktif: state.kategoriAktif === kategori }"`.
   - Pemicu perubahan filter memanggil fungsi `pilihKategori(kategori)` tanpa sentuhan manual ke DOM.

3. **`DaftarProyek.vue`**:
   - Menampilkan kartu-kartu proyek/film menggunakan direktif `v-for="proyek in daftarTersaring" :key="proyek.id"`.
   - Penyaringan kategori ditangani secara reaktif menggunakan `computed()` berbasis `state.kategoriAktif`.
   - Menampilkan status kosong `#pesan-kosong` secara bersyarat via `v-else` ketika tidak ada kartu yang cocok.
   - Struktur elemen HTML dan penamaan kelas (`kartu`, `kartu__judul`, `kartu__kaki`, `kartu__info`) 100% identik dengan P11.

4. **`FormKontak.vue`**:
   - Menampilkan formulir penambahan film baru (`Tambah List Film`).
   - Bidang input diikat secara dua arah (*two-way binding*) menggunakan `v-model` ke variabel `ref` lokal (`judul`, `tahun`, `sutradara`, `rating`).
   - Penanganan pengiriman formulir menggunakan `@submit.prevent="handleSubmit"`.
   - Mengosongkan isian formulir setelah data berhasil ditambahkan ke state tanpa memicu muat ulang (*page refresh*).

---

### 5. Lembar E — Menyambungkan Keadaan Reaktif dan Penyimpanan
- **Transformasi State Imperatif ke State Reaktif (E.1)**:
  - Di `src/state.js`, objek keadaan dibungkus menggunakan `reactive()`:
    ```javascript
    export const state = reactive({
      daftarProyek: [...daftarProyek],
      kategoriAktif: 'semua',
    })
    ```
  - Fungsi `pilihKategori(nilai)` hanya memperbarui properti `state.kategoriAktif`. Tidak ada lagi fungsi `render(state)` manual; sistem reaktivitas Vue otomatis mendeteksi perubahan dan memperbarui tampilan virtual DOM secara instan.
- **Integrasi `localStorage` Klien (E.2)**:
  - Logika penyimpanan dipisahkan bersih pada `src/simpanan.js` menggunakan kunci `"pabw-p11"` dan skema versi `VERSI = 2`.
  - Pada `src/App.vue`:
    - `onMounted()`: Membaca simpanan dari `localStorage` satu kali saat komponen pertama kali dipasang ke DOM.
    - `watch(state, (nilai) => simpan(nilai), { deep: true })`: Mengawasi setiap perubahan state secara mendalam dan otomatis memperbarui `localStorage`.
    - `aturUlangPilihan()`: Menghapus simpanan dan mengembalikan kategori aktif ke `'semua'`.
- **Hasil Pengujian Ketahanan Simpanan (E.4)**:
  - Simpanan korup via `localStorage.setItem('pabw-p11', 'bukan-json')` ditangkap secara aman oleh blok `try/catch` pada fungsi `muat()`, simpanan rusak langsung dibuang, dan sistem kembali ke nilai bawaan tanpa galat.
  - Nilai filter aktif bertahan sempurna saat tab ditutup dan dibuka kembali.

---

### 6. Lembar F — Membangun dan Mencoba Hasil Build
- **Dua Perintah Utama Produksi (F.1)**:
  - `npm run build`: Mengompilasi kode sumber, menggabungkan modul, dan memperkecil berkas (*minify & tree-shaking*) ke folder `dist/`.
  - `npm run preview`: Menjalankan server lokal statis untuk menguji langsung hasil folder `dist/` sebelum rilis.
- **Verifikasi Hasil Build (F.2)**:
  - Folder `dist/` berhasil terbentuk sempurna.
  - `dist/index.html` ada dan bersih.
  - `dist/assets/` memuat bundel JavaScript (`index-DgvRWNVC.js`) dan CSS (`index-6Nsuwklj.css`) dengan penamaan hash acak untuk *cache-busting*.
  - Halaman berjalan lancar dan interaktif lewat `npm run preview`.
- **Perbandingan Ukuran Berkas Sebelum & Sesudah Build (F.3)**:

| Parameter Pengukuran | Sebelum Build (Mode Dev / Sumber) | Sesudah Build (Hasil `dist/` Produksi) |
| :--- | :--- | :--- |
| **Jumlah Berkas yang Dikirim** | 25+ berkas terpisah (HTML, 6 CSS, Vue SFC modules, runtime scripts) | **3 berkas utama** (`index.html`, 1 bundel JS, 1 bundel CSS) |
| **Ukuran Berkas HTML** | ~3.5 kB (mentah) | **0.44 kB** (gzip: 0.30 kB) |
| **Ukuran Berkas CSS** | ~14.8 kB (tersebar di 6 berkas) | **7.77 kB** (gzip: 1.99 kB) |
| **Ukuran Berkas JS / Runtime** | Terpecah-pecah di puluhan modul pengembang | **75.58 kB** (gzip: 29.90 kB) |
| **Efisiensi Jaringan** | Banyak HTTP roundtrips untuk impor modul | **1 bundel terpadu ter-minify**, loading jauh lebih instan |

- **Penanganan Kasus Sulit (F.4)**:
  1. *Nama berkas besar-kecil*: Penamaan berkas komponen disamakan konsisten persis (*PascalCase*: `KepalaProfil.vue`, `TombolFilter.vue`, `DaftarProyek.vue`, `FormKontak.vue`) untuk menjamin kompatibilitas di Windows, Linux, maupun CI/CD.
  2. *Folder `dist/`*: Dikecualikan sejak awal di `.gitignore` agar tidak masuk ke riwayat komit Git.
  3. *Aset statis*: Disimpan di direktori `public/` agar terbaca langsung di lingkungan dev maupun dist tanpa jalur impor yang rusak.
  4. *Jalur folder lokal Windows*: Adanya karakter `#` pada nama folder Windows diselesaikan secara aman menggunakan mapping virtual drive (`subst V:`) dan opsi `resolve.preserveSymlinks: true` pada `vite.config.js`.

---

### 7. Lembar G — Tiket Keluar dan Penilaian Mandiri

#### Jawaban Tiket Keluar (Halaman 18):

1. **Apa bedanya dependencies dan devDependencies? Sebutkan satu contoh untuk masing-masing dari proyek Anda.**
   - **Jawaban**:
     - `dependencies` adalah daftar paket pustaka yang mutlak diperlukan oleh aplikasi saat berjalan di lingkungan produksi (*runtime*). Tanpa paket ini, aplikasi web tidak akan berfungsi bagi pengguna. Contoh di proyek ini: **`vue`** (`^3.5.13`), karena modul reaktivitas dan komponen Vue harus ada saat peramban menjalankan aplikasi.
     - `devDependencies` adalah daftar perkakas yang hanya digunakan oleh pengembang selama tahap perancangan, pengujian, dan kompilasi (*build-time*). Paket-paket ini tidak dikirimkan ke pengguna akhir di produksi. Contoh di proyek ini: **`vite`** (`^6.0.7`) dan **`@vitejs/plugin-vue`** (`^5.2.1`), yang bertugas mengompilasi berkas SFC `.vue` menjadi berkas JavaScript dan CSS statis.

2. **Mengapa package-lock.json wajib disimpan di repositori, sedangkan node_modules/ tidak?**
   - **Jawaban**:
     - `node_modules/` berisi ribuan hingga puluhan ribu berkas fisik paket yang ukurannya sangat besar (ratusan MB). Menyimpannya di Git akan membuat repositori sangat lambat, boros penyimpanan, dan rawan konflik berkas. Folder ini tidak perlu disimpan karena dapat direkonstruksi kapan saja dengan perintah `npm install`.
     - `package-lock.json` wajib disimpan karena bertindak sebagai manifest deterministik yang mencatat secara presisi versi pasti (*exact version*), pohon sub-dependensi, serta *integrity hash* dari setiap paket yang terpasang. Hal ini menjamin bahwa setiap mesin atau rekan pengembang yang mengkloning proyek akan mengunduh versi dependensi yang sama persis 100%, mencegah masalah ketidakcocokan versi (*"it works on my machine"*).

3. **Apa yang dilakukan perintah `npm create vite@latest . -- --template vue`? Apa arti titik pada perintah itu?**
   - **Jawaban**:
     - Perintah tersebut mengunduh dan mengeksekusi alat pembuatan kerangka (*scaffolding*) Vite versi terbaru untuk membuat proyek Single Page Application berbasis framework Vue 3.
     - Tanda titik (`.`) berarti *membuat proyek di direktori kerja saat ini* (current directory), bukan membuat subdirektori baru di dalamnya.
     - Tanda pemisah argumen ganda (`--`) digunakan oleh npm untuk meneruskan argumen setelahnya (`--template vue`) langsung ke perkakas Vite tanpa diinterpretasikan oleh npm itu sendiri.

4. **Di Pertemuan 11 Anda memanggil render(state) sendiri. Apa yang menggantikannya di Vue, dan siapa yang memanggilnya sekarang?**
   - **Jawaban**:
     - Di Pertemuan 11, kita harus menulis dan memanggil fungsi imperatif `render(state)` secara manual setiap kali state dimutasi untuk merombak elemen DOM.
     - Di Vue, fungsi `render()` manual digantikan oleh **blok `<template>` deklaratif** yang terhubung secara otomatis ke data reaktif.
     - Yang memanggil pembaruan tampilan sekarang adalah **sistem reaktivitas bawaan Vue (*Reactivity Engine & Virtual DOM*)**. Ketika nilai properti pada objek `reactive()` atau `ref()` berubah, Vue secara otomatis mendeteksi mutasi tersebut dan menjadwalkan proses *re-render* yang efisien ke elemen DOM yang relevan tanpa campur tangan manual kita.

5. **Mengapa props tidak boleh diubah dari dalam komponen anak?**
   - **Jawaban**:
     - Karena framework modern menerapkan prinsip **One-Way Data Flow (Aliran Data Satu Arah)**. Props diturunkan dari komponen induk ke komponen anak sebagai data masukan *read-only*.
     - Jika komponen anak diperbolehkan memutasi props secara langsung, sumber kebenaran data (*single source of truth*) menjadi kacau, status komponen induk menjadi tidak sinkron, dan alur pelacakan bug (*debugging*) menjadi sangat sulit diprediksi (*unpredictable side-effects*). Jika anak ingin mengubah data, ia harus mengirim sinyal (*emit event*) ke induk agar induk yang memperbarui datanya sendiri.

6. **Apa bedanya npm run dev dan npm run preview? Kapan Anda memakai masing-masing?**
   - **Jawaban**:
     - `npm run dev`: Menjalankan server pengembangan (*Vite Dev Server*) yang menyajikan kode sumber asli dengan memanfaatkan modul ES asli peramban (*unbundled*) dan fitur *Hot Module Replacement* (HMR). Digunakan **selama proses pengodean/pengembangan sehari-hari** karena perubahannya langsung terlihat tanpa perlu waktu build.
     - `npm run preview`: Menjalankan server lokal statis untuk menyajikan berkas hasil kompilasi dan optimasi produksi yang berada di dalam folder `dist/`. Digunakan **setelah proses pengerjaan selesai** guna memverifikasi bahwa hasil kompilasi produksi bekerja persis seperti yang diharapkan sebelum dideploy ke server web publik.

7. **Mengapa dist/ diabaikan sedangkan hasilnya justru yang dijalankan peramban di produksi?**
   - **Jawaban**:
     - Folder `dist/` adalah berkas turunan hasil kompilasi otomatis (*build artifact*), bukan kode sumber asli (*source code*).
     - Berkas di dalam `dist/` ter-minifikasi dan memiliki hash acak pada nama berkasnya setiap kali dibuild. Jika dimasukkan ke Git, riwayat komit akan dipenuhi perubahan berkas biner yang tidak dapat dibaca manusia (*unreadable diffs*) dan ukuran repositori akan membengkak secara tidak perlu.
     - Dalam praktik industri modern (CI/CD pipeline), server produksi akan secara otomatis menarik kode sumber asli dari Git, lalu menjalankan perintah `npm install` dan `npm run build` langsung di server untuk menghasilkan `dist/` yang segar dan bersih.

---

#### G.1 Pemeriksaan Satu per Satu (Checklist)
- [x] Perkakas `node -v` (`v26.3.0`) dan `npm -v` (`11.16.0`) menjawab; versinya tercatat di README.
- [x] Proyek `worksheet-p12/` dibuat dari folder terstruktur; `npm run dev` membuka halaman tanpa galat.
- [x] Pemindahan halaman tampil sama persis seperti P11; token dan CSS P04–P06 tidak diubah.
- [x] Komponen empat komponen tersusun (`KepalaProfil.vue`, `TombolFilter.vue`, `DaftarProyek.vue`, `FormKontak.vue`); `KepalaProfil` menerima props profil; nama berkas dan impor ditulis sama konsisten.
- [x] Keadaan state memakai `reactive()`; tidak ada `render(state)` manual lagi.
- [x] Simpanan `onMounted` memuat dan `watch` menyimpan; pilihan terakhir bertahan setelah tab ditutup; tombol atur ulang mengembalikan nilai bawaan.
- [x] Build `npm run build` menghasilkan `dist/`; `npm run preview` menjalankannya; dua ukuran sudah dibandingkan.
- [x] Git `.gitignore` memuat `node_modules/` dan `dist/`; `package-lock.json` ikut di-commit; lebih dari satu commit terencana.
- [x] Deklarasi AI README menyebutkan bagian mana yang dibantu AI dan bagian mana yang dikerjakan sendiri.
- [x] Lapisan data `src/api.js` dari Pertemuan 10 ikut pindah, isinya tidak diubah, dan fetch hanya ada di dalamnya.

---

#### G.2 Satu Baris untuk Diingat
> *"Di era framework komponen, kita tidak lagi mengutak-atik DOM secara manual: cukup ubah datanya secara reaktif, dan biarkan framework yang memperbarui tampilannya secara presisi."*

---

#### G.3 Penilaian Mandiri

| Bagian Penilaian | Bobot | Perkiraan Nilai | Bukti Berkas / Baris Kode |
| :--- | :---: | :---: | :--- |
| **Proyek Vue berjalan** | 20% | 20 / 20 | `package.json`, `vite.config.js`, `npm run dev` berjalan bersih di `http://localhost:5173/` |
| **Pemindahan tanpa mengubah perilaku** | 25% | 25 / 25 | `src/tokens.css`, `base.css`, `layout.css`, `komponen.css`, `tema.css`, `responsif.css`, `src/api.js`, `src/data.js` |
| **Pemecahan komponen dan props** | 20% | 20 / 20 | `src/components/KepalaProfil.vue` (props), `TombolFilter.vue`, `DaftarProyek.vue`, `FormKontak.vue` |
| **Build produksi dan preview** | 25% | 25 / 25 | `npm run build` menghasilkan `dist/` (HTML, CSS, JS ter-minify) dan lolos uji `npm run preview` |
| **Kebersihan src/, .gitignore, deklarasi AI, bukti** | 10% | 10 / 10 | `.gitignore` rapi, `node_modules` & `dist` diabaikan, `package-lock.json` tersimpan, deklarasi AI lengkap |
| **TOTAL** | **100%** | **100 / 100** | **Sangat Baik** |

---

#### G.4 Catatan untuk Pengampu
- **Bagian tersulit hari ini**: Menjaga integritas alur persistensi `localStorage` agar sinkron secara reaktif menggunakan kait siklus hidup Vue (`onMounted` dan `watch` beropsi `{ deep: true }`) tanpa menimbulkan perenderan ganda, serta menangani jalur sistem berkas lokal pada sistem operasi Windows agar kompatibel dengan modul URL parser Vite.
- **Yang ingin saya bahas di kelas berikutnya**: Manajemen state berskala lebih besar menggunakan pustaka store resmi seperti Pinia, serta integrasi routing multi-halaman pada aplikasi SPA menggunakan Vue Router.
- **Kendala perkakas yang saya alami**: Nama direktori lokal Windows yang memuat karakter hash (`#`) sempat dicegat oleh modul Vite dev server; kendala ini berhasil diselesaikan secara teknis menggunakan pemetaan *virtual drive* (`subst`) dan konfigurasi `preserveSymlinks: true`.

---

## Catatan Penggunaan AI (Pertemuan 12)

- **Bagian yang dibantu AI**:
  - Analisis mendalam terhadap skema instruksi lembar kerja P12 (`Worksheet P12`) dan pemetaan transisi arsitektur dari Vanilla JS P11 ke Vue 3 SFC.
  - Investigasi akar masalah peringatan Vite terkait karakter khusus path direktori pada Windows dan perumusan solusi integrasi `resolve.preserveSymlinks: true` di `vite.config.js`.
  - Simulasi pengujian antarmuka, reaktivitas tombol filter, persistensi `localStorage`, penanganan masukan formulir, dan eksekusi build produksi (`dist/`) melalui instrumentasi peramban CDP (*Chrome DevTools Protocol*).
  - Penyusunan dokumentasi komparasi metrik ukuran berkas sebelum dan sesudah proses *bundling*.
- **Bagian yang dikerjakan sendiri**:
  - Konfigurasi inisialisasi berkas proyek (`package.json`, `.gitignore`, `index.html`, `vite.config.js`).
  - Pemindahan 6 berkas CSS asli P04-P06 ke `src/` serta penyusunan urutan impor CSS terpusat pada `src/main.js`.
  - Perancangan dan implementasi 4 komponen Single File Component: `KepalaProfil.vue` (aliran data props), `TombolFilter.vue` (state kategori), `DaftarProyek.vue` (komputasi filter dan perenderan kartu), dan `FormKontak.vue` (penanganan form reaktif lokal `ref`).
  - Pemisahan lapisan keadaan reaktif `src/state.js` dan lapisan persistensi klien `src/simpanan.js` dengan proteksi data rusak.
  - Pengujian interaktif fungsionalitas pengalihan tema gelap (*CSS `:has`*), pengalihan filter film, dan pengisian form tambah film pada peramban lokal.
  - Penyusunan refleksi analitis dan jawaban lengkap atas seluruh pertanyaan tiket keluar Lembar G.

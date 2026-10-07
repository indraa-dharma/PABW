/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 8 - JavaScript Modern ES6+, Struktur Data, dan Array Methods
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Kelas   : SIF302 / B
 * Topik   : Halaman Profil & Daftar Film yang Pernah Saya Tonton
 */

/* ==========================================================================
   LEMBAR B: DATA HALAMAN SEBAGAI VARIABEL (OBJECT & MODERN ES6+)
   ========================================================================== */

// 1. Data Profil Mahasiswa & Topik Halaman (menggunakan const untuk objek referensi tetap)
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

// 2. Penggunaan let untuk variabel yang nilainya dapat berubah/diperbarui
let filterStatusAktif = "semua";
let counterPilihan = 0;

// 3. Pengecekan tipe data menggunakan typeof
console.log("=== LEMBAR B: NILAI, TIPE, DAN TEMPLATE LITERAL ===");
console.log("Tipe profil.nama        :", typeof profil.nama);         // "string"
console.log("Tipe profil.jumlahFilm    :", typeof profil.jumlahFilm);     // "number"
console.log("Tipe profil.keahlian      :", typeof profil.keahlian);       // "object" (Array)
console.log("Tipe filterStatusAktif    :", typeof filterStatusAktif);     // "string"

// 4. Template literal: menyusun kalimat dinamis
const kalimat = `Nama saya ${profil.nama}, dan saya belajar ${profil.keahlian.length} hal.`;
console.log(kalimat);

// 5. Demonstrasi operator modern: Nullish Coalescing (??) dan Optional Chaining (?.)
const kotaProfil = profil.kontak?.kota ?? "Kota belum diatur";
const provinsiProfil = profil.alamat?.provinsi ?? "Provinsi belum tersedia";
console.log(`Akses aman alamat: Kota = ${kotaProfil}, Provinsi = ${provinsiProfil}`);


/* ==========================================================================
   LEMBAR C: DUA FUNGSI MURNI (PURE FUNCTIONS)
   ========================================================================== */

/**
 * Fungsi 1: Menyusun kalimat perkenalan dari satu object
 * Menerima object dengan destructuring { nama, peran }
 * Murni: hanya bergantung pada argumen, mengembalikan string, tanpa efek samping.
 */
function buatPerkenalan({ nama, peran }) {
  return `${nama} — ${peran}`;
}

/**
 * Fungsi 2: Merapikan daftar keahlian menjadi satu baris teks
 * Menerima array string, mengembalikan string yang dipisahkan oleh ' · '
 * Murni: tidak mengubah array asli, konsisten dan mudah diuji.
 */
const formatKeahlian = (daftar) => daftar.join(" · ");

console.log("\n=== LEMBAR C: DUA FUNGSI MURNI ===");
console.log("Hasil buatPerkenalan :", buatPerkenalan(profil));
console.log("Hasil formatKeahlian :", formatKeahlian(profil.keahlian));


/* ==========================================================================
   LEMBAR D: STRUKTUR DATA DAN ARRAY METHODS
   ========================================================================== */

// 1. Array of Objects: Daftar Film yang Pernah Saya Tonton
const daftarFilm = [
  {
    id: 1,
    judul: "Inception",
    tahun: 2010,
    sutradara: "Christopher Nolan",
    rating: 8.8,
    genre: "Sci-Fi / Action",
    selesai: true,
    sinopsis: "Film dengan cerita tentang dunia mimpi dan pencurian informasi melalui mimpi."
  },
  {
    id: 2,
    judul: "The Shawshank Redemption",
    tahun: 1994,
    sutradara: "Frank Darabont",
    rating: 9.3,
    genre: "Drama",
    selesai: true,
    sinopsis: "Film drama tentang persahabatan, harapan, dan kehidupan di dalam penjara."
  },
  {
    id: 3,
    judul: "The Dark Knight",
    tahun: 2008,
    sutradara: "Christopher Nolan",
    rating: 9.0,
    genre: "Action / Crime",
    selesai: true,
    sinopsis: "Film superhero dengan konflik antara Batman dan ancaman besar di Gotham."
  },
  {
    id: 4,
    judul: "Interstellar",
    tahun: 2014,
    sutradara: "Christopher Nolan",
    rating: 8.7,
    genre: "Sci-Fi / Adventure",
    selesai: false,
    sinopsis: "Perjalanan antarbintang melewati lubang cacing untuk mencari planet baru yang layak huni."
  }
];

// Alias daftarProyek agar sesuai dengan template worksheet
const daftarProyek = daftarFilm;

console.log("\n=== LEMBAR D: STRUKTUR DATA & ARRAY METHODS ===");

// Menampilkan keahlian dan seluruh data proyek/film sebagai tabel
console.log("Tabel Keahlian Profil:");
console.table(profil.keahlian);

console.log("Tabel Seluruh Daftar Film / Proyek:");
console.table(daftarProyek);

// 2. filter: menyaring data (hanya film yang sudah selesai ditonton)
const selesai = daftarProyek.filter((proyek) => proyek.selesai);
console.log("Tabel Film yang Selesai Ditonton (filter):");
console.table(selesai);

// 3. find: mengambil satu elemen pertama yang cocok berdasarkan judul
const katalog = daftarProyek.find((proyek) => proyek.judul === "Inception");
console.log("Hasil Pencarian Film 'Inception' (find):", katalog);

// 4. map: mentransformasikan setiap objek ke bentuk string ringkasan
const ringkasanFilm = daftarFilm.map(
  (film) => `${film.judul} (${film.tahun}) - IMDb ${film.rating}`
);
console.log("Ringkasan Seluruh Film (map):", ringkasanFilm);

// 5. sort tanpa mutasi: menggunakan spread operator [...daftarFilm]
const filmUrutRating = [...daftarFilm].sort((a, b) => b.rating - a.rating);
console.log("Daftar Film Diurutkan Berdasarkan Rating Tertinggi (sort salinan):");
console.table(filmUrutRating);

// Verifikasi integritas data asli (tidak teracak)
console.log("Verifikasi data asli tidak berubah:");
console.log("- Judul film index 0 data asli tetap:", daftarFilm[0].judul); // Inception
console.log("- Judul film index 0 hasil sort rating :", filmUrutRating[0].judul); // The Shawshank Redemption


/* ==========================================================================
   LEMBAR E: PENANGANAN KASUS SULIT & KEBERSIHAN CONSOLE
   ========================================================================== */

console.log("\n=== LEMBAR E: PENANGANAN TIGA KASUS SULIT ===");

// Kasus 1: Mengakses properti bersarang tanpa galat menggunakan Optional Chaining
const cekKota = profil.kontak?.kota ?? "Default Kota";
const cekMedsos = profil.kontak?.instagram ?? "Instagram tidak dicantumkan";
console.log("Kasus 1 ditangani aman:", { kota: cekKota, medsos: cekMedsos });

// Kasus 2: Penanganan querySelector yang aman terhadap null
if (typeof document !== "undefined") {
  const formElemen = document.querySelector("#tambah-list-film form");
  if (formElemen) {
    console.log("Kasus 2 ditangani aman: Elemen form ditemukan di DOM.");
  } else {
    console.warn("Kasus 2: Elemen form tidak ditemukan (null), pemanggilan dihindari.");
  }
} else {
  console.log("Kasus 2 ditangani aman: Lingkungan non-browser, querySelector diamankan.");
}

// Kasus 3: Penjumlahan dari nilai input teks (mencegah konkatenasi string)
const inputContohTeks = "10";
const nilaiHasilJumlah = Number(inputContohTeks) + 5; // 15, bukan "105"
console.log(`Kasus 3 ditangani aman: Number("${inputContohTeks}") + 5 =`, nilaiHasilJumlah);

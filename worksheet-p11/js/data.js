/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 11 - Modul, State, dan Penyimpanan Klien
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Modul   : js/data.js (Data mentah dan fungsi murni pemformat)
 */

// 1. Data Mentah Profil Mahasiswa
export const profil = {
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

// 2. Data Mentah Daftar Film / Proyek
export const daftarFilm = [
  {
    id: 1,
    judul: "Inception",
    tahun: 2010,
    sutradara: "Christopher Nolan",
    rating: 8.8,
    genre: "Sci-Fi / Action",
    kategori: "Sci-Fi",
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
    kategori: "Drama",
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
    kategori: "Action",
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
    kategori: "Sci-Fi",
    selesai: false,
    sinopsis: "Perjalanan antarbintang melewati lubang cacing untuk mencari planet baru yang layak huni."
  }
];

// Alias daftarProyek agar sesuai konvensi template worksheet
export const daftarProyek = daftarFilm;

// 3. Fungsi Murni Pemformat (Pure Functions)

/**
 * Menyusun kalimat perkenalan dari satu objek profil
 * @param {Object} param0 
 * @returns {string}
 */
export function buatPerkenalan({ nama, peran }) {
  return `${nama} — ${peran}`;
}

/**
 * Merapikan daftar keahlian menjadi string dipisahkan titik tengah
 * @param {Array<string>} daftar 
 * @returns {string}
 */
export const formatKeahlian = (daftar) => daftar.join(" · ");

/**
 * Memformat representasi tahun atau tanggal
 * @param {string|number} nilai 
 * @returns {string}
 */
export function formatTanggal(nilai) {
  if (!nilai) return "-";
  return String(nilai);
}

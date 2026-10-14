/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 9 - DOM, Event, dan Interaktivitas
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Kelas   : SIF302 / B
 * Topik   : Halaman Profil & Daftar Film yang Pernah Saya Tonton
 */

import { daftarProyek } from "./app.js";
import { ambilFilm } from "./api.js";

/* ==========================================================================
   LEMBAR A & B: MEMILIH ELEMEN & RENDER DARI DATA
   ========================================================================== */

// Pemilih elemen DOM
const wadah = document.querySelector("#daftar");
const kosong = document.querySelector("#pesan-kosong");
const barisFilter = document.querySelector("#filter");

/**
 * Fungsi untuk membuat satu elemen kartu proyek/film dari data objek
 * Menggunakan createElement, textContent, dan append (aman dari XSS)
 * @param {Object} proyek - Data objek film
 * @returns {HTMLLIElement} Elemen li kartu
 */
function buatKartu(proyek) {
  const li = document.createElement("li");
  li.className = "kartu";

  const judul = document.createElement("h3");
  judul.className = "kartu__judul";
  judul.textContent = proyek.judul || proyek.title || "Tanpa Judul";

  const sinopsis = document.createElement("p");
  sinopsis.textContent = proyek.sinopsis || proyek.description || "Tidak ada sinopsis.";

  const kaki = document.createElement("div");
  kaki.className = "kartu__kaki";
  const tahun = document.createElement("span");
  const tahunVal = proyek.tahun || proyek.release_date || "2026";
  const katVal = proyek.kategori || proyek.genre || "Animasi";
  tahun.textContent = `${tahunVal} · ${katVal}`;
  const rating = document.createElement("strong");
  const ratingVal = proyek.rating ? proyek.rating : (proyek.rt_score ? (parseFloat(proyek.rt_score) / 10).toFixed(1) : "8.5");
  rating.textContent = `IMDB ${ratingVal}`;
  kaki.append(tahun, rating);

  const info = document.createElement("div");
  info.className = "kartu__info";
  const labelSutradara = document.createElement("span");
  labelSutradara.textContent = "Sutradara";
  const sutradara = document.createElement("strong");
  sutradara.textContent = proyek.sutradara || proyek.director || "Sutradara";
  info.append(labelSutradara, sutradara);

  li.append(judul, sinopsis, kaki, info);
  return li;
}

/**
 * Fungsi utama render: mengosongkan wadah, memeriksa keadaan kosong, lalu mengisi ulang
 * @param {Array} daftar - Array data film/proyek yang akan dirender
 */
function render(daftar) {
  // 1. Kosongkan wadah lebih dulu (mencegah kartu berlipat ganda)
  wadah.textContent = "";

  // 2. Periksa keadaan kosong (Keadaan Kosong)
  if (!daftar || daftar.length === 0) {
    if (kosong) {
      kosong.hidden = false;
      kosong.textContent = "Belum ada film yang tersedia.";
    } else {
      wadah.textContent = "Belum ada film yang tersedia.";
    }
    return;
  }

  if (kosong) kosong.hidden = true;

  // 3. Isi ulang wadah dengan elemen kartu (Keadaan Berhasil)
  daftar.forEach((proyek) => wadah.append(buatKartu(proyek)));
}

// Data aktif film
let daftarFilmAktif = [...daftarProyek];

/**
 * Fungsi asinkron untuk memuat data dari API publik (api.js)
 * Menangani 4 keadaan antarmuka: Memuat, Berhasil, Gagal, Kosong
 */
async function tampilkan() {
  // Keadaan 1: Memuat (loading state sebelum balasan datang)
  wadah.textContent = "Memuat data film dari API...";
  if (kosong) kosong.hidden = true;

  try {
    // Panggil lapisan data dari api.js (blok try/catch kedua di pemanggil)
    const data = await ambilFilm();

    // Normalisasi data dari API
    daftarFilmAktif = data.map((item, idx) => ({
      id: item.id || (idx + 1),
      judul: item.judul || item.title || "Tanpa Judul",
      tahun: item.tahun || item.release_date || 2026,
      sutradara: item.sutradara || item.director || "Sutradara",
      rating: item.rating ? item.rating : (item.rt_score ? (parseFloat(item.rt_score) / 10).toFixed(1) : 8.5),
      kategori: item.kategori || item.genre || "Animasi",
      sinopsis: item.sinopsis || item.description || "Tidak ada sinopsis."
    }));

    // Keadaan 4: Kosong jika larik hasil parse berukuran 0
    if (daftarFilmAktif.length === 0) {
      wadah.textContent = "Belum ada film yang tersedia.";
      if (kosong) kosong.hidden = false;
      return;
    }

    // Keadaan 2: Berhasil (render kartu-kartu data)
    render(daftarFilmAktif);
  } catch (galat) {
    // Keadaan 3: Gagal (galat ditangkap dan pesan ditampilkan di antarmuka)
    wadah.textContent = "Gagal memuat data: " + galat.message;
    if (kosong) kosong.hidden = true;
  }
}

// Ekspos fungsi render & tampilkan ke objek window untuk pengujian Console di DevTools
window.gambar = render;
window.tampilkan = tampilkan;

/* ==========================================================================
   LEMBAR C: EVENT DELEGATION PADA TOMBOL FILTER
   ========================================================================== */

/**
 * Menandai tombol filter yang sedang aktif dengan kelas .aktif
 * @param {HTMLButtonElement} tombolAktif - Tombol yang baru diklik
 */
function tandaiTombolAktif(tombolAktif) {
  document.querySelectorAll("#filter button").forEach((tombol) => {
    tombol.classList.toggle("aktif", tombol === tombolAktif);
  });
}

// Pasang satu pendengar di induk (#filter) untuk menangani semua tombol filter
if (barisFilter) {
  barisFilter.addEventListener("click", (event) => {
    const tombol = event.target.closest("button");
    if (!tombol) return; // klik di luar tombol, abaikan

    const kategori = tombol.dataset.kategori;
    tandaiTombolAktif(tombol);

    const terpilih = daftarFilmAktif.filter(
      (proyek) => kategori === "semua" || (proyek.kategori && proyek.kategori.toLowerCase().includes(kategori.toLowerCase()))
    );

    render(terpilih);
  });
}

// Inisialisasi tampilan data secara asinkron dari API
tampilkan();


/* ==========================================================================
   LEMBAR D: VALIDASI FORM YANG MENJAWAB SEBELUM DIKIRIM
   ========================================================================== */

const formFilm = document.querySelector("#tambah-list-film form");
const inputJudul = document.querySelector("#judul");
const inputTahun = document.querySelector("#tahun");
const inputSutradara = document.querySelector("#sutradara");
const inputRating = document.querySelector("#rating");
const tombolSubmit = formFilm ? formFilm.querySelector("button[type='submit']") : null;

/**
 * Memeriksa keabsahan satu input dan memperbarui atribut serta pesan galat
 * @param {HTMLInputElement} input - Elemen input yang diperiksa
 * @param {boolean} isSubmit - Apakah pemeriksaan dipicu saat tombol submit diklik
 * @returns {boolean} Status sah atau tidaknya input
 */
function periksaKolom(input, isSubmit = false) {
  const kolom = input.closest(".form-kolom");
  const pesanGalat = kolom ? kolom.querySelector(".pesan-galat") : null;
  const nilai = input.value.trim();
  let sah = true;

  if (input === inputJudul) {
    sah = nilai !== "";
  } else if (input === inputTahun) {
    const thn = Number(nilai);
    sah = nilai !== "" && !isNaN(thn) && thn >= 1800 && thn <= 2100;
  } else if (input === inputSutradara) {
    sah = nilai !== "";
  } else if (input === inputRating) {
    const rtg = Number(nilai);
    sah = nilai !== "" && !isNaN(rtg) && rtg >= 0 && rtg <= 10;
  }

  // Tampilkan galat jika tidak sah dan pengguna sudah berinteraksi atau sedang submit
  if (!sah && (isSubmit || input.dataset.touched === "true")) {
    input.setAttribute("aria-invalid", "true");
    if (pesanGalat) pesanGalat.style.display = "block";
  } else if (sah) {
    input.removeAttribute("aria-invalid");
    if (pesanGalat) pesanGalat.style.display = "none";
  }

  return sah;
}

/**
 * Memeriksa seluruh kolom dan mengaktifkan/menonaktifkan tombol kirim
 */
function periksaSeluruhForm() {
  const sahJudul = inputJudul ? inputJudul.value.trim() !== "" : false;
  const thn = inputTahun ? Number(inputTahun.value.trim()) : 0;
  const sahTahun = inputTahun ? (inputTahun.value.trim() !== "" && !isNaN(thn) && thn >= 1800 && thn <= 2100) : false;
  const sahSutradara = inputSutradara ? inputSutradara.value.trim() !== "" : false;
  const rtg = inputRating ? Number(inputRating.value.trim()) : -1;
  const sahRating = inputRating ? (inputRating.value.trim() !== "" && !isNaN(rtg) && rtg >= 0 && rtg <= 10) : false;

  const semuaSah = sahJudul && sahTahun && sahSutradara && sahRating;

  if (tombolSubmit) {
    tombolSubmit.disabled = !semuaSah;
  }

  return { semuaSah, sahJudul, sahTahun, sahSutradara, sahRating };
}

// Pasang pendengar validasi langsung saat mengetik (live validation)
if (formFilm) {
  const inputs = [inputJudul, inputTahun, inputSutradara, inputRating].filter(Boolean);

  inputs.forEach((input) => {
    input.addEventListener("input", () => {
      input.dataset.touched = "true";
      periksaKolom(input, false);
      periksaSeluruhForm();
    });

    input.addEventListener("blur", () => {
      input.dataset.touched = "true";
      periksaKolom(input, false);
      periksaSeluruhForm();
    });
  });

  // Jalankan pemeriksaan awal agar tombol submit sesuai status awal
  periksaSeluruhForm();

  // Penangan pengiriman form (submit)
  formFilm.addEventListener("submit", (event) => {
    // Di baris pertama penangan submit: menghentikan muat ulang bawaan
    event.preventDefault();

    let kolomPertamaGalat = null;

    inputs.forEach((input) => {
      input.dataset.touched = "true";
      const sah = periksaKolom(input, true);
      if (!sah && !kolomPertamaGalat) {
        kolomPertamaGalat = input;
      }
    });

    const { semuaSah } = periksaSeluruhForm();

    if (!semuaSah) {
      if (kolomPertamaGalat) {
        kolomPertamaGalat.focus();
      }
      return;
    }

    // Jika seluruh kolom valid: buat data film baru
    const filmBaru = {
      id: daftarFilmAktif.length + 1,
      judul: inputJudul.value.trim(),
      tahun: Number(inputTahun.value.trim()),
      sutradara: inputSutradara.value.trim(),
      rating: Number(inputRating.value.trim()),
      genre: "Drama",
      kategori: "Drama",
      selesai: true,
      sinopsis: `Film karya ${inputSutradara.value.trim()} yang dirilis pada tahun ${inputTahun.value.trim()}.`
    };

    daftarFilmAktif.unshift(filmBaru);
    daftarProyek.unshift(filmBaru);

    // Render ulang daftar dengan data terbaru
    render(daftarFilmAktif);

    // Bersihkan form dan kembalikan penanda filter ke 'semua'
    formFilm.reset();
    inputs.forEach((input) => {
      delete input.dataset.touched;
      input.removeAttribute("aria-invalid");
      const pesan = input.closest(".form-kolom")?.querySelector(".pesan-galat");
      if (pesan) pesan.style.display = "none";
    });

    const tombolSemua = document.querySelector("#filter button[data-kategori='semua']");
    if (tombolSemua) tandaiTombolAktif(tombolSemua);

    periksaSeluruhForm();
  });
}

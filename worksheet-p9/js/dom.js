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
  judul.textContent = proyek.judul;

  const sinopsis = document.createElement("p");
  sinopsis.textContent = proyek.sinopsis || "Tidak ada sinopsis.";

  const kaki = document.createElement("div");
  kaki.className = "kartu__kaki";
  const tahun = document.createElement("span");
  tahun.textContent = `${proyek.tahun} · ${proyek.kategori || proyek.genre || ""}`;
  const rating = document.createElement("strong");
  rating.textContent = `IMDB ${proyek.rating}`;
  kaki.append(tahun, rating);

  const info = document.createElement("div");
  info.className = "kartu__info";
  const labelSutradara = document.createElement("span");
  labelSutradara.textContent = "Sutradara";
  const sutradara = document.createElement("strong");
  sutradara.textContent = proyek.sutradara;
  info.append(labelSutradara, sutradara);

  li.append(judul, sinopsis, kaki, info);
  return li;
}

/**
 * Fungsi utama render: mengosongkan wadah, memeriksa keadaan kosong, lalu mengisi ulang
 * @param {Array} daftar - Array data film/proyek yang akan dirender
 */
function render(daftar) {
  // 1. Kosongkan wadah lebih dulu
  wadah.textContent = "";

  // 2. Periksa keadaan kosong
  if (!daftar || daftar.length === 0) {
    kosong.hidden = false;
    return;
  }

  kosong.hidden = true;

  // 3. Isi ulang wadah dengan elemen kartu
  daftar.forEach((proyek) => wadah.append(buatKartu(proyek)));
}


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

    const terpilih = daftarProyek.filter(
      (proyek) => kategori === "semua" || proyek.kategori === kategori
    );

    render(terpilih);
  });
}

// Render awal saat halaman pertama kali dimuat
render(daftarProyek);


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
      id: daftarProyek.length + 1,
      judul: inputJudul.value.trim(),
      tahun: Number(inputTahun.value.trim()),
      sutradara: inputSutradara.value.trim(),
      rating: Number(inputRating.value.trim()),
      genre: "Drama",
      kategori: "Drama",
      selesai: true,
      sinopsis: `Film karya ${inputSutradara.value.trim()} yang dirilis pada tahun ${inputTahun.value.trim()}.`
    };

    daftarProyek.push(filmBaru);

    // Render ulang daftar dengan data terbaru
    render(daftarProyek);

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

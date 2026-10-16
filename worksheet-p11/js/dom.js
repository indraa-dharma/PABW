/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 11 - Modul, State, dan Penyimpanan Klien
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Modul   : js/dom.js (Seluruh sentuhan ke halaman: pemilih, render, kelas)
 */

// 1. Pemilih Elemen DOM
export const wadah = document.querySelector("#daftar");
export const kosong = document.querySelector("#pesan-kosong");
export const barisFilter = document.querySelector("#filter");
export const tombolReset = document.querySelector("#tombol-reset");

export const formFilm = document.querySelector("#tambah-list-film form");
export const inputJudul = document.querySelector("#judul");
export const inputTahun = document.querySelector("#tahun");
export const inputSutradara = document.querySelector("#sutradara");
export const inputRating = document.querySelector("#rating");
export const tombolSubmit = formFilm ? formFilm.querySelector("button[type='submit']") : null;

/**
 * Membuat satu elemen kartu proyek/film dari data objek
 * Menggunakan createElement, textContent, dan append murni (aman dari XSS)
 * @param {Object} proyek 
 * @returns {HTMLLIElement}
 */
export function buatKartu(proyek) {
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
 * Menyaring daftar proyek dari state berdasarkan state.kategoriAktif
 * @param {Object} state 
 * @returns {Array}
 */
export function saring(state) {
  const kat = state.kategoriAktif;
  const daftar = state.daftarProyek || [];
  if (!kat || kat === "semua") {
    return daftar;
  }
  return daftar.filter((proyek) =>
    proyek.kategori && proyek.kategori.toLowerCase().includes(kat.toLowerCase())
  );
}

/**
 * Memperbarui tampilan tombol filter aktif di DOM berdasarkan state
 * @param {string} kategoriAktif 
 */
export function tandaiTombolAktif(kategoriAktif) {
  const tombolSemua = document.querySelectorAll("#filter button");
  tombolSemua.forEach((tombol) => {
    tombol.classList.toggle("aktif", tombol.dataset.kategori === kategoriAktif);
  });
}

/**
 * Fungsi utama render: menerima objek state dan menggambar ulang tampilan
 * Tiga pekerjaan tetap berurutan:
 * 1. Kosongkan wadah
 * 2. Periksa keadaan kosong
 * 3. Isi ulang dari state
 * @param {Object} state 
 */
export function render(state) {
  if (!wadah) return;

  // 1. Kosongkan wadah
  wadah.textContent = "";

  // 2. Periksa keadaan kosong
  const tampil = saring(state);
  if (tampil.length === 0) {
    if (kosong) {
      kosong.hidden = false;
      kosong.textContent = "Tidak ada proyek pada kategori itu.";
    }
    tandaiTombolAktif(state.kategoriAktif);
    return;
  }

  if (kosong) kosong.hidden = true;

  // 3. Isi ulang dari state
  tampil.forEach((item) => wadah.append(buatKartu(item)));
  tandaiTombolAktif(state.kategoriAktif);
}

// 2. Validasi Formulir (Helper DOM)

export function periksaKolom(input, isSubmit = false) {
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

  if (!sah && (isSubmit || input.dataset.touched === "true")) {
    input.setAttribute("aria-invalid", "true");
    if (pesanGalat) pesanGalat.style.display = "block";
  } else if (sah) {
    input.removeAttribute("aria-invalid");
    if (pesanGalat) pesanGalat.style.display = "none";
  }

  return sah;
}

export function periksaSeluruhForm() {
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

export function resetFormValidation() {
  const inputs = [inputJudul, inputTahun, inputSutradara, inputRating].filter(Boolean);
  inputs.forEach((input) => {
    delete input.dataset.touched;
    input.removeAttribute("aria-invalid");
    const pesan = input.closest(".form-kolom")?.querySelector(".pesan-galat");
    if (pesan) pesan.style.display = "none";
  });
  periksaSeluruhForm();
}

/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 11 - Modul, State, dan Penyimpanan Klien
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Modul   : js/state.js (Objek state tunggal dan fungsi pengubahnya)
 */

import { daftarProyek, profil } from "./data.js";
import { render } from "./dom.js";

// Kunci penyimpanan dan versi skema simpanan
const KUNCI = "pabw-p11";
const VERSI = 2;

// Objek state tunggal: satu-satunya sumber kebenaran seluruh aplikasi
export const state = {
  kategoriAktif: "semua",
  daftarProyek: [...daftarProyek],
  profil: { ...profil }
};

/* ==========================================================================
   LEMBAR D & E: PENYIMPANAN KLIEN (LOCALSTORAGE) & PENANGANAN RUSAK
   ========================================================================== */

/**
 * Menyimpan keadaan penting aplikasi ke localStorage dengan format JSON
 * @param {Object} stateObjek 
 */
export function simpan(stateObjek) {
  const isi = {
    versi: VERSI,
    kategoriAktif: stateObjek.kategoriAktif
  };
  localStorage.setItem(KUNCI, JSON.stringify(isi));
}

/**
 * Membaca simpanan dari localStorage dengan penanganan try/catch dan validasi versi
 * @returns {Object|null}
 */
export function muat() {
  try {
    const dataTeks = localStorage.getItem(KUNCI);
    if (!dataTeks) return null;

    const isi = JSON.parse(dataTeks);

    // Periksa nomor versi skema: bila tidak cocok, buang dan gunakan nilai bawaan
    if (isi?.versi !== VERSI) {
      localStorage.removeItem(KUNCI);
      return null;
    }

    return isi;
  } catch {
    // Tangani simpanan rusak (bukan JSON sah): buang simpanan dan pakai nilai bawaan
    localStorage.removeItem(KUNCI);
    return null;
  }
}

/**
 * Menghapus simpanan pada localStorage
 */
export function aturUlang() {
  localStorage.removeItem(KUNCI);
}

/* ==========================================================================
   LEMBAR C: FUNGSI PENGUBAH STATE (SATU PINTU MASUK SETIAP PERUBAHAN)
   ========================================================================== */

/**
 * Mengubah filter kategori aktif, menyimpan pilihan, dan menggambar ulang tampilan
 * @param {string} nilaiKategori 
 */
export function pilihKategori(nilaiKategori) {
  state.kategoriAktif = nilaiKategori;
  simpan(state);
  render(state);
}

/**
 * Menambahkan data film baru ke daftar state dan menggambar ulang tampilan
 * @param {Object} filmBaru 
 */
export function tambahFilm(filmBaru) {
  state.daftarProyek.unshift(filmBaru);
  render(state);
}

/**
 * Mengembalikan kategori aktif ke nilai bawaan dan membersihkan localStorage
 */
export function aturUlangPilihan() {
  aturUlang();
  state.kategoriAktif = "semua";
  render(state);
}

/**
 * Memperbarui seluruh daftar proyek dalam state dan menggambar ulang tampilan
 * @param {Array} daftarBaru 
 */
export function setDaftarProyek(daftarBaru) {
  state.daftarProyek = daftarBaru;
  render(state);
}

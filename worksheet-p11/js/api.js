/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 10 - JavaScript Asinkron: fetch, Promise, dan JSON
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Kelas   : SIF302 / B
 * Topik   : Halaman Profil & Daftar Film yang Pernah Saya Tonton
 * Berkas  : js/api.js (Lapisan Data)
 */

/* ==========================================================================
   LEMBAR A: ALAMAT TUNGGAL DAN PEMANGGILAN FETCH PERTAMA
   ========================================================================== */

// 1. Alamat API ditulis satu kali saja di bagian atas berkas (skema HTTPS, tanpa kunci akses)
const ALAMAT = "https://ghibliapi.vercel.app/films";
const ALAMAT_LOKAL = "./film.json";

/* ==========================================================================
   LEMBAR B: FUNGSI ASINKRON DENGAN ASYNC/AWAIT DAN TRY/CATCH
   ========================================================================== */

/**
 * Mengambil data film dari API publik dengan penanganan status respons.ok
 * dan penangkapan galat try/catch pada lapisan data.
 * @returns {Promise<Array>} Array data film
 */
export async function ambilFilm() {
  try {
    const respons = await fetch(ALAMAT);
    console.log("status", respons.status, "ok", respons.ok);

    // fetch tidak melempar galat pada 404/500, periksa respons.ok secara eksplisit
    if (!respons.ok) {
      throw new Error("status " + respons.status);
    }

    const data = await respons.json();
    return data;
  } catch (galat) {
    console.error("gagal memuat", galat.message);
    throw galat; // Lempar ke pemanggil (app.js / dom.js) untuk ditangani di UI
  }
}

// Alias fungsi untuk kesesuaian dengan panduan worksheet
export { ambilFilm as ambilNotisia };

/* ==========================================================================
   LEMBAR C: UTILITAS KONVERSI JSON DUA ARAH
   ========================================================================== */

/**
 * Demonstrasi konversi data dua arah: JSON.stringify dan JSON.parse
 * @param {Object} dataObjek 
 * @returns {string} teks JSON
 */
export function ubahKeJSON(dataObjek) {
  // Objek/nilai -> teks JSON (untuk dikirim ke server / localStorage)
  return JSON.stringify(dataObjek);
}

/**
 * Mengurai string JSON menjadi nilai JavaScript
 * @param {string} teksJSON 
 * @returns {Object|Array} nilai objek/array JS
 */
export function uraiDariJSON(teksJSON) {
  // Teks JSON -> nilai JavaScript (untuk membaca data lokal / localStorage)
  return JSON.parse(teksJSON);
}

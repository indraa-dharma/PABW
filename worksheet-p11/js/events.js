/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 11 - Modul, State, dan Penyimpanan Klien
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Modul   : js/events.js (Pemasangan seluruh pendengar peristiwa)
 */

import { pilihKategori, tambahFilm, aturUlangPilihan, state } from "./state.js";
import {
  barisFilter,
  tombolReset,
  formFilm,
  inputJudul,
  inputTahun,
  inputSutradara,
  inputRating,
  periksaKolom,
  periksaSeluruhForm,
  resetFormValidation
} from "./dom.js";

/**
 * Memasang seluruh event listener pada elemen DOM yang relevan
 */
export function pasangPendengar() {
  // 1. Event Delegation untuk seluruh tombol filter
  if (barisFilter) {
    barisFilter.addEventListener("click", (event) => {
      const tombol = event.target.closest("button");
      if (!tombol) return;

      const kategori = tombol.dataset.kategori;
      if (kategori) {
        // Panggil fungsi pengubah di state.js, bukan mengubah DOM atau state langsung
        pilihKategori(kategori);
      }
    });
  }

  // 2. Pendengar klik untuk tombol Atur Ulang Simpanan (Reset)
  if (tombolReset) {
    tombolReset.addEventListener("click", () => {
      aturUlangPilihan();
    });
  }

  // 3. Validasi interaktif langsung (live validation) pada formulir input
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

    // Jalankan pemeriksaan status tombol awal
    periksaSeluruhForm();

    // 4. Penanganan pengiriman formulir (submit)
    formFilm.addEventListener("submit", (event) => {
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

      // Buat objek film baru
      const filmBaru = {
        id: (state.daftarProyek.length ? Math.max(...state.daftarProyek.map((p) => p.id || 0)) : 0) + 1,
        judul: inputJudul.value.trim(),
        tahun: Number(inputTahun.value.trim()),
        sutradara: inputSutradara.value.trim(),
        rating: Number(inputRating.value.trim()),
        kategori: "Drama",
        genre: "Drama",
        selesai: true,
        sinopsis: `Film karya ${inputSutradara.value.trim()} yang dirilis pada tahun ${inputTahun.value.trim()}.`
      };

      // Tambahkan melalui fungsi pengubah state
      tambahFilm(filmBaru);

      // Reset form dan validasi
      formFilm.reset();
      resetFormValidation();
    });
  }
}

/**
 * PABW - Pengembangan Aplikasi Berbasis Web (SIF302)
 * Pertemuan 11 - Modul, State, dan Penyimpanan Klien
 * 
 * Nama    : Amadeus Dharma Akbarindra
 * NIM     : 25523253
 * Modul   : js/app.js (Perakit: mengimpor semuanya dan menjalankan aplikasi)
 */

import { state, muat } from "./state.js";
import { render } from "./dom.js";
import { pasangPendengar } from "./events.js";
import { ambilFilm } from "./api.js";

// 1. Muat data tersimpan dari localStorage bila ada
const simpanan = muat();
if (simpanan?.kategoriAktif) {
  state.kategoriAktif = simpanan.kategoriAktif;
}

// 2. Pasang seluruh pendengar peristiwa
pasangPendengar();

// 3. Render awal dari state (tampilan instan dari data mentah/state)
render(state);

// 4. Lapisan data masuk dari Pertemuan 10 bila api.js ada (B.4)
try {
  const dataApi = await ambilFilm();
  if (Array.isArray(dataApi) && dataApi.length > 0) {
    const dataApiNormalisasi = dataApi.slice(0, 2).map((item, idx) => ({
      id: 100 + idx,
      judul: item.title || item.judul || "Film Ghibli",
      tahun: Number(item.release_date) || item.tahun || 2026,
      sutradara: item.director || item.sutradara || "Hayao Miyazaki",
      rating: item.rt_score ? Number((parseFloat(item.rt_score) / 10).toFixed(1)) : 8.5,
      kategori: "Drama",
      genre: "Drama",
      selesai: true,
      sinopsis: item.description || item.sinopsis || "Film animasi karya Studio Ghibli."
    }));
    state.daftarProyek = [...state.daftarProyek, ...dataApiNormalisasi];
    render(state);
  }
} catch (galat) {
  console.warn("P10 API: Mode luring aktif / data lokal digunakan:", galat.message);
}

// 5. Ekspos ke objek window untuk keperluan pengujian interaktif di DevTools Console
window.state = state;
window.muat = muat;
window.render = render;

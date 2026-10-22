<script setup>
import { onMounted, watch } from 'vue'
import { state } from './state.js'
import { muat, simpan, aturUlang } from './simpanan.js'
import { ambilFilm } from './api.js'

import KepalaProfil from './components/KepalaProfil.vue'
import TombolFilter from './components/TombolFilter.vue'
import DaftarProyek from './components/DaftarProyek.vue'
import FormKontak from './components/FormKontak.vue'

const identitas = {
  nama: 'Amadeus Dharma Akbarindra',
  peran: 'Mahasiswa Informatika yang belajar front-end & mengulas film',
}

onMounted(async () => {
  const isi = muat()
  if (isi?.kategoriAktif) {
    state.kategoriAktif = isi.kategoriAktif
  }

  // Lapisan data API Pertemuan 10
  try {
    const dataApi = await ambilFilm()
    if (Array.isArray(dataApi) && dataApi.length > 0) {
      const dataApiNormalisasi = dataApi.slice(0, 2).map((item, idx) => ({
        id: 100 + idx,
        judul: item.title || item.judul || 'Film Ghibli',
        tahun: Number(item.release_date) || item.tahun || 2026,
        sutradara: item.director || item.sutradara || 'Hayao Miyazaki',
        rating: item.rt_score ? Number((parseFloat(item.rt_score) / 10).toFixed(1)) : 8.5,
        kategori: 'Drama',
        genre: 'Drama',
        selesai: true,
        sinopsis: item.description || item.sinopsis || 'Film animasi karya Studio Ghibli.'
      }))
      const idSet = new Set(state.daftarProyek.map(p => p.id))
      dataApiNormalisasi.forEach(item => {
        if (!idSet.has(item.id)) {
          state.daftarProyek.push(item)
        }
      })
    }
  } catch (err) {
    console.warn('P10 API: Mode luring aktif / data lokal digunakan:', err.message)
  }

  // Ekspos ke window untuk inspeksi DevTools
  if (typeof window !== 'undefined') {
    window.state = state
    window.muat = muat
  }
})

watch(state, (nilai) => simpan(nilai), { deep: true })

function aturUlangPilihan() {
  aturUlang()
  state.kategoriAktif = 'semua'
  simpan(state)
}
</script>

<template>
  <KepalaProfil :profil="identitas" />

  <main class="isi content">
    <aside id="tentang" class="sisi kartu">
      <div class="kartu__isi">
        <h2>Tentang Saya</h2>
        <p>
          Saya adalah mahasiswa yang memiliki beberapa film
          favorit dan ingin mencatat film yang pernah saya tonton.
        </p>
        <p>
          Data pada halaman ini berisi judul film, tahun rilis,
          sutradara, dan rating IMDB.
        </p>
      </div>

      <div class="kartu__kaki">
        <span>Amadeus Dharma Akbarindra</span>
        <span>2026</span>
      </div>
    </aside>

    <section id="film" class="utama">
      <h2>Daftar Film</h2>
      <TombolFilter @atur-ulang="aturUlangPilihan" />
      <DaftarProyek />
    </section>

    <FormKontak />
  </main>

  <footer class="page-footer">
    <p>Amadeus Dharma Akbarindra · 25523253 · 2026</p>
  </footer>
</template>

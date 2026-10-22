<script setup>
import { computed } from 'vue'
import { state } from '../state.js'

const daftarTersaring = computed(() => {
  const kat = state.kategoriAktif
  const daftar = state.daftarProyek || []
  if (!kat || kat === 'semua') {
    return daftar
  }
  return daftar.filter((proyek) =>
    proyek.kategori && proyek.kategori.toLowerCase().includes(kat.toLowerCase())
  )
})
</script>

<template>
  <div>
    <ul id="daftar" class="galeri grid" v-if="daftarTersaring.length > 0">
      <li
        v-for="proyek in daftarTersaring"
        :key="proyek.id"
        class="kartu"
      >
        <h3 class="kartu__judul">{{ proyek.judul || proyek.title || 'Tanpa Judul' }}</h3>
        <p>{{ proyek.sinopsis || proyek.description || 'Tidak ada sinopsis.' }}</p>
        <div class="kartu__kaki">
          <span>{{ (proyek.tahun || proyek.release_date || 2026) }} · {{ (proyek.kategori || proyek.genre || 'Film') }}</span>
          <strong>IMDB {{ proyek.rating ? proyek.rating : (proyek.rt_score ? (parseFloat(proyek.rt_score) / 10).toFixed(1) : '8.5') }}</strong>
        </div>
        <div class="kartu__info">
          <span>Sutradara</span>
          <strong>{{ proyek.sutradara || proyek.director || 'Sutradara' }}</strong>
        </div>
      </li>
    </ul>

    <p id="pesan-kosong" v-else>
      Tidak ada proyek pada kategori itu.
    </p>
  </div>
</template>

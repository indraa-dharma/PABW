<script setup>
import { state, pilihKategori } from '../state.js'
import { aturUlang, simpan } from '../simpanan.js'

const daftarKategori = ['semua', 'Action', 'Drama', 'Sci-Fi', 'Komedi']

const emit = defineEmits(['atur-ulang'])

function handleReset() {
  aturUlang()
  state.kategoriAktif = 'semua'
  simpan(state)
  emit('atur-ulang')
}
</script>

<template>
  <div class="filter-bar">
    <div id="filter">
      <button
        v-for="kategori in daftarKategori"
        :key="kategori"
        type="button"
        :data-kategori="kategori"
        :class="{ aktif: state.kategoriAktif === kategori }"
        @click="pilihKategori(kategori)"
      >
        {{ kategori === 'semua' ? 'Semua' : kategori }}
      </button>
    </div>
    <button
      type="button"
      id="tombol-reset"
      class="tombol-reset"
      @click="handleReset"
    >
      Atur Ulang Pilihan
    </button>
  </div>
</template>

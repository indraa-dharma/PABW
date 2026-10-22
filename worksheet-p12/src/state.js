/**
 * PABW - Pertemuan 12
 * src/state.js - Objek keadaan reaktif tunggal aplikasi
 */

import { reactive } from 'vue'
import { daftarProyek } from './data.js'

export const state = reactive({
  daftarProyek: [...daftarProyek],
  kategoriAktif: 'semua',
})

export function pilihKategori(nilai) {
  state.kategoriAktif = nilai // reaktif, tanpa render() manual
}

export function tambahFilm(filmBaru) {
  state.daftarProyek.unshift(filmBaru)
}

<script setup>
import { ref } from 'vue'
import { tambahFilm } from '../state.js'

const judul = ref('')
const tahun = ref('')
const sutradara = ref('')
const rating = ref('')

const submitted = ref(false)

function handleSubmit() {
  submitted.value = true

  if (!judul.value || !tahun.value || !sutradara.value || !rating.value) {
    return
  }

  const filmBaru = {
    id: Date.now(),
    judul: judul.value.trim(),
    tahun: Number(tahun.value),
    sutradara: sutradara.value.trim(),
    rating: Number(rating.value),
    kategori: 'Drama',
    genre: 'Drama',
    selesai: true,
    sinopsis: `Film karya ${sutradara.value.trim()} yang dirilis pada tahun ${tahun.value}.`
  }

  tambahFilm(filmBaru)

  // Kosongkan form setelah kirim tanpa memuat ulang halaman
  judul.value = ''
  tahun.value = ''
  sutradara.value = ''
  rating.value = ''
  submitted.value = false
}
</script>

<template>
  <section id="tambah-list-film" class="form-section bawah">
    <div class="panel-form">
      <h2>Tambah List Film</h2>

      <form @submit.prevent="handleSubmit" novalidate>
        <div class="form-kolom">
          <label for="judul">Judul Film:</label>
          <input
            type="text"
            id="judul"
            name="judul"
            v-model="judul"
            required
            :aria-invalid="submitted && !judul"
          />
          <small class="pesan-galat" v-if="submitted && !judul">
            Judul film harus diisi.
          </small>
        </div>

        <div class="form-kolom">
          <label for="tahun">Tahun Rilis:</label>
          <input
            type="number"
            id="tahun"
            name="tahun"
            min="1800"
            max="2100"
            v-model="tahun"
            required
            :aria-invalid="submitted && (!tahun || tahun < 1800 || tahun > 2100)"
          />
          <small class="pesan-galat" v-if="submitted && (!tahun || tahun < 1800 || tahun > 2100)">
            Tahun rilis harus diisi dengan angka yang sesuai (1800-2100).
          </small>
        </div>

        <div class="form-kolom">
          <label for="sutradara">Sutradara:</label>
          <input
            type="text"
            id="sutradara"
            name="sutradara"
            v-model="sutradara"
            required
            :aria-invalid="submitted && !sutradara"
          />
          <small class="pesan-galat" v-if="submitted && !sutradara">
            Nama sutradara harus diisi.
          </small>
        </div>

        <div class="form-kolom">
          <label for="rating">Rating IMDB:</label>
          <input
            type="number"
            step="0.1"
            min="0"
            max="10"
            id="rating"
            name="rating"
            v-model="rating"
            required
            :aria-invalid="submitted && (!rating || rating < 0 || rating > 10)"
          />
          <small class="pesan-galat" v-if="submitted && (!rating || rating < 0 || rating > 10)">
            Rating harus berada antara 0 sampai 10.
          </small>
        </div>

        <button type="submit">
          Tambah Film
        </button>
      </form>
    </div>
  </section>
</template>

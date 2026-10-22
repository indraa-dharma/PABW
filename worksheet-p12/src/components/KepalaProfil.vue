<script setup>
const props = defineProps({
  profil: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <header id="beranda">
    <div class="navbar">
      <div class="brand">
        <h1>{{ props.profil.nama }}</h1>
        <p>{{ props.profil.peran }}</p>
      </div>

      <div class="navbar-kanan">
        <input type="checkbox" id="tema" class="pengalih-tema">
        <label for="tema" class="tombol-tema">Tema gelap</label>

        <nav aria-label="Navigasi Utama">
          <ul>
            <li><a href="#beranda">Beranda</a></li>
            <li><a href="#film">Daftar Film</a></li>
            <li><a href="#tentang">Tentang Saya</a></li>
          </ul>
        </nav>
      </div>
    </div>
  </header>
</template>

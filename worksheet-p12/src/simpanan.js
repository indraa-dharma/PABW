/**
 * PABW - Pertemuan 12
 * src/simpanan.js - Lapisan persistensi klien (localStorage)
 */

const KUNCI = 'pabw-p11'
const VERSI = 2

export function simpan(stateObjek) {
  const isi = {
    versi: VERSI,
    kategoriAktif: stateObjek.kategoriAktif,
  }
  localStorage.setItem(KUNCI, JSON.stringify(isi))
}

export function muat() {
  try {
    const dataTeks = localStorage.getItem(KUNCI)
    if (!dataTeks) return null

    const isi = JSON.parse(dataTeks)

    // Periksa versi skema
    if (isi?.versi !== VERSI) {
      localStorage.removeItem(KUNCI)
      return null
    }

    return isi
  } catch {
    // Tangani simpanan rusak (bukan JSON sah)
    localStorage.removeItem(KUNCI)
    return null
  }
}

export function aturUlang() {
  localStorage.removeItem(KUNCI)
}

export { KUNCI, VERSI }

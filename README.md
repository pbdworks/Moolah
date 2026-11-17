# Moolah

**Kelola uangmu tanpa internet, tanpa biaya, tanpa mengorbankan privasi.**

Aplikasi budgeting pribadi yang gratis, open-source, dan 100% offline, dengan OCR struk dan sistem Kantong (Pockets).

[Fitur](#fitur-utama) | [Instalasi](#instalasi) | [Roadmap](#roadmap) | [Kontribusi](#kontribusi) | [Lisensi](#lisensi)

---

## Tentang Moolah

Kebanyakan aplikasi keuangan meminta data sensitif, mewajibkan akun, atau menyembunyikan fitur utama di balik langganan berbayar.

**Moolah** dibuat dengan pendekatan sebaliknya: sederhana, transparan, dan sepenuhnya milik penggunanya. Semua data tersimpan di perangkatmu sendiri. Tidak ada akun, tidak ada server, tidak ada pelacakan.

## Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| **Open-Source** | Kode terbuka dan bisa diaudit siapa saja. |
| **100% Offline** | Tidak butuh internet sama sekali. Data tersimpan lokal di perangkat. |
| **OCR Struk** | Foto struk belanja, lalu total, tanggal, dan nama toko dibaca otomatis. Proses OCR berjalan di perangkat, bukan di cloud. |
| **Kantong (Pockets)** | Bagi uangmu ke beberapa kantong seperti *Makan*, *Transport*, *Tabungan*, atau *Dana Darurat*. |
| **Gratis Selamanya** | Tanpa iklan, tanpa langganan, tanpa fitur berbayar. |

## Cara Kerja Kantong

1. **Buat kantong** sesuai kebutuhanmu (misalnya Makan, Transport, Hiburan).
2. **Isi kantong** dengan alokasi uang bulanan.
3. **Catat transaksi** secara manual atau scan struk dengan OCR.
4. **Pantau sisa** di setiap kantong dan lihat kapan kamu mendekati batas.

## Prinsip

1. **Privasi dulu**: datamu tidak pernah meninggalkan perangkatmu.
2. **Sederhana**: fokus pada hal yang benar-benar dibutuhkan untuk mengatur uang.
3. **Terbuka**: dibangun bersama komunitas, bukan untuk dimonetisasi.

## Tech Stack

> Sesuaikan bagian ini dengan teknologi yang kamu pakai.

- **Framework:** (contoh: Flutter / React Native / Kotlin)
- **Database lokal:** (contoh: SQLite / Drift / Room)
- **OCR on-device:** (contoh: Google ML Kit Text Recognition / Tesseract)

## Instalasi

> Moolah masih dalam tahap pengembangan. Rilis resmi akan tersedia di halaman [Releases](../../releases).

### Menjalankan dari source

```bash
# Clone repository
git clone https://github.com/<username>/moolah.git
cd moolah

# Install dependencies
# (sesuaikan dengan tech stack, contoh untuk Flutter)
flutter pub get

# Jalankan aplikasi
flutter run
```

## Roadmap

- [ ] Pencatatan pemasukan dan pengeluaran manual
- [ ] Sistem Kantong (buat, isi, transfer antar kantong)
- [ ] OCR struk di perangkat
- [ ] Ringkasan dan grafik pengeluaran
- [ ] Ekspor dan impor data (CSV / JSON)
- [ ] Backup dan restore lokal
- [ ] Mode gelap
- [ ] Dukungan multi-bahasa

## Kontribusi

Kontribusi sangat diterima dalam bentuk apa pun: kode, desain, terjemahan, laporan bug, maupun ide fitur.

1. Fork repository ini
2. Buat branch baru (`git checkout -b fitur/nama-fitur`)
3. Commit perubahanmu (`git commit -m "Tambah fitur ..."`)
4. Push ke branch (`git push origin fitur/nama-fitur`)
5. Buka **Pull Request**

Punya ide atau menemukan bug? Silakan buka [Issue](../../issues).

Dengan berkontribusi, kamu setuju bahwa kontribusimu dirilis di bawah lisensi yang sama dengan project ini (GPL-3.0).

## Lisensi

Moolah dirilis di bawah **GNU General Public License v3.0 (GPL-3.0)**. Kamu bebas memakai, mempelajari, memodifikasi, dan membagikan aplikasi ini. Jika kamu mendistribusikan versi yang dimodifikasi, kode sumbernya harus tetap terbuka dengan lisensi yang sama.

Lihat file [LICENSE](LICENSE) untuk teks lengkapnya.

---

Dibuat untuk siapa saja yang ingin mengatur uang tanpa mengorbankan privasi.

Kalau Moolah bermanfaat, beri bintang di repo ini!

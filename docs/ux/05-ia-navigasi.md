# IA dan navigasi

## Keputusan: bottom navigation 3 tab + aksi Catat
Gunakan **Beranda, Kantong, Riwayat** di bottom navigation, dengan CTA/FAB berlabel **Catat pengeluaran**. Pilihan ini tegas: bukan hamburger dan bukan dashboard-centric. Tiga tujuan berulang mudah dikenali, konsisten dengan pola mobile yang dipelajari (Jakob’s Law), dekat zona jempol, dan label mengurangi recall. Dashboard adalah isi Beranda, bukan navigasi kedua.

## Pohon IA
- **Beranda:** sisa semua Kantong, ringkasan, Catat, empty/offline/hampir habis/minus.
- **Kantong:** daftar, buat, detail, tambah/pindah uang.
- **Riwayat:** semua transaksi, filter, detail, edit/hapus.
- **Catat (aksi global):** manual/scan, koreksi, review dampak, sukses.
- **Pengaturan:** privasi/offline, ekspor lokal, kamera, bantuan, open-source.

## Aturan
Tab aktif berlabel + indikator + aria-current; posisi tidak berubah. Detail punya back konsisten. Form satu kolom: label permanen, nominal→Kantong→tanggal→catatan, validasi inline, tombol “Simpan transaksi”. Semua target 44×44 px; kontras teks normal ≥4.5:1; body minimal 16sp; judul 20–24sp; tidak ada informasi yang memakai teks <12sp. Dukung font scaling OS sampai 200% tanpa teks terpotong atau tumpang tindih. Status tidak hanya warna. Empty/error punya CTA dan batal/kembali. Offline menjelaskan data lokal dan tidak memblokir aksi lokal.

Referensi: [Jakob’s Law](https://www.nngroup.com/articles/jakobs-law/), [WCAG target](https://www.w3.org/TR/WCAG22/#target-size-minimum), [WCAG contrast](https://www.w3.org/TR/WCAG22/#contrast-minimum).

# Catatan keputusan — arah visual Moolah

Satu halaman. Ditulis 2026-11-18, sebelum runtime squad dipindah. Tujuannya: siapa pun yang melanjutkan tidak perlu mengulang dua penolakan yang sudah terjadi.

## Riwayat singkat, supaya tidak diulang

**Arah 1 — paper/terracotta.** Ditolak Davaa. Palet `#F7F3EA` + `#C2410C`, tipografi Plus Jakarta Sans + JetBrains Mono, tanpa serif. Alasan penolakan: tidak menyerupai aplikasi yang dia tunjuk.

**Arah 2 — slate/teal.** Ditolak Davaa. Palet `#F8FAFC` + `#176B87`, tanpa serif. Ini kesalahan yang lebih buruk: saya mengoreksi **menjauh** dari selera Davaa, bukan mendekat. Penyebabnya instruksi saya sendiri — "ambil pola, bukan kulit" — yang membuat riset menolak mendokumentasikan tipografi, palet, dan motion sebagai "tidak ada bukti yang memadai", lalu tetap diminta menghasilkan desain yang mengikuti aplikasi referensi.

**Arah 3 — Moneer.** Sedang berjalan saat pekerjaan dihentikan. Token diekstrak langsung dari canvas `NRSnt05BCx` yang Davaa tunjuk. Satu layar (Beranda) selesai, belum dinilai Davaa.

**Pelajaran yang mengikat:** kalau Davaa menunjuk sebuah canvas sebagai referensi, ekstrak tokennya dari canvas itu. Jangan menurunkan arah visual dari pola abstrak, dan jangan menulis "tidak ada bukti yang memadai" untuk hal yang bisa dilihat di layar.

## Yang diambil dari GoPay, Jago, myBCA

Ketiganya punya konsep kantong — ini temuan yang mengubah arah riset:

- **GoPay** — fokus pada tugas yang dipromosikan. Galeri Play Store-nya menonjolkan pembayaran QR/transfer sebagai kemampuan, bukan susunan home. Jangan mengklaim lebih dari itu.
- **Jago** — Kantong sebagai objek yang dapat dikelola: buat, isi, pindahkan. Ini model mental yang Moolah pakai.
- **myBCA** — punya **Rupiah Pocket** (hingga 100 per akun) dan **Forex Pocket**, plus **Financial Diary** untuk melacak pengeluaran harian. Ditemukan setelah paket Play Store yang benar (`com.bca.mybca.omni.android`) dibuka; percobaan pertama memakai paket salah dan sempat disimpulkan "tidak ada bukti".

Yang diambil: kantong sebagai objek, ringkasan sebelum detail, aksi utama dekat jangkauan jempol.

## Yang sengaja ditolak

- **Akun dan login sebagai prasyarat.** Moolah offline dan tanpa akun.
- **Ketergantungan jaringan.** Offline adalah state yang bisa dipakai, bukan error.
- **Saldo tunggal tanpa konteks Kantong.** Saldo total tidak menjawab "berapa yang boleh saya belanjakan untuk Makan?".
- **Menyalin logo, nama, atau aset brand.** Yang dipinjam bahasa visualnya, bukan identitasnya.
- **Tab bar sebagai default tanpa alasan.** Tiga destinasi dipilih karena Moolah punya tiga konsep, bukan karena aplikasi lain begitu.

## Keputusan visual yang sudah diambil

| Keputusan | Alasan |
|---|---|
| Kertas hangat `#E9E3D6`/`#FAF6EC`, bukan putih | Referensi memakainya; putih membuatnya terasa seperti dashboard SaaS |
| Fraunces untuk **semua angka uang** | Angka serif adalah pembeda utama arah ini. Tanpa itu, desain kembali generik |
| Plus Jakarta Sans untuk UI | Netral, tidak bersaing dengan serif |
| Satu permukaan jenuh (kartu pine-deep) | Mata punya satu tempat mendarat |
| Tanpa shadow | Pemisahan dari hairline dan kontras isian |
| Warna sebagai tata bahasa: hijau masuk, bata keluar, kuningan kewajiban | Tidak ada warna dekoratif |
| FAB `Catat` terangkat di tengah nav | Mencatat adalah kata kerja utama aplikasi |
| Tiga destinasi: Beranda, Kantong, Riwayat | IA Moolah, bukan IA Moneer (yang punya Transaksi/Jurnal/Lainnya) |

## Yang belum selesai

- Lima layar lain: Kantong, Manual, OCR, Sisa Kantong, Riwayat.
- Nav belum memakai ikon; referensi memakainya.
- Strip peringatan `Hampir habis` masih datar, belum ada ikon atau penekanan.
- Angka Transport di Beranda belum konsisten: terpakai Rp 25.000 dengan sisa Rp 20.000 menyiratkan batas Rp 45.000, dan "hampir habis" pada 44% sisa itu berlebihan.
- Target nav masih nama (`navigate:ManualB1`), bukan frame ID. Ganti saat lima layar dibangun, dan buktikan lewat `targetName` di `get_prototype`.
- Beranda belum dinilai Davaa.

## Status dokumen lain

- `06-prinsip-visual.md` di `main` masih menjelaskan arah paper/terracotta yang **sudah ditolak**. Jangan dipakai sebagai acuan. Arah yang berlaku ada di `08-token-referensi-moneer.md`.
- `07-riset-ui-referensi.md` (PR #5) berisi riset pola abstrak dari arah 2. Berguna sebagai catatan sumber, tapi **bukan** dasar arah visual.
- `accessibility-audit-hifi.md` mengaudit frame-frame arah 2 di canvas `lZZDl9Eagd`, yang sekarang jadi arsip.

# Audit UX kompetitor Moolah

**Tanggal audit:** 17 November 2026  
**Ruang lingkup:** onboarding, catat transaksi, lihat budget, dan scan struk.  
**Catatan evidensi:** audit desk research, bukan klaim uji pengguna langsung. Tautan pada kolom *bukti/screenshot* adalah halaman resmi atau galeri yang dapat dibuka untuk memeriksa layar yang dirujuk. Aplikasi yang tidak memiliki OCR struk ditandai **N/A**, bukan diasumsikan punya fitur tersebut.

## Metode dan skala

- **Tap** = ketuk kontrol yang diperlukan; mengetik satu field dihitung satu aksi submit, bukan tiap karakter. Back navigation dan membuka keyboard tidak dihitung. Jalur dihitung dari layar pertama setelah launch sampai transaksi tersimpan.
- **Langkah** = perpindahan layar/keputusan utama; tap boleh lebih banyak dari langkah karena beberapa tap terjadi pada layar yang sama.
- Jalur dicatat untuk konfigurasi Android/iOS yang terdokumentasi publik. Paywall, izin kamera, dan akun yang tidak wajib dicatat sebagai cabang.
- Temuan kualitatif mengikuti heuristik NN/g (H1–H10), tetapi skor numerik dihapus karena bukti publik tidak cukup untuk membedakan skor 3 dari 4. Setiap temuan menyebut observasi yang mendasarinya.

## Ringkasan angka

| Aplikasi | Tipe | Onboarding (estimasi tap/langkah) | Manual (estimasi tap/langkah) | Budget (estimasi tap/langkah) | Scan struk (estimasi tap/langkah) |
|---|---|---:|---:|---:|---:|
| Money Manager (Realbyte) | populer | 3/2 | 5/3 | 3/2 | N/A |
| Wallet by BudgetBakers | populer | 7/4 | 6/3 | 5/3 | 5/3 |
| Spendee | populer | 6/4 | 5/3 | 5/3 | N/A |
| Goodbudget | populer | 8/5 | 6/3 | 4/3 | N/A |
| Ivy Wallet | open-source | 2/2 | 4/3 | 3/2 | N/A |
| Cashew | open-source | 2/2 | 4/3 | 3/2 | N/A |
| Actual Budget | open-source | 6/4 | 7/4 | 5/3 | N/A |
| Bluecoins | populer | 3/2 | 6/3 | 4/2 | N/A |

**Interpretasi:** semua angka bertanda `~` adalah estimasi desk research, bukan pengukuran langsung. `terverifikasi` berarti dokumentasi langkah eksplisit tersedia; `estimasi` berarti jalur direkonstruksi dari screenshot/feature page. Angka adalah baseline komparatif untuk prototipe, bukan klaim bahwa aplikasi tercepat selalu terbaik. Moolah sebaiknya menargetkan manual **≤5 tap/3 langkah** dan scan berhasil **≤6 tap/3 langkah**, dengan koreksi OCR tidak disembunyikan.

## Tabel audit per aplikasi

### Money Manager (Realbyte)

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree) | ~3 tap / ~2 langkah | estimasi | Mulai cepat; kategori dan akun disiapkan sesudah masuk. |
| Catat transaksi | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree) | ~5 tap / ~3 langkah | estimasi | Form terstruktur; tanggal/kategori mudah dikenali, tetapi field cukup padat. |
| Lihat budget | [fitur resmi](https://realbyteapps.com/) | ~3 tap / ~2 langkah | estimasi | Ringkasan dan grafik memberi status saldo; budget tidak bercampur dengan transaksi. |
| Scan struk | N/A — tidak ditemukan fitur OCR struk pada sumber resmi | N/A | — | Tidak dijadikan baseline OCR. |

### Wallet by BudgetBakers

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.droid4you.application.wallet) | ~7 tap / ~4 langkah | estimasi | Onboarding kaya fitur tetapi akun/sinkronisasi menambah keputusan awal. |
| Catat transaksi | [fitur resmi](https://budgetbakers.com/) | ~6 tap / ~3 langkah | estimasi | Tombol tambah jelas; kategori dan akun tersedia sebagai pilihan. |
| Lihat budget | [fitur budget](https://budgetbakers.com/en/products/wallet/features/budgets/) | ~5 tap / ~3 langkah | estimasi | Progress budget eksplisit; visual berpotensi padat di layar kecil. |
| Scan struk | [Receipt Scanner](https://budgetbakers.com/en/products/wallet/features/receipt-scanner/) | ~5 tap / ~3 langkah | estimasi | OCR tersedia; pengguna perlu meninjau hasil sebelum simpan. |

### Spendee

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.cleevio.spendee) | ~6 tap / ~4 langkah | estimasi | Visual onboarding kuat; pilihan wallet dan fitur premium muncul dini. |
| Catat transaksi | [situs resmi](https://www.spendee.com/) | ~5 tap / ~3 langkah | estimasi | Input cepat dan kategori visual; recurring/bank sync bisa menambah kompleksitas. |
| Lihat budget | [budget feature](https://www.spendee.com/budgeting-app) | ~5 tap / ~3 langkah | estimasi | Sisa budget divisualkan per wallet. |
| Scan struk | N/A — tidak ditemukan OCR struk sebagai alur publik | N/A | — | Jangan menjadikan absennya fitur sebagai asumsi kebutuhan. |

### Goodbudget

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.dayspringtech.envelopes) | ~8 tap / ~5 langkah | estimasi | Model envelope dijelaskan dengan baik tetapi setup awal panjang. |
| Catat transaksi | [help—add transaction](https://goodbudget.com/help/transactions/add-a-transaction/) | ~6 tap / ~3 langkah | estimasi | Bahasa envelope konsisten; beberapa pilihan harus dipahami sebelum input. |
| Lihat budget | [help—envelopes](https://goodbudget.com/help/budgets/envelopes/) | ~4 tap / ~3 langkah | estimasi | Saldo per envelope sangat mudah dipindai. |
| Scan struk | N/A | N/A | — | Tidak ada alur OCR struk publik. |

### Ivy Wallet (open-source)

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [GitHub README/screenshots](https://github.com/Ivy-Apps/ivy-wallet) | ~2 tap / ~2 langkah | estimasi | Tanpa akun dan cepat; ini relevan untuk prinsip offline Moolah. |
| Catat transaksi | [GitHub](https://github.com/Ivy-Apps/ivy-wallet) | ~4 tap / ~3 langkah | estimasi | Aksi utama mudah ditemukan; kategori perlu sudah tersedia. |
| Lihat budget | [GitHub](https://github.com/Ivy-Apps/ivy-wallet) | ~3 tap / ~2 langkah | estimasi | Ringkas; kedalaman insight lebih terbatas dibanding aplikasi komersial. |
| Scan struk | N/A | N/A | — | Tidak tersedia pada dokumentasi publik yang diaudit. |

### Cashew (open-source)

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [GitHub README](https://github.com/jameskokoska/Cashew) | ~2 tap / ~2 langkah | estimasi | Setup minimal; cocok sebagai baseline tanpa akun. |
| Catat transaksi | [GitHub](https://github.com/jameskokoska/Cashew) | ~4 tap / ~3 langkah | estimasi | Input utama singkat; preset mengurangi ketikan. |
| Lihat budget | [GitHub](https://github.com/jameskokoska/Cashew) | ~3 tap / ~2 langkah | estimasi | Dashboard dan budget dapat dipindai cepat. |
| Scan struk | N/A | N/A | — | Tidak ditemukan OCR struk publik. |

### Actual Budget (open-source)

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [Getting started](https://actualbudget.org/docs/getting-started/) | ~6 tap / ~4 langkah | estimasi | Kuat untuk power user; setup server/sync bukan pola Moolah tanpa akun. |
| Catat transaksi | [transactions](https://actualbudget.org/docs/transactions/) | ~7 tap / ~4 langkah | estimasi | Kontrol rekonsiliasi kuat, namun lebih banyak konsep. |
| Lihat budget | [budgeting](https://actualbudget.org/docs/budgeting/) | ~5 tap / ~3 langkah | estimasi | Status budget sangat informatif tetapi kepadatan tinggi. |
| Scan struk | N/A | N/A | — | Tidak ditemukan OCR struk publik. |

### Bluecoins

| Alur | Bukti/screenshot | Estimasi tap/langkah | Keyakinan | Temuan |
|---|---|---:|---|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.rammigsoftware.bluecoins) | ~3 tap / ~2 langkah | estimasi | Dapat mulai tanpa setup panjang. |
| Catat transaksi | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.rammigsoftware.bluecoins) | ~6 tap / ~3 langkah | estimasi | Banyak opsi akuntansi membantu power user namun menambah pilihan. |
| Lihat budget | [website](https://www.bluecoinsapp.com/) | ~4 tap / ~2 langkah | estimasi | Laporan kuat; perlu hierarki agar pengguna baru tidak kewalahan. |
| Scan struk | N/A — tidak ditemukan OCR struk di sumber resmi yang diaudit | N/A | — | Tidak dijadikan baseline OCR. |

## Cakupan pasar Indonesia dan pembanding OCR

Audit awal tidak menemukan dokumentasi publik yang cukup untuk mengukur alur OCR struk pada tiga aplikasi berikut; baris ini sengaja dicatat agar celah evidensi tidak tertukar dengan fitur yang tidak ada:

| Aplikasi/target pasar | Bukti yang diaudit | OCR struk | Status pembanding |
|---|---|---|---|
| Money Lover | [situs resmi](https://moneylover.me/) · [Google Play](https://play.google.com/store/apps/details?id=com.bookmark.money) | Tidak ada langkah OCR yang terdokumentasi pada sumber publik yang diperiksa | Tidak memadai untuk benchmark tap |
| Finansialku (Indonesia) | [situs resmi](https://www.finansialku.com/) | Tidak ada langkah OCR struk yang terdokumentasi pada sumber publik yang diperiksa | Tidak memadai untuk benchmark tap |
| BukuKas (Indonesia) | [situs resmi](https://bukukas.co.id/) | Layanan/produk publik tidak menyediakan dokumentasi langkah OCR yang dapat direproduksi | Tidak memadai untuk benchmark tap |

Dengan demikian, **tidak ada pembanding OCR yang memadai** dalam audit desk research ini: Wallet by BudgetBakers adalah satu-satunya alur OCR yang dapat diverifikasi dari sumber publik. Target Moolah `≤6 tap/3 langkah` ditetapkan dari prinsip desain (kamera → pratinjau → review → simpan), bukan benchmark pasar. Jalur tersebut wajib diuji ulang pada setidaknya tiga aplikasi nyata atau build Moolah sebelum dipakai sebagai KPI.

## Pola yang layak ditiru

1. **Aksi tambah yang selalu terlihat** (Money Manager, Ivy, Cashew): target manual Moolah adalah maksimal 5 tap sampai simpan.
2. **Status sisa per envelope/kantong** (Goodbudget): tampilkan `tersisa`, `terpakai`, dan `batas` pada satu kartu; jangan memaksa pengguna membuka laporan.
3. **Tanpa akun sebagai jalur utama** (Ivy/Cashew): onboarding hanya nama mata uang dan Kantong pertama; sinkronisasi/ekspor bersifat opsional.
4. **Review sebelum commit untuk OCR** (Wallet): hasil OCR bukan langsung transaksi; tampilkan sumber foto, confidence, dan tombol Simpan/Koreksi/Scan ulang.
5. **Kategori/preset yang dikenali** (Money Manager/Cashew): default kategori dapat dipakai tanpa konfigurasi, tetapi tetap bisa diedit.
6. **Progress budget eksplisit** (Wallet/Actual): gunakan angka dan progress bar, bukan warna saja; dukung kontras minimum 4,5:1.

## Analisis khusus Kantong/envelope

Goodbudget adalah analog terdekat karena model envelope-nya eksplisit. Temuan berikut berasal dari dokumentasi bantuan, bukan uji pengguna:

| Pertanyaan desain | Goodbudget/envelope | Implikasi Moolah |
|---|---|---|
| Membuat Kantong | Envelope dibuat sebagai bagian dari budget dan diberi nama/kategori; istilah envelope konsisten di transaksi. [Dokumentasi](https://goodbudget.com/help/budgets/envelopes/) | Sediakan `Buat Kantong` dengan nama, ikon/warna opsional, batas periode opsional; gunakan istilah Kantong konsisten. |
| Mengisi dana | Budget dialokasikan ke envelope dari layar budget; saldo envelope menjadi angka yang dipantau. [Dokumentasi](https://goodbudget.com/help/budgets/envelopes/) | Aksi `Isi/Tambah dana` harus terlihat di detail Kantong, dengan konfirmasi saldo sebelum/sesudah. |
| Overspend | Goodbudget menampilkan envelope negatif/overspending dan menyediakan alokasi ulang untuk menutup kekurangan. [Dokumentasi](https://goodbudget.com/help/budgets/overspending/) | Jangan blokir transaksi; tampilkan state minus yang eksplisit, jumlah kekurangan, dan aksi `Pindahkan dana`/`Kurangi pengeluaran`. |
| Memindahkan antar Kantong | Dana dapat dipindahkan antar envelope untuk menyeimbangkan budget. [Dokumentasi](https://goodbudget.com/help/budgets/transfer-money/) | Transfer harus berupa form standar: sumber, tujuan, nominal, pratinjau saldo; sediakan batal/undo agar tidak terjadi kehilangan data. |

Keputusan Moolah: gunakan pola envelope yang dikenal, tetapi beri inovasi pada ringkasan `tersisa/terpakai/batas` dan pemulihan ketika saldo minus. Semua state tetap memiliki layar, bukan hanya perubahan warna.

## Pola yang harus dihindari

1. **Setup panjang sebelum nilai pertama** (Goodbudget/Wallet): jangan meminta akun, sinkronisasi, atau konfigurasi lengkap sebelum transaksi pertama.
2. **Memaksa konsep baru di navigasi** (Actual): gunakan bottom navigation dan form standar (Jakob's Law); inovasi hanya pada Kantong dan koreksi scan.
3. **Kepadatan kontrol power-user** (Bluecoins/Actual): tampilkan field inti dulu, opsi lanjutan di `Lainnya`.
4. **OCR tanpa jalur pemulihan**: confidence rendah harus menghasilkan layar koreksi yang menyebut field bermasalah; pengguna bisa batalkan atau ambil ulang tanpa kehilangan input.
5. **Status hanya mengandalkan warna**: state Kantong minus, kosong, offline, dan OCR gagal harus punya pesan, ikon/label, dan tindakan yang jelas.
6. **Paywall atau izin kamera menghalangi eksplorasi**: jelaskan mengapa kamera diperlukan, sediakan input manual, dan jangan meminta akun untuk data lokal.

## Keputusan untuk Moolah

- **Navigasi:** bottom navigation standar: `Beranda`, `Kantong`, `Riwayat`; tombol aksi utama `Catat` untuk transaksi manual dan scan. Ini pilihan tegas karena pola tersebut paling mudah dikenali dan konsisten dengan Jakob's Law. Label final mengacu ke `docs/ux/05-ia-navigasi.md`.
- **Target jalur:** manual ≤5 tap/3 langkah; OCR berhasil ≤6 tap/3 langkah sebelum simpan, lalu koreksi inline bila confidence rendah. Angka OCR ini prinsip desain sementara, bukan benchmark (hanya satu pembanding publik yang dapat diverifikasi).
- **Kriteria audit lanjutan:** ulangi pengukuran pada build Moolah dengan 3 task yang sama, catat median dan kegagalan, bukan hanya hitungan tap.

## Referensi heuristik

- [Nielsen Norman Group — 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Jakob's Law](https://lawsofux.com/jakobs-law/)
- [WCAG 2.2 — contrast minimum 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

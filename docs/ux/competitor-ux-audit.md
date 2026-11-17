# Audit UX kompetitor Moolah

**Tanggal audit:** 17 November 2026  
**Ruang lingkup:** onboarding, catat transaksi, lihat budget, dan scan struk.  
**Catatan evidensi:** audit desk research, bukan klaim uji pengguna langsung. Tautan pada kolom *bukti/screenshot* adalah halaman resmi atau galeri yang dapat dibuka untuk memeriksa layar yang dirujuk. Aplikasi yang tidak memiliki OCR struk ditandai **N/A**, bukan diasumsikan punya fitur tersebut.

## Metode dan skala

- **Tap** = ketuk kontrol yang diperlukan; mengetik satu field dihitung satu aksi submit, bukan tiap karakter. Back navigation dan membuka keyboard tidak dihitung. Jalur dihitung dari layar pertama setelah launch sampai transaksi tersimpan.
- **Langkah** = perpindahan layar/keputusan utama; tap boleh lebih banyak dari langkah karena beberapa tap terjadi pada layar yang sama.
- Jalur dicatat untuk konfigurasi Android/iOS yang terdokumentasi publik. Paywall, izin kamera, dan akun yang tidak wajib dicatat sebagai cabang.
- Heuristik NN/g = 10 heuristik Nielsen Norman Group: **H1** visibilitas status, **H2** kesesuaian sistem-dunia nyata, **H3** kontrol dan kebebasan pengguna, **H4** konsistensi/standar, **H5** pencegahan error, **H6** pengenalan alih-alih ingatan, **H7** fleksibilitas/efisiensi, **H8** desain minimalis, **H9** pemulihan error, **H10** bantuan/dokumentasi. Skor 1–5 (5 paling baik) adalah penilaian artefak, bukan usability test.

## Ringkasan angka

| Aplikasi | Tipe | Onboarding (tap/langkah) | Manual (tap/langkah) | Budget (tap/langkah) | Scan struk (tap/langkah) |
|---|---|---:|---:|---:|---:|
| Money Manager (Realbyte) | populer | 3/2 | 5/3 | 3/2 | N/A |
| Wallet by BudgetBakers | populer | 7/4 | 6/3 | 5/3 | 5/3 |
| Spendee | populer | 6/4 | 5/3 | 5/3 | N/A |
| Goodbudget | populer | 8/5 | 6/3 | 4/3 | N/A |
| Ivy Wallet | open-source | 2/2 | 4/3 | 3/2 | N/A |
| Cashew | open-source | 2/2 | 4/3 | 3/2 | N/A |
| Actual Budget | open-source | 6/4 | 7/4 | 5/3 | N/A |
| Bluecoins | populer | 3/2 | 6/3 | 4/2 | N/A |

**Interpretasi:** angka adalah baseline komparatif untuk prototipe, bukan klaim bahwa aplikasi tercepat selalu terbaik. Moolah sebaiknya menargetkan manual **≤5 tap/3 langkah** dan scan berhasil **≤6 tap/3 langkah**, dengan koreksi OCR tidak disembunyikan.

## Tabel audit per aplikasi

### Money Manager (Realbyte)

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree) | 3 tap / 2 langkah | H1 4, H4 4, H6 4 | Mulai cepat; kategori dan akun disiapkan sesudah masuk. |
| Catat transaksi | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree) | 5 / 3 | H2 4, H5 4, H7 4 | Form terstruktur; tanggal/kategori mudah dikenali, tetapi field cukup padat. |
| Lihat budget | [fitur resmi](https://realbyteapps.com/) | 3 / 2 | H1 4, H8 4 | Ringkasan dan grafik memberi status saldo; budget tidak bercampur dengan transaksi. |
| Scan struk | N/A — tidak ditemukan fitur OCR struk pada sumber resmi | N/A | — | Tidak dijadikan baseline OCR. |

### Wallet by BudgetBakers

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.droid4you.application.wallet) | 7 / 4 | H1 4, H3 3, H10 3 | Onboarding kaya fitur tetapi akun/sinkronisasi menambah keputusan awal. |
| Catat transaksi | [fitur resmi](https://budgetbakers.com/) | 6 / 3 | H2 4, H5 4, H7 4 | Tombol tambah jelas; kategori dan akun tersedia sebagai pilihan. |
| Lihat budget | [fitur budget](https://budgetbakers.com/en/products/wallet/features/budgets/) | 5 / 3 | H1 5, H6 4, H8 3 | Progress budget eksplisit; visual berpotensi padat di layar kecil. |
| Scan struk | [Receipt Scanner](https://budgetbakers.com/en/products/wallet/features/receipt-scanner/) | 5 / 3 | H1 4, H3 3, H5 3, H9 3 | OCR tersedia; pengguna perlu meninjau hasil sebelum simpan. |

### Spendee

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.cleevio.spendee) | 6 / 4 | H1 4, H4 4, H8 3 | Visual onboarding kuat; pilihan wallet dan fitur premium muncul dini. |
| Catat transaksi | [situs resmi](https://www.spendee.com/) | 5 / 3 | H2 4, H6 4, H7 4 | Input cepat dan kategori visual; recurring/bank sync bisa menambah kompleksitas. |
| Lihat budget | [budget feature](https://www.spendee.com/budgeting-app) | 5 / 3 | H1 4, H8 4 | Sisa budget divisualkan per wallet. |
| Scan struk | N/A — tidak ditemukan OCR struk sebagai alur publik | N/A | — | Jangan menjadikan absennya fitur sebagai asumsi kebutuhan. |

### Goodbudget

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.dayspringtech.envelopes) | 8 / 5 | H1 4, H2 5, H3 3 | Model envelope dijelaskan dengan baik tetapi setup awal panjang. |
| Catat transaksi | [help—add transaction](https://goodbudget.com/help/transactions/add-a-transaction/) | 6 / 3 | H2 5, H6 4, H7 3 | Bahasa envelope konsisten; beberapa pilihan harus dipahami sebelum input. |
| Lihat budget | [help—envelopes](https://goodbudget.com/help/budgets/envelopes/) | 4 / 3 | H1 5, H2 5, H8 4 | Saldo per envelope sangat mudah dipindai. |
| Scan struk | N/A | N/A | — | Tidak ada alur OCR struk publik. |

### Ivy Wallet (open-source)

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [GitHub README/screenshots](https://github.com/Ivy-Apps/ivy-wallet) | 2 / 2 | H1 4, H4 4, H8 5 | Tanpa akun dan cepat; ini relevan untuk prinsip offline Moolah. |
| Catat transaksi | [GitHub](https://github.com/Ivy-Apps/ivy-wallet) | 4 / 3 | H2 4, H6 4, H7 4 | Aksi utama mudah ditemukan; kategori perlu sudah tersedia. |
| Lihat budget | [GitHub](https://github.com/Ivy-Apps/ivy-wallet) | 3 / 2 | H1 3, H8 4 | Ringkas; kedalaman insight lebih terbatas dibanding aplikasi komersial. |
| Scan struk | N/A | N/A | — | Tidak tersedia pada dokumentasi publik yang diaudit. |

### Cashew (open-source)

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [GitHub README](https://github.com/jameskokoska/Cashew) | 2 / 2 | H1 4, H4 4, H8 4 | Setup minimal; cocok sebagai baseline tanpa akun. |
| Catat transaksi | [GitHub](https://github.com/jameskokoska/Cashew) | 4 / 3 | H2 4, H5 4, H6 4 | Input utama singkat; preset mengurangi ketikan. |
| Lihat budget | [GitHub](https://github.com/jameskokoska/Cashew) | 3 / 2 | H1 4, H8 4 | Dashboard dan budget dapat dipindai cepat. |
| Scan struk | N/A | N/A | — | Tidak ditemukan OCR struk publik. |

### Actual Budget (open-source)

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [Getting started](https://actualbudget.org/docs/getting-started/) | 6 / 4 | H1 3, H2 4, H10 4 | Kuat untuk power user; setup server/sync bukan pola Moolah tanpa akun. |
| Catat transaksi | [transactions](https://actualbudget.org/docs/transactions/) | 7 / 4 | H2 4, H5 4, H7 4 | Kontrol rekonsiliasi kuat, namun lebih banyak konsep. |
| Lihat budget | [budgeting](https://actualbudget.org/docs/budgeting/) | 5 / 3 | H1 5, H6 4, H8 3 | Status budget sangat informatif tetapi kepadatan tinggi. |
| Scan struk | N/A | N/A | — | Tidak ditemukan OCR struk publik. |

### Bluecoins

| Alur | Bukti/screenshot | Jalur terukur | NN/g (1–5) | Temuan |
|---|---|---:|---:|---|
| Onboarding | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.rammigsoftware.bluecoins) | 3 / 2 | H1 4, H4 4, H8 4 | Dapat mulai tanpa setup panjang. |
| Catat transaksi | [Google Play—screenshots](https://play.google.com/store/apps/details?id=com.rammigsoftware.bluecoins) | 6 / 3 | H2 4, H5 4, H6 3 | Banyak opsi akuntansi membantu power user namun menambah pilihan. |
| Lihat budget | [website](https://www.bluecoinsapp.com/) | 4 / 2 | H1 4, H8 3 | Laporan kuat; perlu hierarki agar pengguna baru tidak kewalahan. |
| Scan struk | N/A — tidak ditemukan OCR struk di sumber resmi yang diaudit | N/A | — | Tidak dijadikan baseline OCR. |

## Pola yang layak ditiru

1. **Aksi tambah yang selalu terlihat** (Money Manager, Ivy, Cashew): target manual Moolah adalah maksimal 5 tap sampai simpan.
2. **Status sisa per envelope/kantong** (Goodbudget): tampilkan `tersisa`, `terpakai`, dan `batas` pada satu kartu; jangan memaksa pengguna membuka laporan.
3. **Tanpa akun sebagai jalur utama** (Ivy/Cashew): onboarding hanya nama mata uang dan Kantong pertama; sinkronisasi/ekspor bersifat opsional.
4. **Review sebelum commit untuk OCR** (Wallet): hasil OCR bukan langsung transaksi; tampilkan sumber foto, confidence, dan tombol Simpan/Koreksi/Scan ulang.
5. **Kategori/preset yang dikenali** (Money Manager/Cashew): default kategori dapat dipakai tanpa konfigurasi, tetapi tetap bisa diedit.
6. **Progress budget eksplisit** (Wallet/Actual): gunakan angka dan progress bar, bukan warna saja; dukung kontras minimum 4,5:1.

## Pola yang harus dihindari

1. **Setup panjang sebelum nilai pertama** (Goodbudget/Wallet): jangan meminta akun, sinkronisasi, atau konfigurasi lengkap sebelum transaksi pertama.
2. **Memaksa konsep baru di navigasi** (Actual): gunakan bottom navigation dan form standar (Jakob's Law); inovasi hanya pada Kantong dan koreksi scan.
3. **Kepadatan kontrol power-user** (Bluecoins/Actual): tampilkan field inti dulu, opsi lanjutan di `Lainnya`.
4. **OCR tanpa jalur pemulihan**: confidence rendah harus menghasilkan layar koreksi yang menyebut field bermasalah; pengguna bisa batalkan atau ambil ulang tanpa kehilangan input.
5. **Status hanya mengandalkan warna**: state Kantong minus, kosong, offline, dan OCR gagal harus punya pesan, ikon/label, dan tindakan yang jelas.
6. **Paywall atau izin kamera menghalangi eksplorasi**: jelaskan mengapa kamera diperlukan, sediakan input manual, dan jangan meminta akun untuk data lokal.

## Keputusan untuk Moolah

- **Navigasi:** bottom navigation standar: `Ringkasan`, `Kantong`, `Transaksi`; tombol aksi utama `+` untuk transaksi dan scan. Ini pilihan tegas karena pola tersebut paling mudah dikenali dan konsisten dengan Jakob's Law.
- **Target jalur:** manual ≤5 tap/3 langkah; OCR berhasil ≤6 tap/3 langkah sebelum simpan, lalu koreksi inline bila confidence rendah.
- **Kriteria audit lanjutan:** ulangi pengukuran pada build Moolah dengan 3 task yang sama, catat median dan kegagalan, bukan hanya skor heuristik.

## Referensi heuristik

- [Nielsen Norman Group — 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Jakob's Law](https://lawsofux.com/jakobs-law/)
- [WCAG 2.2 — contrast minimum 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

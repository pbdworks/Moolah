# Riset UI referensi: GoPay, Jago, dan myBCA

## Kritik keputusan prototipe lama (RYUX Critique)

**Sumber yang dicoba:** canvas Doop `lZZDl9Eagd` dengan frame `XGOStniyLt` (Beranda), `PatjB3bLSw` (Kantong), `tKTdJzCQej` (Manual), `ZSyd_NGQhO` (OCR), `Wrsp6edBQe` (Sisa Kantong), dan `59rGPFJLOw` (Riwayat). MCP Doop tidak tersedia di runtime ini, jadi saya tidak dapat mengambil screenshot/metadata frame final secara langsung. Kritik ini memakai keputusan terdokumentasi di `docs/ux/05-ia-navigasi.md`, `docs/ux/06-prinsip-visual.md`, dan wireframe HTML sebagai sumber pengganti; status frame final ditandai tidak terverifikasi.

| ID | Temuan | Bukti RYUX | Kekuatan | Dampak keputusan |
|---|---|---|---|---|
| C-01 | Bottom navigation tiga tab dengan `Beranda` di kiri dipilih sebagai pola acuan, tetapi alasan dibanding drawer/stack atau aksi berbasis tugas tidak tercatat. | **Observed:** `05-ia-navigasi.md` menetapkan bottom navigation 3 tab. **Inferred:** pilihan ini mengikuti pola mobile umum. **Knowledge:** `mobile-design-thinking.md` memperingatkan tab bar sebagai default yang harus dipertanyakan. | Strong untuk keputusan yang terdokumentasi; Thin untuk alasan pengguna | Sebelum mengubah warna, uji apakah tiga destinasi memang tujuan berulang: Beranda, Kantong, Riwayat. Aksi `Catat` harus tetap dibedakan dari destinasi. |
| C-02 | Menempatkan Beranda di kiri memberi orientasi konvensional, tetapi mengorbankan pembuktian apakah layar yang paling sering dipakai adalah Beranda atau Catat. | **Observed:** urutan label pada IA. **Inferred:** Beranda dianggap titik masuk utama. **Judgment call:** belum ada data frekuensi task yang membuktikan urutan. | Thin | Validasi dengan task offline: buka aplikasi, catat pengeluaran, cek Kantong. Jika Catat dominan, pertimbangkan entry point aksi yang lebih langsung tanpa menambah tab. |
| C-03 | Enam layar mencakup Kantong, OCR, dan state offline/minus, tetapi keputusan navigasi tidak menjelaskan hubungan lintas alur tersebut secara eksplisit. | **Observed:** flow dan wireframe mendokumentasikan layar/state. **Inferred:** pengguna akan menemukan OCR melalui Catat. **Not verifiable:** target Doop final tidak dapat saya inspect. | Thin | Pastikan Beranda → Catat → Manual/OCR dan Beranda → Kantong dapat dijangkau tanpa menu tersembunyi; ukur task, bukan sekadar keberadaan tab. |
| C-04 | Eksekusi visual/aksesibilitas bukan masalah utama pada kritik ini: dokumen mencatat target 44/48px dan kontras AA. Masalahnya adalah keputusan navigasi belum memiliki pembanding atau kriteria keberhasilan. | **Observed:** aturan target/kontras di dokumen. **Knowledge:** touch target dan kontras adalah guardrail, bukan bukti IA optimal. | Strong | Fase B harus mempertahankan guardrail, tetapi memvalidasi arsitektur dengan trade-off eksplisit sebelum memoles token visual. |
| C-05 | Arah visual lama (paper/terracotta, tipografi dan kesan “buku kas”) dipilih tanpa sumber pembanding atau kriteria yang menghubungkannya ke offline, privasi, atau Kantong. Tiga aplikasi referensi memperlihatkan sistem visual yang berbeda: hierarki angka/label, kartu tujuan, dan peran warna sebagai pengenal; prototipe lama tidak menunjukkan alasan mengapa sistemnya harus menyerupai buku kas. | **Observed:** `06-prinsip-visual.md` mendokumentasikan arah paper/terracotta dan “buku kas”. **Inferred:** arah dipilih agar terasa hangat/playful. **Knowledge:** RYUX Critique melarang preferensi menjadi temuan tanpa bukti konteks; referensi visual publik menunjukkan pola alternatif, bukan token yang harus disalin. | Strong untuk keputusan yang terdokumentasi; Thin untuk alasan pengguna | Ubah lebih dulu sistem hierarki, kepadatan, dan peran warna berdasarkan pola yang bisa dirujuk; jangan sekadar mengganti warna. |

**Prioritas perubahan:** (1) nyatakan hipotesis IA dan alternatif yang ditolak, (2) uji tiga task utama pada entry point, (3) baru tetapkan sistem visual. Ini kritik keputusan, bukan klaim bahwa target sentuh, kontras, atau `problemCount` gagal.

**Fase:** A — riset sebelum perubahan prototype  
**Tanggal:** 18 November 2026  
**Batasan evidensi:** Saya tidak memiliki akun/login pada GoPay, Jago, atau myBCA dan tidak menjalankan aplikasinya pada perangkat. Karena itu, dokumen ini tidak mengklaim pengamatan layar pasca-login. Saya mencoba membuka listing Google Play dan galeri screenshot publik: GoPay (`com.gojek.gopay`) berhasil dibuka dan galeri gambarnya dapat diunduh; Jago berhasil dibuka dan tujuh preview screenshot dapat diunduh; URL awal myBCA (`com.bca.mybca`) 404, lalu paket yang benar (`com.bca.mybca.omni.android`) berhasil dibuka dan 12 preview screenshot dapat diunduh. Temuan di bawah berasal dari halaman resmi, pusat bantuan, listing aplikasi, dan materi publik yang dapat dibuka. Detail yang hanya dapat dipastikan setelah login ditulis **tidak ada bukti yang memadai**. Ini sengaja: referensi tidak boleh berubah menjadi detail rekaan.

## Cara baca dan tingkat keyakinan

Analisis memakai entry point RYUX Analyze: screenshot galeri yang berhasil diunduh diberi label **Observed**, nilai yang tidak terbaca dari capture diberi **Unknown**, dan penalaran lintas sumber diberi **Inferred**. Tidak ada RYUX MCP `search_screens` yang tersedia, sehingga tidak ada screen_id pembanding eksternal.

- **Terverifikasi publik:** klaim didukung halaman resmi atau dokumentasi resmi yang menyebut pola tersebut.
- **Terlihat publik:** klaim berasal dari screenshot/preview resmi, bukan interaksi langsung.
- **Tidak ada bukti yang memadai:** sumber publik tidak cukup untuk menyimpulkan detail.
- Angka tap yang direkonstruksi dari screenshot ditulis dengan `~`. Dalam riset ini, tidak ada jalur login yang bisa saya jalankan, sehingga tidak ada angka tap yang saya presentasikan sebagai pengukuran langsung.
- Saya membandingkan **pola**, bukan logo, nama, warna brand, atau komponen visual untuk disalin.

## Sumber yang dapat dibuka

| Produk | Sumber publik utama | Batasan sumber |
|---|---|---|
| GoPay | [Situs GoPay](https://gopay.co.id/), [Google Play GoPay](https://play.google.com/store/apps/details?id=com.gojek.gopay), [Pusat bantuan Gojek—GoPay](https://www.gojek.com/id-id/help/gopay) | Listing dan bantuan mendokumentasikan fitur; layar akun memerlukan login. |
| Jago | [Situs Bank Jago](https://www.jago.com/), [Google Play Jago](https://play.google.com/store/apps/details?id=com.jago.digitalBanking), [Pusat bantuan Jago](https://jago.com/id/support) | Dokumentasi publik cukup untuk konsep Kantong; urutan tap layar transaksi pasca-login tidak dapat dijalankan. |
| myBCA | [Situs myBCA](https://www.bca.co.id/id/Individu/produk/e-banking/myBCA), [Google Play myBCA](https://play.google.com/store/apps/details?id=com.bca.mybca.omni.android), [BCA—bantuan](https://www.bca.co.id/id/bantuan) | Preview publik dan catatan rilis menunjukkan Financial Diary serta Pocket Rupiah/Forex; layar akun dan motion penuh tetap memerlukan login. |

## GoPay

### Tujuh dimensi

| Dimensi | Temuan berbasis bukti | Keyakinan |
|---|---|---|
| Struktur home | Halaman produk dan listing publik memposisikan layanan pembayaran, transfer, tagihan, dan QR sebagai tugas utama. Galeri Play Store GoPay yang berhasil dibuka berisi materi promosi transfer, QRIS, dan paket data; saya tidak melihat layar home pencatatan finansial yang dapat diverifikasi. Jadi kesimpulan sebelumnya tentang kumpulan shortcut home GoPay **diturunkan**: sumber ini hanya mendukung bahwa GoPay menonjolkan tugas pembayaran, bukan jumlah atau susunan blok home. Jumlah blok yang benar-benar tampil dapat berubah menurut versi/akun; **tidak ada bukti yang memadai** untuk angka blok yang tetap. | Terlihat publik |
| Pola navigasi | Listing aplikasi menyebut ekosistem Gojek/GoPay dan beberapa layanan; screenshot publik memperlihatkan navigasi/shortcut, tetapi jumlah destinasi dan apakah pola finalnya tab atau halaman shortcut tidak dapat dipastikan tanpa login. Aksi pembayaran/QR secara konseptual berada dekat area thumb melalui shortcut utama, tetapi posisi piksel tidak saya klaim. | Terlihat publik; struktur final tidak memadai |
| Jalan ke transaksi | GoPay mendokumentasikan pembayaran QR dan transfer sebagai use case. Jalur tap pasca-login tidak dapat saya ukur; **tidak ada bukti yang memadai** untuk menyatakan `~N tap`. Shortcut pembayaran adalah pola yang terlihat dari materi publik, bukan pengukuran task. | Terverifikasi fitur; tap tidak memadai |
| Saldo dan kantong/kategori | GoPay memiliki saldo/uang elektronik dan fitur pembayaran, tetapi bukan model envelope budget. Sumber publik tidak menunjukkan pemisahan saldo menjadi Kantong dengan target progres. | Terverifikasi untuk saldo; tidak memadai untuk Kantong |
| Tipografi | Pada preview galeri GoPay yang terbaca, judul promosi memakai sans/display tebal dengan hierarki sangat besar; layar transaksi produk tidak tersedia, sehingga font UI, skala body, dan perlakuan angka uang **tidak ada bukti yang memadai**. Ini observasi materi screenshot, bukan token. | Tidak ada bukti yang memadai |
| Palet | Dari preview galeri GoPay yang terbaca, materi memakai bidang cyan/turquoise sebagai latar dan teks display hitam/putih pada materi promosi; ini bukan token UI dan bukan rekomendasi untuk disalin. Kode warna UI aktual tidak diterbitkan sebagai spesifikasi resmi yang dapat diverifikasi. | Terlihat publik; kode tidak memadai |
| Motion | Galeri screenshot GoPay bersifat statis; saya tidak menemukan rekaman interaksi yang bisa dipakai mengukur transisi/durasi. Motion **tidak ada bukti yang memadai**. | Tidak ada bukti yang memadai |

### Yang diambil dan ditolak

- **Diambil — fokus pada tugas yang dipromosikan:** galeri GoPay yang terbaca menonjolkan pembayaran QR/transfer sebagai kemampuan, tetapi tidak membuktikan susunan home atau shortcut dari permukaan utama. Untuk Moolah, implikasinya hanya: definisikan tugas utama secara eksplisit; keputusan posisi `Catat` harus berasal dari uji IA Moolah, bukan klaim tentang GoPay.
- **Diambil — kejelasan tugas bernilai tinggi:** sumber publik hanya membuktikan GoPay menonjolkan pembayaran/QR/transfer, bukan bahwa permukaan utamanya mengelompokkan tugas. Untuk Moolah, tampilkan `Sisa Kantong` dan transaksi terbaru sebelum laporan lanjutan berdasarkan prinsip offline dan kebutuhan keputusan cepat; jangan mengatribusikan susunan ini ke GoPay.
- **Ditolak — ketergantungan akun/layanan online:** GoPay mengandalkan ekosistem pembayaran dan akun. Moolah tidak meminta akun dan data harus tetap dapat digunakan offline; pola onboarding bertahap berbasis verifikasi tidak relevan.
- **Ditolak — model saldo tunggal sebagai pengganti Kantong:** saldo uang elektronik tidak memberi batas per kategori. Moolah perlu pemisahan Kantong dan state minus yang eksplisit.

## Jago (Bank Jago)

### Tujuh dimensi

| Dimensi | Temuan berbasis bukti | Keyakinan |
|---|---|---|
| Struktur home | Situs dan pusat bantuan Jago menjelaskan **Kantong (Pockets)** sebagai tempat mengatur uang berdasarkan tujuan. Ini membuat konsep tujuan/uang teralokasi menjadi objek produk, bukan sekadar label transaksi. Susunan blok home dan jumlah kartu yang tampil setelah login tidak dapat dipastikan dari sumber publik. | Terverifikasi konsep; layout final tidak memadai |
| Pola navigasi | Dokumentasi publik memperlihatkan akses ke Kantong dan aktivitas akun, tetapi jumlah destinasi dan apakah navigasi utama berupa tab, drawer, atau kombinasi tidak dapat diverifikasi tanpa sesi login. | Terverifikasi konsep; pola final tidak memadai |
| Jalan ke transaksi | Jago mendokumentasikan aktivitas transfer/pembayaran dan pengelolaan Kantong. Urutan dari home ke transaksi serta shortcut yang tersedia berbeda menurut task dan versi; **tidak ada bukti yang memadai** untuk angka tap. | Terverifikasi fitur; tap tidak memadai |
| Saldo dan kantong/kategori | Ini bukti terkuat: saldo dapat diatur ke Kantong berdasarkan tujuan, dan dokumentasi menjelaskan pembuatan/pengelolaan Kantong. Materi publik tidak cukup untuk mengukur apakah target ditampilkan sebagai progress bar atau hanya angka; jangan mengklaim bentuk visualnya. | Terverifikasi konsep; visual progres tidak memadai |
| Tipografi | Tiga dari tujuh preview galeri Jago yang saya baca memperlihatkan judul sans tebal berukuran dominan, label kecil di atas kartu, serta angka/daftar transaksi yang lebih rapat di layar investasi. Nama font dan skala numerik yang presisi **tidak ada bukti yang memadai**. | Tidak ada bukti yang memadai |
| Palet | Preview galeri Jago menunjukkan latar kuning/oranye dan pada materi Kantong memakai kartu-kartu berwarna dengan teks gelap/putih; ini dicatat sebagai peran warna dan kepadatan, bukan token untuk disalin. Kode warna UI aktual tidak dipublikasikan. | Terlihat publik; kode tidak memadai |
| Motion | Galeri yang saya buka adalah screenshot statis; tidak ada video interaksi yang dapat diukur. Motion Kantong **tidak ada bukti yang memadai**. | Tidak ada bukti yang memadai |

### Yang diambil dan ditolak

- **Diambil — uang sebagai Kantong tujuan:** memisahkan saldo utama dan alokasi tujuan mengurangi kebutuhan pengguna menghitung sendiri sisa kategori. Moolah menerapkannya pada kartu Kantong dengan `tersisa`, `terpakai`, dan `batas`.
- **Diambil — Kantong sebagai objek yang dapat dikelola:** buat, isi, dan pindahkan dana harus menjadi aksi yang terlihat pada detail Kantong, bukan hanya kategori pasif di form transaksi. Alasan: konsep Kantong adalah pembeda Moolah.
- **Ditolak — asumsi sinkronisasi bank:** Jago adalah bank digital dan dapat mengandalkan rekening/layanan online. Moolah harus tetap berfungsi saat offline dan tidak boleh mengirim data ke server.
- **Ditolak — kompleksitas finansial bank:** produk bank memiliki kebutuhan rekening, transfer, dan verifikasi yang tidak diperlukan untuk pencatatan pribadi Moolah. Moolah mengambil model mental Kantongnya, bukan seluruh IA bank.

## myBCA

### Tujuh dimensi

| Dimensi | Temuan berbasis bukti | Keyakinan |
|---|---|---|
| Struktur home | Listing benar menunjukkan fitur Financial Diary untuk melacak pengeluaran harian dan riwayat lintas akun; galeri yang dibaca menampilkan permukaan layanan/rekening, tetapi jumlah blok home tidak saya ukur. | Terverifikasi fitur; layout final sebagian terlihat |
| Pola navigasi | myBCA menyediakan banyak layanan dan preview menampilkan layar pengaturan/layanan; jumlah destinasi dan pola tab/drawer final tidak dapat dipastikan tanpa login. | Terlihat publik; struktur final tidak memadai |
| Jalan ke transaksi | Financial Diary adalah entry point pencatatan pengeluaran yang relevan; urutan tap dari home sampai tersimpan tidak dapat saya ukur tanpa login. | Terverifikasi fitur; tap tidak memadai |
| Saldo dan kantong/kategori | Catatan rilis listing menyebut pembuatan hingga 100 **Rupiah Pocket** per akun dan transaksi **Forex Pocket**. Preview galeri juga menampilkan kartu Pocket Rupiah/Valas. Ini mengubah kesimpulan lama: myBCA bukan hanya rekening/layanan; ia juga punya model pocket dan diary pengeluaran. | Terverifikasi listing + terlihat publik |
| Tipografi | Preview yang dibaca memakai sans tebal untuk headline promosi, label kecil untuk helper, dan teks UI sans pada mockup; nama font/skala numerik presisi tidak dapat diukur. | Terlihat publik; ukuran presisi tidak memadai |
| Palet | Preview memakai latar biru muda dan bidang putih pada materi promosi; mockup UI memakai aksen biru gelap. Ini deskripsi peran visual publik, bukan token Moolah. | Terlihat publik; kode token tidak memadai |
| Motion | Galeri statis; tidak ada video interaksi yang dapat mengukur durasi/transisi. | Tidak ada bukti yang memadai |

### Yang diambil dan ditolak

- **Diambil — ringkasan dan pencatatan dalam satu produk:** myBCA mendokumentasikan Financial Diary untuk pengeluaran harian, sekaligus riwayat lintas akun. Untuk Moolah, ini mendukung pemisahan jelas antara Catat dan Riwayat tanpa menghilangkan konteks Kantong. Moolah menerapkan hierarki ini dengan total tersisa, ringkasan Kantong, lalu riwayat; bukan menjejalkan semua laporan.
- **Diambil — pengelompokan layanan:** layanan bank yang berbeda dipisahkan sebagai tugas yang dapat dikenali. Moolah memisahkan `Catat`, `Kantong`, dan `Riwayat` secara semantik agar tombol Catat tidak bersaing dengan tab Riwayat.
- **Ditolak — alur autentikasi dan ketergantungan jaringan:** login, OTP, dan layanan rekening bukan bagian dari Moolah. Data lokal harus terbuka tanpa akun, dan offline harus menjadi state yang dapat dipakai, bukan error blocking.
- **Ditolak — saldo rekening tanpa konteks Kantong:** walaupun myBCA punya Pocket, konteks rekening dan layanan bank tidak boleh disalin sebagai IA penuh. Moolah tetap menampilkan sisa per Kantong dan dampak transaksi secara lokal/offline.

## Sistem visual ketiga aplikasi

Bagian ini mendeskripsikan **cara sistem visual disusun**, bukan memilih token Moolah. Observasi GoPay, Jago, dan myBCA berasal dari galeri screenshot Google Play yang saya unduh; myBCA dibaca dari paket benar `com.bca.mybca.omni.android` setelah URL awal 404.

| Produk | Hierarki angka dan label | Kepadatan/layout | Peran warna | Batas bukti |
|---|---|---|---|---|
| GoPay | Pada materi GoPay yang terbaca, headline promosi jauh lebih besar daripada label pendukung; angka transaksi pada layar produk tidak tersedia untuk dibandingkan. Tidak ada bukti tabular figures. | Materi promosi memakai satu pesan utama dan satu mockup ponsel; ini bukan bukti kepadatan home. | Cyan/turquoise menjadi bidang latar promosi; aksen hijau terlihat pada badge/pesan promo. Warna berfungsi sebagai identitas dan penekanan promo, bukan bukti state saldo. | Screenshot yang tersedia bukan home/transaksi lengkap; jangan menurunkan spacing atau token dari materi promosi. |
| Jago | Preview Kantong menempatkan nama Kantong dan label tujuan di atas kartu; preview investasi menampilkan angka dan daftar lebih rapat. Kontras judul–label jelas, tetapi font/angka presisi tidak dapat diukur dari crop. | Kantong disusun sebagai grid kartu berulang, sementara daftar investasi memakai baris yang lebih padat. Ini mendukung pemindaian objek tujuan tanpa menjadikan semua informasi sama berat. | Kartu Kantong memakai beberapa warna untuk membedakan tujuan; teks gelap/putih menyesuaikan latar. Warna berperan sebagai pengenal kategori, bukan satu-satunya status. | Hanya preview promosi; tidak ada pengukuran jarak piksel atau motion. |
| myBCA | Financial Diary; Pocket Rupiah/Valas; headline sans tebal, label kecil, mockup UI sans. | Pocket/Diary terverifikasi listing; visual terlihat publik; motion tidak memadai. | Biru muda/putih pada materi promosi, aksen biru gelap pada mockup; bukan token Moolah. | Tidak ada akses interaksi/login atau motion terukur. |

### Catatan yang bisa dipakai Fase B tanpa memilih token

1. Pisahkan **angka utama** dari label pendukung secara hierarkis; jangan membuat nominal, label, dan metadata sama besar.
2. Gunakan kepadatan berbeda sesuai tugas: kartu Kantong boleh berupa grid objek yang mudah dipindai, sedangkan daftar riwayat memakai baris konsisten.
3. Warna boleh membedakan objek Kantong atau menonjolkan aksi, tetapi status minus, offline, dan OCR gagal tetap membutuhkan label/teks; jangan mengandalkan warna saja.
4. Jangan mengklaim tabular figures, durasi motion, atau ukuran token sebelum ada screenshot produk yang cukup tajam atau inspeksi langsung.

## Perbandingan pola (bukan kulit visual)

| Pertanyaan | GoPay | Jago | myBCA | Pelajaran pola untuk Moolah |
|---|---|---|---|---|
| Unit utama | Tugas pembayaran | Uang berdasarkan tujuan/Kantong | Rekening, Pocket, dan Financial Diary | Gabungkan shortcut tugas dengan objek Kantong; jangan meniru model rekening. |
| Jalur transaksi | Shortcut pembayaran/QR terlihat dari materi publik | Transfer/pengelolaan Kantong; tap tidak terukur | Transfer/pembayaran; tap tidak terukur | `Catat` harus satu aksi utama dan tersedia dari Beranda; tidak mengarang benchmark tap. |
| Ringkasan | Saldo/layanan | Saldo + alokasi tujuan | Ringkasan rekening | Urutkan: sisa total → Kantong → riwayat. |
| Offline/privasi | Tidak relevan sebagai pola utama pembayaran online | Bergantung layanan bank | Bergantung layanan bank | Moolah mengambil kejelasan status, tetapi menolak ketergantungan jaringan/akun. |

## Delta terhadap prototipe sekarang

Delta di bawah adalah perubahan perilaku/struktur yang harus diuji pada enam layar; bukan pilihan warna atau font.

| Layar | Kondisi prototype sekarang | Perubahan pola yang diarahkan | Bukti/prinsip |
|---|---|---|---|
| **Beranda** | Ringkasan dan kartu Kantong sudah ada, dengan aksi Catat. | Jadikan `Catat` satu shortcut tugas yang paling mudah ditemukan; susun urutan **sisa total → Kantong prioritas → aktivitas terbaru**. Jangan menambah grid layanan seperti super-app. | GoPay: shortcut tugas; myBCA: ringkasan sebelum detail + Financial Diary; offline/privacy Moolah. |
| **Kantong** | Daftar Kantong dan aksi buat/isi sudah ada. | Jadikan Kantong sebagai objek utama: setiap kartu menampilkan tersisa/terpakai/batas; aksi `Isi`, `Pindahkan`, dan state minus dikelompokkan di detail, bukan disembunyikan di form transaksi. | Jago: alokasi berdasarkan tujuan; prinsip Kantong Moolah. |
| **Manual** | Form manual langsung simpan dan toast Urungkan. | Pertahankan simpan langsung (jangan menambah review); naikkan `Catat` sebagai jalur task dari Beranda dan gunakan preset Kantong agar pengguna tidak mengingat kategori. | GoPay: shortcut task; keputusan flow Moolah; target tap sebelumnya tetap harus divalidasi, bukan dianggap benchmark. |
| **OCR** | Review confidence rendah dan aksi pemulihan tersedia. | Pertahankan review karena input OCR tidak pasti; kelompokkan hasil sebagai tugas `Periksa → Koreksi → Simpan`, dengan fallback Isi manual tanpa kehilangan foto/hasil lain. | Prinsip pemulihan error; bukan pola visual brand. |
| **Sisa Kantong** | Detail sisa dan state minus sudah ada. | Tampilkan dampak transaksi pada Kantong sebagai ringkasan yang mudah dipindai: sebelum, nominal, sesudah; sediakan Pindahkan dana saat minus. | Jago: uang dialokasikan menurut tujuan; prinsip offline dan kontrol pengguna. |
| **Riwayat** | Daftar transaksi dan filter Kantong/periode tersedia. | Pertahankan filter sebagai kontrol eksplisit; tambahkan ringkasan per Kantong di atas daftar, lalu detail per baris. Hindari meniru feed layanan super-app yang mencampur semua aktivitas. | myBCA: ringkasan sebelum detail + Financial Diary; Kantong Moolah sebagai filter utama. |

### Keputusan yang sengaja belum dibuat

- **Palet dan font Moolah:** bukan keluaran Fase A. Jangan mengambil warna/font GoPay, Jago, atau myBCA.
- **Jumlah tab / bottom navigation:** riset ini tidak memberi bukti cukup untuk menyalin struktur navigasi ketiga aplikasi. Keputusan IA kanonik tetap dirujuk ke `docs/ux/05-ia-navigasi.md`; fase visual harus menjelaskan trade-off-nya, bukan menganggap tab bar sebagai default.
- **Durasi motion:** tidak ada bukti memadai dari sumber publik. Jangan mengarang durasi; pilih kemudian berdasarkan kebutuhan feedback dan `prefers-reduced-motion`.

## Ringkasan untuk review Fase A

1. **Pola terkuat untuk diadopsi:** shortcut berbasis tugas (GoPay), Kantong sebagai alokasi tujuan (Jago), dan ringkasan sebelum detail (myBCA).
2. **Pola yang ditolak:** akun/login sebagai prasyarat, ketergantungan jaringan, dan saldo tunggal tanpa konteks Kantong.
3. **Batas validitas:** tidak ada inspeksi pasca-login dan tidak ada pengukuran tap langsung. Klaim yang tidak bisa dibuktikan diberi label tidak memadai; Fase B harus memvalidasi perubahan terhadap prototype, bukan mengklaim benchmark aplikasi asal.
4. **Saran review:** setujui arah pola di atas dulu. Baru setelah itu tentukan token visual dan uji ulang enam layar dengan task offline yang sama.

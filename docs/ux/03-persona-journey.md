# Persona dan journey map

Persona ini hipotesis berbasis konteks dan sumber sekunder, bukan pengganti wawancara.

## Naya — mahasiswa, 20

**Konteks hidup:** uang saku tidak tetap; transaksi kecil dan cepat berulang; kadang berada tanpa jaringan.

**Perangkat & kenyamanan teknologi:** ponsel sebagai alat utama; nyaman dengan aplikasi sederhana, tetapi tidak ingin mengonfigurasi banyak kategori.

**Tujuan:**
1. Mengetahui sisa uang makan sampai akhir minggu.
2. Mencatat transaksi kecil sebelum lupa.
3. Memisahkan makan, transport, dan tabungan.

**Frustrasi:**
1. Form panjang untuk nominal kecil.
2. Kategori yang terasa menghakimi atau terlalu teknis.
3. Aplikasi yang tidak berfungsi saat offline.

**Kutipan khas:** “Saya mau tahu masih aman makan sampai akhir minggu, bukan belajar istilah keuangan.”

**Moolah gagal jika:** ia membutuhkan lebih dari beberapa tindakan untuk mencatat pengeluaran kecil atau tidak bisa melihat sisa Kantong tanpa internet.

## Raka — pekerja, 29

**Konteks hidup:** penghasilan bulanan; membayar tunai, QRIS, dan kartu; waktu mencatat sempit setelah perjalanan atau makan.

**Perangkat & kenyamanan teknologi:** pengguna ponsel yang cukup percaya diri; bersedia memberi izin kamera jika manfaat dan penyimpanan lokal jelas.

**Tujuan:**
1. Mencocokkan transaksi dengan struk fisik/digital.
2. Menjaga batas Kantong makan dan transport.
3. Menyelesaikan pencatatan tanpa mengulang data.

**Frustrasi:**
1. Total atau tanggal OCR keliru tanpa penanda.
2. Tidak bisa mengedit hasil scan.
3. Harus login atau menunggu jaringan.

**Kutipan khas:** “Saya bisa memeriksa hasilnya, tapi jangan suruh saya mengetik ulang semuanya.”

**Moolah gagal jika:** ia menyimpan OCR yang salah karena tidak melihat field bermasalah atau tidak punya kontrol foto ulang/manual.

## Sari & Bimo — keluarga, 36/38

**Konteks hidup:** satu orang sering belanja untuk rumah; kebutuhan rutin bercampur dengan pengeluaran tak terduga; keputusan perlu dapat ditelusuri bersama.

**Perangkat & kenyamanan teknologi:** menggunakan ponsel untuk tugas harian; nyaman dengan label jelas, kurang nyaman dengan istilah finansial dan pengaturan rumit.

**Tujuan:**
1. Mengetahui sisa kebutuhan rumah.
2. Memisahkan belanja rutin dan kebutuhan darurat.
3. Memahami transaksi yang membuat Kantong berubah atau minus.

**Frustrasi:**
1. Kategori baku tidak cocok untuk kebutuhan keluarga.
2. Saldo berubah tanpa riwayat atau penjelasan.
3. Kekhawatiran data rumah tangga tersimpan di cloud.

**Kutipan khas:** “Kalau uangnya minus, saya perlu tahu penyebabnya dan cara memperbaikinya.”

**Moolah gagal jika:** keluarga tidak dapat menamai/mengisi Kantong sesuai kebutuhan atau tidak dapat menelusuri transaksi penyebab minus.


## Journey mencatat pengeluaran
| Tahap | Perilaku & friksi | Respons desain |
|---|---|---|
| Sadar | Selesai bayar; takut lupa | CTA Catat selalu terlihat; manual dan kamera setara |
| Mulai | Memilih cara tercepat | Dua aksi berlabel, 44×44 px |
| Masukkan | Foto/isi nominal | Panduan frame, preview, validasi inline |
| Simpan manual | Pengguna baru saja memasukkan data; ingin feedback tanpa jeda | Langsung simpan → toast “Transaksi tersimpan · Sisa Makan Rp320.000” + **Urungkan** selama 5 detik |
| Periksa OCR | Meragukan hasil otomatis | Tandai field bermasalah; semua field inti editable; review dampak sebelum simpan |
| Pulih | OCR gagal atau berubah pikiran | Foto ulang, manual, batal; tidak auto-save transaksi |
| Kembali | Mengecek hasil | Riwayat, empty state edukatif, badge offline |

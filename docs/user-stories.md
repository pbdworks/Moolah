# User stories dan acceptance criteria

Semua story berikut adalah **Must / MVP**.

## US-1 — Membuat dan mengisi Kantong
Sebagai pengguna, saya ingin membuat Kantong dan mengalokasikan dana agar batas pengeluaran saya jelas.

**Acceptance criteria**
- Pengguna dapat memberi nama Kantong, warna opsional, dan nominal alokasi positif.
- Nama wajib diisi dan nama duplikat ditolak secara jelas.
- Saldo tersedia dihitung sebagai alokasi + pemasukan - pengeluaran; saldo tidak berubah karena tampilan saja.
- Pengguna dapat mengubah nama/alokasi dan melihat riwayat transaksi terkait.

## US-2 — Mencatat transaksi manual
Sebagai pengguna, saya ingin mencatat pemasukan atau pengeluaran ke Kantong agar saldo selalu aktual.

**Acceptance criteria**
- Form mewajibkan tipe, nominal positif, tanggal, Kantong, dan kategori; catatan/toko opsional.
- Simpan atomik: transaksi dan perubahan saldo terlihat bersama atau tidak sama sekali.
- Nominal invalid, tanggal invalid, atau Kantong terhapus ditolak tanpa data parsial.
- Pengguna dapat mengedit dan menghapus transaksi; konfirmasi ditampilkan sebelum hapus.

## US-3 — Memindai struk secara privat
Sebagai pengguna, saya ingin memindai struk tanpa internet agar pencatatan lebih cepat dan privat.

**Acceptance criteria**
- Foto diproses di perangkat; fitur tidak membutuhkan jaringan atau akun.
- Sistem mengusulkan total, tanggal, toko, dan teks mentah bila tersedia.
- Hasil OCR selalu berstatus draf dan tidak memengaruhi saldo sebelum pengguna mengoreksi/menyetujui.
- Saat OCR gagal, pengguna tetap dapat memasukkan data manual; gambar mentah boleh dibuang setelah selesai.

## US-4 — Mengoreksi dan menyimpan hasil OCR
Sebagai pengguna, saya ingin mengoreksi hasil scan sebelum disimpan agar saldo tidak salah.

**Acceptance criteria**
- Setiap field hasil OCR dapat diedit; nominal wajib valid dan Kantong/kategori wajib dipilih.
- Pengguna melihat ringkasan final sebelum konfirmasi.
- Menekan simpan membuat tepat satu transaksi (retry tidak menggandakan transaksi).
- Hasil yang dibatalkan tidak membuat transaksi atau perubahan saldo.

## US-5 — Melihat saldo dan ringkasan
Sebagai pengguna, saya ingin melihat saldo Kantong dan ringkasan periode agar bisa mengontrol pengeluaran.

**Acceptance criteria**
- Beranda menampilkan setiap Kantong: alokasi, terpakai, dan tersisa.
- Pengguna dapat memilih periode (minimal bulan berjalan dan rentang tanggal).
- Ringkasan menampilkan total pemasukan/pengeluaran dan breakdown kategori; angka konsisten dengan transaksi tersimpan.
- Empty state dan saldo minus dijelaskan tanpa menghalangi pengguna melihat atau memperbaiki transaksi.

## Definition of done MVP
Story diuji dengan data lokal, termasuk relaunch aplikasi dan perangkat offline; tidak ada request jaringan; validasi nominal/tanggal diuji; data tidak hilang saat transaksi gagal.

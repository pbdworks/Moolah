# User flow inti

Notasi: **[Layar]** → aksi → **[Layar]**. Target aksi 44×44 px.

## Onboarding
**[Welcome: privat/offline]** → Mulai tanpa akun → **[Izin kamera opsional]** → izinkan/lewati → **[Pilih template Kantong]** → **[Beranda empty]** → Catat/Buat Kantong. Kamera ditolak → **[Kamera tidak tersedia]** → Isi manual.

## Buat/isi Kantong
**[Kantong empty]** → Buat → **[Form nama, target opsional, saldo awal]** → validasi → **[Review]** → Simpan → **[Detail + sisa]**. Tambah uang: Detail → nominal/sumber → Review → simpan. Saldo 0 tetap boleh.

## Manual
**[Beranda/Kantong]** → Catat → **[Nominal, Kantong, tanggal, catatan]** → **[Review dampak sisa sebelum/sesudah]** → Simpan → **[Sukses + sisa]**. Offline: banner “tersimpan di perangkat”. Minus: **[Kantong minus]** dengan transaksi penyebab dan Tambah/Pindah/Edit; simpan tidak diblokir.

## Scan dan koreksi OCR
**[Pilih cara catat]** → Scan → **[Kamera + frame]** → foto → **[Memproses lokal dengan progress]**.
- Confidence tinggi → **[Review]** toko, total, tanggal, Kantong; tetap editable → Review dampak → Simpan.
- Confidence rendah → **[Review perlu diperiksa]**, alasan (“Total tidak terbaca jelas”), label field bermasalah, fokus ke field pertama. Field editable: toko, total, tanggal, Kantong, catatan (item hanya bila MVP mendukung).
- OCR gagal → **[Tidak dapat membaca struk]** tetap menampilkan preview + **Foto lagi / Pilih foto / Isi manual / Batal**. Tidak auto-save. Batal membuang hasil dengan konfirmasi bila telah diedit; foto ulang kembali kamera; manual memberi nominal kosong.

## Sisa Kantong
**[Beranda]** → Kantong → **[Detail: awal, terpakai, sisa, status]** → transaksi → **[Detail transaksi]** → edit/hapus → Review dampak. Empty punya Catat/Tambah; hampir habis memakai teks + warna; minus menampilkan sebab + pemulihan.

## State wajib
Offline (lanjut lokal), kamera ditolak (pengaturan/manual), OCR gagal (empat aksi), minus (dampak + pemulihan), empty (konteks + satu CTA).

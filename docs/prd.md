# PRD MVP Moolah

**Status:** draft untuk review Dava · **Target:** Android terlebih dahulu, iOS menyusul

## Ringkasan
Moolah membantu mahasiswa, pekerja, dan keluarga mencatat pengeluaran serta mengendalikan anggaran tanpa akun, server, iklan, atau koneksi internet. Nilai utamanya adalah pencatatan cepat, Kantong yang mudah dipahami, dan OCR struk yang tetap privat.

## Asumsi dan hal yang menunggu PBD-25
Dokumen ini memakai asumsi awal **Flutter + SQLite (akses melalui Drift) + OCR on-device**. PBD-25 belum selesai; setelah riset, hanya bagian bertanda ini yang boleh berubah: framework, library database, engine OCR, ukuran model, lisensi dependensi, serta target akurasi/perangkat. Prinsip offline, skema domain, dan batas MVP tetap menjadi baseline sampai ada keputusan Dava.

## Sasaran dan non-sasaran
**Sasaran MVP:** pengguna dapat membuat Kantong, mengalokasikan dana, mencatat transaksi manual, memindai struk lalu mengoreksi hasil OCR, dan melihat sisa serta ringkasan pengeluaran.

**Bukan MVP:** akun/sinkronisasi/cloud, koneksi bank atau e-wallet, pembayaran, budgeting otomatis/AI, multi-device collaboration, berbagi Kantong, langganan/iklan, dan dashboard analitik lanjutan. Ekspor/impor, backup/restore, multi-bahasa, dan tema gelap masuk fase berikutnya kecuali Dava memprioritaskan ulang.

## Prinsip produk
1. Data finansial tidak meninggalkan perangkat.
2. Semua hasil OCR adalah draf yang dapat dikoreksi; aplikasi tidak menyatakan hasil mesin sebagai fakta.
3. Aksi finansial eksplisit, dapat dibatalkan sebelum disimpan, dan nominal disimpan sebagai integer unit mata uang (bukan floating point).
4. MVP fokus pada satu mata uang pilihan pengguna dan timezone perangkat.

## Persona dan outcome
- **Pengguna hemat waktu:** ingin mencatat transaksi kurang dari satu menit.
- **Pengguna pemula budgeting:** ingin tahu uang yang masih aman dibelanjakan per Kantong.
- **Pengguna sadar privasi:** ingin fungsi penuh tanpa akun atau internet.

## Risiko produk
- OCR struk Indonesia beragam dan mungkin salah membaca nominal → tampilkan confidence/field yang perlu ditinjau, wajibkan konfirmasi sebelum simpan.
- Pengguna kehilangan perangkat → jelaskan bahwa MVP belum memiliki backup; prioritaskan backup lokal pada v0.2.
- Scope terlalu besar → kunci daftar Must di bawah; perubahan harus disetujui Dava.

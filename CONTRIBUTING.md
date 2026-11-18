# Berkontribusi ke Moolah

Moolah adalah project GPL-3.0, offline-first, dan privacy-first. Sebelum implementasi dimulai, baca `docs/prd.md`, `docs/user-stories.md`, dan `docs/architecture.md`.

## Alur kontribusi
1. Buka atau pilih issue yang jelas; jangan menggabungkan fitur di luar scope tanpa persetujuan maintainer.
2. Fork atau buat branch dari default branch: `feat/<ringkas>`, `fix/<ringkas>`, atau `docs/<ringkas>`.
3. Perubahan produk harus menyertakan acceptance test atau alasan mengapa tidak relevan.
4. Jalankan formatter, analyzer, dan test yang tersedia sebelum PR. Jangan menambahkan dependency tanpa memeriksa lisensi dan kebutuhan offline.
5. Buka PR memakai template. Satu PR sebaiknya satu tujuan yang dapat direview.

## Aturan privasi
Tidak boleh ada network call untuk data finansial, telemetry tersembunyi, secret, nominal/merchant/raw OCR di log, atau upload gambar struk. Semua permission harus memiliki alasan UX. Perubahan schema wajib migration dan test.

## Commit dan review
Gunakan commit imperatif singkat. PR memerlukan minimal satu reviewer; perubahan schema, OCR, atau privasi memerlukan reviewer domain. Maintainer dapat meminta perubahan untuk aksesibilitas, data loss, security, atau lisensi.

## Laporan bug dan keamanan
Gunakan issue template untuk bug/feature. Jangan publikasikan data finansial atau gambar struk. Untuk kerentanan yang belum ditambal, hubungi maintainer secara privat melalui kanal repository dan sertakan langkah reproduksi minimal.

## Lisensi
Dengan mengirim kontribusi, kamu setuju kontribusi dilisensikan di bawah GPL-3.0 sebagaimana repository ini.

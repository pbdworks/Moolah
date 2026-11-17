# Roadmap dan backlog

Estimasi adalah kalender relatif setelah scope MVP disetujui; satu minggu = kapasitas satu squad kecil. Target dapat berubah setelah PBD-25/PBD-27.

## Milestone

| Milestone | Target | Isi | Exit criteria |
|---|---:|---|---|
| MVP | Minggu 1–6 | shell Flutter, schema/migration, Kantong, transaksi, ringkasan, OCR draft + koreksi, offline QA | Lima story MVP lulus acceptance; smoke test pada perangkat target; tidak ada network dependency |
| v0.2 | Minggu 7–9 | ekspor/impor CSV/JSON, backup/restore lokal, enkripsi storage bila layak, filter/recurring sederhana | round-trip backup berhasil; dokumentasi recovery |
| v1.0 | Minggu 10–14 | polish aksesibilitas, multi-bahasa, dark mode, OCR tuning berbasis dataset, release packaging | usability review, regression suite, release checklist |

## Backlog (dibuat sebagai tabel; issue dibuat kemudian oleh owner)

| Judul | Squad tujuan | Prioritas | Dependency |
|---|---|---|---|
| Bootstrap Flutter, CI lint/test, offline guard | Engineering | Must | keputusan PBD-25 |
| SQLite/Drift schema + migrations + DAO | Engineering | Must | bootstrap |
| Domain use cases dan saldo Kantong | Engineering | Must | schema |
| UI buat/isi/arsip Kantong | UI/UX + Engineering | Must | domain |
| UI transaksi manual + edit/hapus | UI/UX + Engineering | Must | domain |
| Summary period/category + empty/minus states | UI/UX + Engineering | Must | transaksi |
| OCR adapter dan parser receipt | Engineering | Must | PBD-25, kamera |
| Flow OCR review/correction/idempotent save | UI/UX + Engineering | Must | OCR adapter, transaksi |
| Offline/relaunch/security acceptance tests | QA | Must | semua MVP |
| UX usability test dan accessibility pass | UI/UX + QA | Should | UI MVP, PBD-27 |
| CSV/JSON export-import | Engineering | Should | schema stabil |
| Backup/restore lokal + encryption assessment | Engineering + QA | Should | export, PBD-25 |
| Dark mode dan multi-bahasa | UI/UX + Engineering | Could | UI stabil |
| Recurring transactions dan transfer Kantong | Engineering | Could | transaksi |
| Cloud sync, accounts, bank integration | — | Won't (MVP) | keputusan produk baru |

## Prioritas MoSCoW
**Must:** lima user story, persistence lokal, validasi, migration, offline guard, dan QA. **Should:** export/backup dan accessibility/usability polish. **Could:** tema, bahasa, recurring/transfer. **Won't:** akun, sync, cloud OCR, bank/e-wallet, monetisasi, dan analitik prediktif.

## Risiko dan mitigasi
| Risiko | Dampak | Mitigasi | Pemilik |
|---|---|---|---|
| OCR Indonesia tidak konsisten | saldo salah | draft + review wajib, fallback manual, benchmark PBD-25 | Engineering/QA |
| keputusan stack terlambat | pekerjaan ulang | isolasi adapter; tandai asumsi; kunci keputusan sebelum bootstrap | Squad lead |
| scope melebar | milestone mundur | change control berbasis Must/Should/Could/Won't | Product/Dava |
| kehilangan perangkat | data hilang | peringatan jelas MVP, backup lokal v0.2, recovery test | Engineering |
| dependensi berlisensi tidak cocok | risiko distribusi | license inventory dan review sebelum merge | Engineering |

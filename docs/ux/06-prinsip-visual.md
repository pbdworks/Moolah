# Prinsip desain dan arah visual Moolah

## Arah baru: calm task finance
Moolah memakai permukaan netral terang, tinta navy, dan aksen teal untuk membangun hierarki tugas tanpa menyalin warna merek kompetitor. Arah ini merespons referensi GoPay, Jago, dan myBCA: tugas utama harus mudah dipindai, angka finansial dominan, ringkasan mendahului detail, dan warna memiliki satu peran.

**Status bukti hue:** Thin. Riset referensi mendukung hierarki, kepadatan, dan peran warna; tidak memberikan dasar kuat untuk hue Moolah tertentu. Hue dapat diganti bila ada bukti pengguna atau uji desain yang lebih baik.

## Token visual
| Role | Token | Nilai | Peran |
|---|---|---|---|
| Surface | `--color-surface-new` | `#F8FAFC` | latar netral |
| Card | `--color-card-new` | `#FFFFFF` | ringkasan dan panel |
| Ink | `--color-ink-new` | `#172033` | teks utama dan angka |
| Muted | `--color-muted-new` | `#526174` | label sekunder |
| Primary | `--color-primary-new` | `#176B87` | CTA dan tautan aksi |
| Safe | `--color-safe-new` | `#176B5B` | status aman dan indikator proporsi |
| Warn | `--color-warn-new` | `#8A5A00` | status hampir habis/minus |

Primary tidak dipakai untuk status; safe/warn tidak dipakai sebagai CTA. Semua status memiliki teks, bukan warna saja.

## Tipografi dan angka
- Plus Jakarta Sans untuk UI dan teks.
- JetBrains Mono untuk nominal agar digit mudah dibandingkan.
- Body 16px, label 14px, judul 28px, angka utama 40px.
- Weight 400/700 membedakan informasi sekunder dan aksi/angka penting.

## Spacing, bentuk, dan target
- Spacing: 4/8/12/16/24px.
- Radius: 8px untuk kontrol, 14px untuk panel.
- Target sentuh minimum 48px, jarak antartarget minimal 8–12px.
- Kontras normal minimal 4.5:1; palet B1 telah diverifikasi lulus AA.

## Hierarki layar
1. Ringkasan atau status utama.
2. Angka finansial dan proporsi Kantong.
3. Aktivitas/transaksi terbaru.
4. Aksi utama yang jelas sebagai aksi, bukan tab.
5. Detail dan pemulihan error.

Beranda harus menjelaskan rekonsiliasi total, Kantong harus dapat dikelola, dan Riwayat harus mendahulukan filter lalu daftar transaksi. Format data lintas layar wajib konsisten.

## Motion dan aksesibilitas
Gunakan motion singkat hanya untuk perubahan state. `prefers-reduced-motion: reduce` mematikan animation, transition, dan transform. Fokus keyboard harus terlihat dengan outline 3px. Form memakai label permanen dan pesan error/status semantik. Progress Kantong memakai `role="progressbar"` dengan nilai 0–100 yang cocok dengan lebar visual.

## Dasar keputusan
- Hierarki angka dan ringkasan sebelum detail: observasi lintas Jago/myBCA, Strong.
- Shortcut berbasis tugas: observasi terbatas GoPay, Thin.
- Kantong sebagai objek yang dapat dikelola: pola Pocket Jago/myBCA dan prinsip produk Moolah, Strong.
- Hue surface/ink/teal Moolah: keputusan desain sementara, Thin; jangan diperlakukan sebagai temuan kompetitor.

## Status
Arah baru diterapkan pada frame B1 Beranda `SEufifNC2w` dan Kantong `NE6vwZLtzZ`, serta B2 Manual, OCR, Sisa Kantong, dan Riwayat. Frame lama tetap arsip pembanding dan tidak dihapus.
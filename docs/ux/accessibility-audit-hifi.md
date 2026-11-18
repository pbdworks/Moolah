# Audit aksesibilitas — frame high-fidelity Beranda

Frame diaudit: `XGOStniyLt` (Doop). Audit berbasis HTML dan `inspect_frame`; uji screen reader nyata tetap perlu dilakukan pada sesi pengguna.

| Area | Bukti | Dampak | Rekomendasi | Prioritas |
|---|---|---|---|---|
| Fokus dan nav fixed | `.nav{position:fixed;bottom:0}`; target nav 48px; `main` memiliki padding bawah 96px | Ruang bawah mencegah konten terakhir tertutup; tetap perlu uji Tab pada tinggi layar kecil/zoom 200% | Verifikasi keyboard di viewport kecil; pertahankan padding bawah ≥ tinggi nav + 24px | High |
| Tab aktif | `nav a[aria-current=page]`; Beranda computed weight 700, tab lain 400; border bawah terracotta | State aktif dapat diumumkan dan dilihat; `page` tepat untuk navigasi halaman utama | Pertahankan label selalu tampil dan indikator non-warna | Pass |
| Struktur heading | `h1` Beranda, `h2#recent-title` Transaksi terakhir; kartu saldo dan Kantong memakai label/`article`, bukan heading | Lompatan heading tidak menemukan setiap kartu, tetapi landmark section tetap tersedia | Bila kartu perlu navigasi langsung, tambahkan heading level 3; jangan menambah heading hanya untuk styling | Medium |
| Reduced motion | `@media(prefers-reduced-motion:no-preference)` menerapkan animasi `.pocket`; `@media(prefers-reduced-motion:reduce)` menetapkan `animation:none`, `transition:none`, `transform:none` | Preferensi reduce mematikan animasi pocket sepenuhnya | Pertahankan pola ini dan uji computed animation dalam kedua mode | Pass |
| CTA accessible name | CTA memiliki teks “Catat pengeluaran” dan `aria-label` dengan nilai sama | Aman, tetapi label redundan karena accessible name sudah berasal dari teks | Hapus `aria-label` atau ubah hanya bila label visual berbeda; teks terlihat sudah cukup | Low |
| Status offline | `.offline-status[role=status]` berisi “Offline · tersimpan lokal” | Status diumumkan sebagai status, bukan hanya glyph/warna | Pertahankan teks dan role; jangan menyampaikan offline hanya dengan warna | Pass |
| Status Kantong | `.status--safe` memakai `--color-safe`, `.status--warn` memakai `--color-warn`; teks “Sisa aman”/“Hampir habis” | Status tidak bergantung pada warna saja; warna semantik konsisten | Pertahankan pasangan label + warna; uji kontras pada render | Pass |
| Touch target & spacing | `nav a` min 48px, margin 4px + gap 8px; CTA min-height 44px | Target memenuhi 48dp nav dan spacing efektif 16px | Uji juga pada font scaling 200% agar reflow tidak tumpang tindih | Pass/High |

## Prioritas tindak lanjut

1. **High:** uji keyboard nyata pada viewport kecil dan zoom 200% untuk memastikan fixed nav tidak menutupi fokus.
2. **Medium:** pertimbangkan heading level 3 bila kartu Kantong/Saldo menjadi tujuan navigasi langsung.
3. **Low:** hapus `aria-label` CTA yang identik dengan teks visual untuk mengurangi redundansi.

Kontras warna mengikuti angka yang diberikan pada review Morgan; audit ini tidak mengulang perhitungan rasio.
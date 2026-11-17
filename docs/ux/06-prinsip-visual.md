# Prinsip desain dan arah visual Moolah

## Arah
Moolah harus terasa **tenang, tepercaya, dan dekat**, seperti buku kas pribadi yang tetap bekerja tanpa internet. “Playful” berarti tidak kaku—bukan dekorasi seperti game. Privasi dan kontrol pengguna terlihat pada momen simpan, izin kamera, dan status offline.

## Tipografi
- **Plus Jakarta Sans** untuk UI dan teks; dibuat Tokotype untuk identitas Jakarta.
- **JetBrains Mono** untuk seluruh angka uang agar digit sejajar saat panjang nominal berbeda.
- Body 16px/1.5, judul 28px/1.2 weight 700, saldo 40px weight 700; gunakan kontras weight 400/700.
- Dukung pembesaran font OS 200% tanpa teks terpotong/bertumpuk; informasi tidak boleh di bawah 12px.

## Warna buku kas
| Token | Nilai | Kontras/tujuan |
|---|---|---|
| `--color-paper` | `#F7F3EA` | latar hangat |
| `--color-card` | `#FFFDF8` | kartu; 16,48:1 vs ink |
| `--color-ink` | `#14201C` | teks; 15,13:1 |
| `--color-muted` | `#5A635E` | sekunder; 5,61:1 |
| `--color-accent` | `#C2410C` | aksi; 4,68:1 |
| `--color-safe` | `#1F6F4A` | aman; 5,53:1 |
| `--color-warn` | `#8A5300` | hampir habis; 5,72:1 |
| `--color-danger` | `#A02020` | minus; 6,97:1 |

Jangan gunakan gradien ungu, biru template `#0066FF`, atau putih murni sebagai latar utama.

## Bentuk, ruang, dan elevasi
Radius kartu 12px, tombol 10px; spacing kelipatan 4: 4/8/12/16/24/32px. Satu level bayangan hangat: `0 1px 2px rgba(20,32,28,.06), 0 4px 12px rgba(20,32,28,.04)`.

## Motion
Gunakan transisi 180ms `ease-out`; reveal kartu bertahap dengan jarak 40ms. Wajib mematikan transform dan animasi pada `prefers-reduced-motion: reduce`.

## Aksesibilitas non-negotiable
Kontras teks minimal 4,5:1; target sentuh 44×44px; focus-visible outline 3px ink dengan offset 3px; body 16px; font scaling 200%. “Hampir habis” dan “minus” selalu memiliki label teks, bukan warna saja. Form memakai label permanen dan status error diumumkan secara semantik.

## Bukti eksekusi
Arah ini diterapkan pada frame Doop high-fidelity **Beranda — arah visual**, tanpa menimpa frame wireframe untuk usability test. Frame memakai token warna, Plus Jakarta Sans, JetBrains Mono, hierarchy saldo 40px, dan CTA Catat yang kontras.

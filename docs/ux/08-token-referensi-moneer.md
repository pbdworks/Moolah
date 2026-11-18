# Token referensi — canvas `NRSnt05BCx` (Moneer Prototype)

Diekstrak dari canvas Doop `NRSnt05BCx` milik Davaa, frame `aUOdHE_PHM` (Beranda) dan blok token canvas. Ini **sumber kebenaran arah visual Moolah** sampai ada keputusan lain.

Canvas itu bukan milik Moolah — ia prototipe "Moneer" yang Davaa tunjuk sebagai target rasa. Yang diambil bahasanya, bukan identitasnya.

## Palet

| Token | Nilai | Peran |
|---|---|---|
| `--color-ground` | `#E9E3D6` | Latar halaman, kertas-batu hangat. Bukan putih. |
| `--color-surface` | `#FAF6EC` | Kartu, sheet, bar nav |
| `--color-surface-sunken` | `#F1EBDE` | Baris inset, isi input |
| `--color-ink` | `#16211C` | Teks utama, near-black kehijauan |
| `--color-ink-soft` | `#5B665F` | Teks sekunder, label |
| `--color-ink-faint` | `#8A938C` | Teks tersier, hint |
| `--color-line` | `#DAD2C1` | Hairline dan border |
| `--color-pine` | `#0E4E43` | Brand: tombol, tab aktif, header, FAB |
| `--color-pine-deep` | `#082F29` | Kartu gelap, blok berat |
| `--color-pine-tint` | `#DCE8E1` | Chip terpilih, isian hijau lembut |
| `--color-leaf` | `#1F6B4F` | Uang masuk / pemasukan |
| `--color-brick` | `#A84A2F` | Uang keluar / pengeluaran, nominal negatif |
| `--color-brick-tint` | `#F3E0D8` | Isian lembut untuk badge pengeluaran |
| `--color-brass` | `#E3B45C` | Aksen kewajiban, perhatian |
| `--color-brass-tint` | `#F6E8CB` | Isian lembut untuk strip peringatan |

**Aturan peran warna.** Hijau = masuk, bata = keluar, kuningan = kewajiban/perhatian, pine = brand dan aksi. Tidak ada warna dekoratif. Status tidak boleh disampaikan hanya dengan warna — selalu ada label teks.

## Tipografi

Dua keluarga, pembagiannya tegas dan tidak boleh dicampur:

| Token | Nilai | Peran |
|---|---|---|
| `--font-display` | `Fraunces, Georgia, serif` | Judul layar, sapaan, **dan seluruh angka uang** |
| `--font-sans` | `Plus Jakarta Sans, system-ui, sans-serif` | Label, tanggal, nav, teks UI, isi baris |

| Token | Nilai |
|---|---|
| `--text-xs` | `11px` |
| `--text-sm` | `13px` |
| `--text-base` | `15px` |
| `--text-lg` | `17px` |
| `--text-xl` | `21px` |
| `--text-2xl` | `27px` |
| `--text-3xl` | `34px` |

Angka uang memakai `--font-display` pada `--text-3xl` (34px) untuk angka utama dan `--text-lg` (17px) untuk nominal di dalam baris. Ini inti dari arah ini: **angka uang serif, UI sans.** Tanpa itu, desainnya kembali terasa seperti aplikasi fintech generik.

## Bentuk dan ruang

| Token | Nilai |
|---|---|
| `--radius-sm` | `10px` |
| `--radius-md` | `16px` |
| `--radius-lg` | `22px` |
| `--radius-xl` | `28px` |
| `--radius-pill` | `999px` |

| Token | Nilai |
|---|---|
| `--spacing-1` | `4px` |
| `--spacing-2` | `8px` |
| `--spacing-3` | `12px` |
| `--spacing-4` | `16px` |
| `--spacing-5` | `20px` |
| `--spacing-6` | `24px` |
| `--spacing-8` | `32px` |

**Tanpa shadow.** Pemisahan datang dari kontras isian dan hairline `--color-line`, bukan elevasi.

## Kontras terukur

Dihitung dengan rumus WCAG, bukan dikira-kira:

| Pasangan | Rasio | Status |
|---|---|---|
| `--color-ink` di `--color-surface` | 15,34:1 | lulus AA |
| `--color-ink-soft` di `--color-surface` | 5,54:1 | lulus AA |
| `--color-brick` di `--color-surface` | 5,28:1 | lulus AA |
| `--color-pine` di `--color-surface` | 8,89:1 | lulus AA |
| `--color-surface` di `--color-pine-deep` | 13,43:1 | lulus AA |
| `--color-pine-tint` di `--color-pine-deep` | 11,51:1 | lulus AA |
| `--color-surface` di `--color-pine` (FAB) | 9,59:1 | lulus AA |

## Jebakan yang sudah terbukti

**Spesifisitas CSS pada FAB.** `.nav a{color:var(--color-ink-soft)}` (0,1,1) mengalahkan `.fab{color:var(--color-surface)}` (0,1,0) meskipun ditulis belakangan. Akibatnya label FAB jadi `#5B665F` di atas pine — **1,60:1**, praktis tidak terbaca. Perbaikannya `.nav a.fab{color:var(--color-surface)}`.

**Nav fixed menutupi konten.** Frame harus cukup tinggi, atau `main` butuh `padding-bottom` lebih besar dari tinggi nav (82px) plus jarak. `problemCount` di Doop tidak menangkap ini karena nav-nya `fixed`.

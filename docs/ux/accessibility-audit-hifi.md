## Audit ulang aksesibilitas high-fidelity — tiga frame

**Tanggal audit:** 2026-11-18
**Scope:** Doop canvas `lZZDl9Eagd`, frame `rCT31Sro_C` (Sisa Kantong), `NE6vwZLtzZ` (Kantong), dan `QtyerZnq1w` (OCR).
**Metode:** inspeksi HTML frame dan `inspect_frame` setelah revisi terakhir. Kontras tidak diulang. Audit ini tidak menjalankan Tab aktual dengan browser/screen reader, tidak mengemulasikan `prefers-reduced-motion`, dan tidak menguji zoom 200% atau viewport pendek.

### Konfirmasi temuan High sebelumnya

| Temuan sebelumnya | Status audit ulang | Bukti selector/angka | Dampak tersisa |
|---|---|---|---|
| Dua `aria-current="page"` pada Sisa Kantong | **LULUS** | `nav > a:nth-of-type(2)` “Kantong” adalah satu-satunya `[aria-current=page]`; computed `font-weight:700`; Beranda/Riwayat `400` | Tidak ada dua konteks aktif pada markup saat ini. Pengumuman screen reader tetap perlu uji aktual. |
| Indikator dan aktivitas duplikat pada Sisa Kantong | **LULUS** | Satu `.ratio` per Kantong; satu `section.latest` pada y=`683`, tinggi `120px`; tidak ada duplikasi pada HTML | Urutan baca kini Makan → Transport → Aktivitas terbaru → nav; sesuai urutan visual. |
| Progressbar ARIA hilang pada Sisa Kantong | **LULUS** | Makan: `[role=progressbar]`, `aria-valuenow="36"`, min `0`, max `100`, visual `width:36%`; Transport: `90` dan `width:90%`; masing-masing tinggi visual `6px` | Label masih menyebut angka (“36 persen terpakai”/“90 persen terpakai”), sehingga screen reader tertentu dapat mengulang angka bersama value. Ini saran copy, bukan kegagalan semantik. |
| Simpan Kantong self-scroll/tanpa status | **SEBAGIAN — aksi lulus, status belum lulus penuh** | `#buat .cta` sekarang `href="#kantong-aktif"` + `data-doop-action="scroll-to:#kantong-aktif"`; `#kantong-aktif` memiliki `role="status" hidden` | Target tidak lagi self-scroll. Namun elemen yang `hidden` tidak berada di accessibility tree dan tidak dapat mengumumkan status saat tetap tersembunyi. Status sukses hanya akan diumumkan bila implementasi membuka/unhides elemen dan memperbarui teks; belum ada bukti itu terjadi. |
| Aksi pemulihan OCR tanpa grup | **LULUS** | `section[role=group][aria-label="Pemulihan setelah OCR gagal"]`, rect x=`20`, y=`441`, width=`380`, height=`302`; berisi Foto lagi, Pilih foto lain, Isi manual, Batal | Grup kini punya accessible name. Aksi kamera masih berupa link dalam prototipe; pada implementasi gunakan button/file picker. |

### Temuan baru dan catatan wajib

| Frame | Masalah | Bukti | Dampak | Perbaikan yang disarankan | Tingkat |
|---|---|---|---|---|---|
| `NE6vwZLtzZ` — Kantong | Status sukses `hidden` tidak dapat diumumkan dalam keadaan tersembunyi | `section#kantong-aktif[role=status][hidden]`; `inspect_frame` tidak menemukan `[role=status]` atau `#kantong-aktif` sebagai elemen visible | `role=status`/live announcement efektif hanya ketika node tersedia di accessibility tree. Jika node tetap hidden setelah simpan, pengguna screen reader tidak menerima konfirmasi. | Saat simpan berhasil, lepaskan `hidden` terlebih dahulu lalu isi/update teks status; pertahankan `role="status" aria-live="polite" aria-atomic="true"`. Jangan mengandalkan perubahan pada node yang masih hidden. | **High bila implementasi tidak meng-unhide; belum terverifikasi di prototipe** |
| `rCT31Sro_C` — Sisa Kantong | Status urutan baca sudah diperbaiki dan tidak gagal | DOM/visual: panel Makan, panel Transport, `section.latest` “Aktivitas terbaru”, kemudian `nav`; `.latest` rect y=`683–803`, nav y=`907–980` | Aktivitas tidak lagi muncul setelah nav atau tersembunyi di bawah navigasi; pembaca layar mendapat konteks transaksi sebelum nav. | Pertahankan urutan ini. Beri accessible name pada setiap panel bila nanti menjadi region mandiri. | **Lulus inspeksi** |
| `QtyerZnq1w` — OCR | Grup pemulihan kini bernama, tetapi judul visual “OCR gagal?” bukan heading/label terpisah yang dirujuk | `section[role=group][aria-label="Pemulihan setelah OCR gagal"]`; empat link pada y=`482`, `546`, `610`, `674` dengan tinggi `52px` | Accessible name sudah tersedia dari `aria-label`, jadi tidak gagal. Judul visual tidak perlu didengar dua kali. | Pertahankan `aria-label`, atau ganti dengan `aria-labelledby` ke id judul bila markup judul berubah. | **Lulus; saran konsistensi** |

### Form dan field OCR

Pada Kantong, label tetap terhubung dengan benar:

- `label[for="pocket-name"]` → `input#pocket-name`, rect y=`652`, tinggi `48px`.
- `label[for="pocket-limit"]` → `input#pocket-limit`, rect y=`742`, tinggi `48px`, `inputmode="numeric"`.

`inputmode="numeric"` hanya memilih virtual keyboard numerik; pembaca layar tetap memperoleh field textbox bernama “Batas Kantong” dan placeholder “Rp 500.000”. Tidak ada `aria-describedby`, `aria-invalid`, atau error message pada markup saat ini. Itu bukan regresi dari temuan High sebelumnya karena temuan tersebut adalah status simpan, tetapi validasi error tetap harus ditambahkan saat form diimplementasikan.

OCR mempertahankan relasi error: field Total memiliki `aria-invalid="true"` dan `aria-describedby="ocr-help"`, dengan `p#ocr-help` berisi “Koreksi total sebelum menyimpan.” Ini lulus inspeksi semantik. Simpan transaksi berada pada rect y=`360`, tinggi `48px`; grup pemulihan mulai y=`441`, sehingga urutan visual dan DOM konsisten.

### Fokus keyboard dan fixed nav

- `rCT31Sro_C`: CTA “Isi / Pindahkan” y=`316`, “Lihat transaksi” y=`594`, nav y=`907`, tinggi `73px`; tidak ada overlap pada `inspect_frame`.
- `NE6vwZLtzZ`: input `#pocket-name` y=`652`, `#pocket-limit` y=`742`, Simpan y=`802`, aktivitas y=`874–1040`, CTA bawah y=`1128`, nav y=`1227`, tinggi `73px`; `problemCount:0`.
- `QtyerZnq1w`: input Total y=`239`, CTA simpan y=`360`, grup aksi y=`441–743`, nav y=`1027`, tinggi `73px`; `problemCount:0`.

CSS menyediakan `nav a:focus-visible,.cta:focus-visible { outline:3px solid var(--color-ink-new); outline-offset:3px }`. Namun `inspect_frame` tidak memindahkan fokus dan tidak menghasilkan computed style untuk pseudo-class `:focus-visible`. Karena itu urutan Tab dan keterlihatan outline pada nav, CTA, tautan aksi, serta input tetap **BELUM TERVERIFIKASI**. Demikian juga viewport pendek/zoom 200% dan WCAG 2.4.11 pada kondisi tersebut tetap **BELUM TERVERIFIKASI**; tidak boleh dianggap lulus hanya dari `problemCount:0`.

### Reduced motion

Ketiga frame memuat blok:

```css
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{
    animation:none!important;
    transition:none!important;
    transform:none!important
  }
}
```

Struktur CSS mencakup `.pocket`/semua elemen dan pseudo-element, tetapi inspect tidak menyediakan emulasi media preference. Status computed `animation-name`, `transition-duration`, dan `transform` pada `prefers-reduced-motion: reduce` **BELUM TERVERIFIKASI**.

### Kesimpulan dan prioritas

1. **Selesaikan status simpan Kantong:** `hidden` boleh menjadi kondisi awal, tetapi implementasi wajib meng-unhide lalu mengubah teks pada `#kantong-aktif[role=status]` agar live announcement benar-benar terjadi. Ini satu-satunya catatan High yang belum dapat dinyatakan lulus.
2. Progressbar Sisa Kantong sekarang semantik dan angka konsisten: `36% ↔ 36`, `90% ↔ 90`; pertimbangkan label non-numerik bila screen reader mengulang angka.
3. Aksi pemulihan OCR sekarang berada dalam grup bernama dan field Total tetap memiliki relasi error yang valid.
4. Urutan baca Sisa Kantong sudah benar: Aktivitas terbaru berada sebelum nav dan tidak duplikat.
5. Tetap lakukan uji manual Tab/Shift+Tab, screen reader, reduced-motion computed style, viewport pendek, dan zoom 200% sebelum menyatakan audit aksesibilitas selesai.

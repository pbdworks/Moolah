# Referensi desain (pihak ketiga)

Skill desain yang dipakai squad untuk Fase 3. Sumber: **claude-code-templates** oleh Daniel Avila.

- Repo: https://github.com/davila7/claude-code-templates
- Path asal: `cli-tool/components/skills/creative-design/`
- Lisensi: **MIT** — boleh dipakai dan didistribusikan ulang dengan atribusi.

File di sini adalah salinan apa adanya dari sumber, bagian `SKILL.md` dan referensi yang relevan saja. Tidak diubah isinya.

## Kenapa disalin, bukan di-install

Instruksi aslinya memakai `npx claude-code-templates@latest --skill ...`, yang mengunduh paket dan menulis 41 file ke `.claude/skills/`. Kebijakan squad melarang install dependency di VPS, jadi file referensinya diambil langsung dari repo sumber lewat API GitHub dan disimpan di sini. Semua agent yang checkout repo ini bisa membacanya.

## Kapan membaca apa

| File | Baca saat |
|---|---|
| `mobile-design-SKILL.md` | Kerangka utama: prinsip mobile, anti-pattern, platform convention |
| `touch-psychology.md` | Fitts's Law, zona jempol, gestur, ukuran target |
| `mobile-navigation.md` | Tab bar vs stack vs drawer; aturan jumlah tab dan indikator aktif |
| `mobile-typography.md` | Dynamic Type, skala teks, aksesibilitas tipografi |
| `mobile-color-system.md` | Dark mode, OLED, konsumsi baterai |
| `ui-ux-pro-max-SKILL.md` | Daftar periksa UX berbobot: aksesibilitas, touch, performa, layout |

## Yang sudah diterapkan di Moolah

Arah visual Moolah (`06-prinsip-visual.md`) sudah lebih dulu ditetapkan sebelum referensi ini masuk. Referensi ini dipakai untuk **menguji dan mengoreksi**, bukan mengganti arah:

- **Tab bar 3–5 destinasi, label selalu tampil, indikator aktif wajib** — `mobile-navigation.md`. Ini yang mengoreksi nav Moolah yang sebelumnya punya 4 tab tanpa indikator aktif.
- **Target sentuh ≥44pt (iOS) / 48dp (Android), jarak antar target 8–12px** — `mobile-design-SKILL.md`. Moolah memakai 44px; untuk Android target naik ke 48dp.
- **Status tidak boleh hanya warna** — `ui-ux-pro-max-SKILL.md`. Sudah dipenuhi lewat label teks "Hampir habis" / "minus".
- **Focus state wajib terlihat** — `ui-ux-pro-max-SKILL.md`. Sudah dipenuhi lewat `:focus-visible`.

## Catatan

Palet dan tipografi Moolah (Plus Jakarta Sans + JetBrains Mono, palet buku kas) **tidak berasal dari referensi ini** dan tidak boleh diganti hanya karena referensi menawarkan opsi lain. Keduanya dipilih dengan alasan konteks Indonesia dan keterbacaan angka uang.

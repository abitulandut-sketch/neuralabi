# Cara membedah video referensi

## Kalau ada file video di sandbox (code execution aktif)

```bash
python3 scripts/bedah_video.py /path/ke/video.mp4 --out /tmp/bedah
```

Hasilnya:
- `info.txt`: durasi, resolusi, fps, ada audio atau tidak.
- `adegan.txt`: daftar titik potong adegan dengan timecode (deteksi perubahan gambar).
- `frames/adegan_XX.jpg`: satu frame dari tengah tiap adegan.
- `sheet_XX.jpg`: contact sheet (frame tiap 0,5 dtk) dengan timecode di tiap kotak.

Lalu **lihat gambarnya** (buka file jpg) dan baca isi tiap adegan. Kalau deteksi potongan terlalu banyak/sedikit, ulangi dengan `--threshold 0.2` (lebih sensitif) atau `0.45` (kurang sensitif). Untuk video tanpa potongan (satu take panjang), bagi adegan berdasarkan perubahan aksi atau kalimat, kira-kira tiap 3–7 dtk.

Subtitle tertanam: crop area subtitle dan perbesar, mis.
```bash
ffmpeg -i video.mp4 -vf "fps=2,crop=iw:ih*0.25:0:ih*0.6,scale=720:-1,tile=4x6" -frames:v 1 subs.jpg
```
lalu baca teksnya dari gambar untuk mendapat naskah asli.

Kalau ffmpeg tidak ada di sandbox, coba `pip install imageio-ffmpeg` dan pakai binary-nya, atau minta user kirim screenshot.

## Kalau tidak ada file video
- Minta user kirim **screenshot tiap adegan** (atau screen record yang dipotong per adegan) beserta perkiraan detiknya, plus naskah/teks kalau ada.
- Link TikTok/Instagram biasanya tidak bisa dibuka langsung. Jangan mengarang isi video dari judul link.

## Audio
Transkripsi audio sering tidak tersedia. Urutan prioritas naskah:
1. Teks yang di-paste user.
2. Subtitle tertanam yang dibaca dari frame.
3. Rekonstruksi dari visual + gerak bibir + konteks, dan bilang ke user bahwa naskah disusun ulang.

## Yang dicatat per adegan
| Aspek | Contoh |
|---|---|
| Timecode | 0,0–1,5 dtk |
| Shot size & angle | close-up, low angle, POV, over-shoulder |
| Gerak kamera | push-in, orbit, tilt up, handheld, statis, whip |
| Aksi talent | berbalik, menunjuk kamera, merapikan baju |
| Produk | dipakai/dipegang, sisi yang terlihat (→ pilih REF yang cocok) |
| Lokasi & properti | lobby marmer, kamar dengan lampu pink |
| Lighting | softbox kiri, lampu meja hangat, cahaya jendela |
| Transisi | hard cut, fabric wipe, jump cut |
| Teks & suara | overlay, subtitle, VO, dialog |

(Tabel ini hanya untuk catatanmu; jangan dimasukkan ke file hasil.)

## DNA video (untuk MASTER STYLE)
- Hook 1–3 detik pertama: apa yang bikin orang berhenti scroll.
- Gaya: UGC handphone, editorial studio, review, POV, ASMR, before-after.
- Tempo: rata-rata panjang cut.
- Palet: ambil 4–6 warna dominan dan tulis kode hex-nya.
- Kamera: perkiraan lensa (24mm HP, 85mm portrait, 100mm macro), fps, rasio.

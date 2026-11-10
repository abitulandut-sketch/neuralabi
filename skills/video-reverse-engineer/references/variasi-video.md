# Varian video

Tentukan varian dari permintaan user atau dari video referensi. Kalau user bilang "tanpa wording", artinya tidak ada teks di layar (subtitle/overlay), tapi suara tetap boleh.

## A. Tanpa suara (editorial / B-roll / produk)
- MASTER STYLE: "No voice over, no on-screen text, no subtitles, no watermark."
- Tidak ada baris Dialog/Voice over.
- Musik dipilih saat editing, tidak ditulis di prompt (kecuali user minta).
- Cocok untuk: video campaign, cinematic, detail produk, model.
- Contoh: `examples/contoh-editorial-tanpa-suara.md`.

## B. Voice over (talent lipsync, tanpa wording)
- Di tiap adegan, di bawah baris `Kamera:`, tambahkan `Voice over: "..."` (Indonesia). Adegan tanpa suara tulis `Voice over: (diam, hanya ambience)`.
- Di prompt Inggris: "She says in casual Indonesian, with accurate lip-sync: "..."" (pakai teks VO yang sama persis).
- MASTER STYLE tetap memuat "No on-screen text, no subtitles".
- Di akhir file tulis **Naskah voice over lengkap** + 1 baris "Gaya suara" (usia, logat, tempo, kata yang ditekan).
- Panjang kalimat per adegan harus muat di durasinya (kira-kira 2,5–3 kata per detik).
- Contoh: `examples/contoh-review-voice-over.md`.

## C. Talking head (talent bicara langsung ke kamera)
- Baris di adegan: `Dialog: "..."`, dan di prompt Inggris "She says in casual Indonesian, with accurate lip-sync: ...".
- Wajah selalu terlihat, mulut tidak tertutup. Produk dipegang di bawah dagu atau di samping wajah, tidak menutupi mulut.
- Tidak ada teks di layar kecuali diminta.

## D. Dialog 2 orang (mis. orang di balik kamera + talent)
- Tentukan siapa yang terlihat dan siapa yang hanya suara. Tulis di MASTER STYLE: suara siapa, usia, nada.
- Di tiap adegan tulis dialog berurutan: baris pembicara off-camera dulu, lalu jawaban talent.
- Di prompt Inggris tambahkan: "<Nama> is never seen on screen, only heard; the <talent>'s mouth stays closed while <Nama> speaks."
- Tulis naskah lengkap per adegan di akhir untuk cek lipsync.
- Catatan cadangan: kalau generator hanya bisa satu suara, suara kedua direkam terpisah dan ditempel saat editing.
- Contoh: `examples/contoh-talking-head-dialog.md`.

## Penutup (semua varian)
- Default: adegan CTA dengan logo brand (Image N) di tengah, produk di belakangnya, lalu cut ke hitam dengan logo.
- Varian review/UGC boleh ditutup dengan produk + kemasan di meja lalu cut ke hitam.
- Talking head boleh ditutup talent mengajak checkout ("langsung cek keranjang, ya!") lalu hold senyum.
- Ganti end card toko di video asli (QR, harga, nama toko lain) dengan penutup di atas.

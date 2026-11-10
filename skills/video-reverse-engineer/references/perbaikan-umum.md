# Masalah umum hasil generate & kalimat pengamannya

Tambahkan pengaman ini langsung ke MASTER STYLE / Deskripsi produk / prompt adegan bila relevan, dan tulis catatan perbaikan di akhir file.

## Logo atau tulisan salah eja
AI sering salah mengeja logo (contoh nyata: "TULANDUT" jadi "TULANDOT").
- Upload logo PNG sebagai Image N sendiri (REF-LOGO).
- Eja huruf per huruf di prompt: `logo "TULANDUT" spelled T-U-L-A-N-D-U-T, never TULANDOT`. Sebut juga ciri font kalau unik (mis. "letter A without crossbar").
- Kalau tetap salah, generate tanpa logo dan tempel logo PNG saat editing (blend Screen).

## Warna produk yang dipakai di balik baju berubah
Contoh nyata: bra nude muncul hitam dan tembus di balik kaos putih.
- Di MASTER STYLE, Talent, dan tiap adegan: "the <product> worn under the top is the same <nude/ivory> color as Image N, never black or dark, invisible through the opaque top, neckline closed".
- Hindari baju putih tipis; pilih baju opaque.

## Produk harus tersembunyi tapi malah terlihat
Untuk konten "nggak kelihatan pakai apa-apa" (seamless, invisible):
- "HIDDEN <PRODUCT>, NOT VISIBLE. no outline, no lines, no straps peeking, no see-through fabric, fully opaque top".

## Outfit berubah antar adegan
- Upload foto outfit sebagai Image N (REF-OUTFIT), sebut di baris Referensi dan prompt tiap adegan.
- "Outfit exactly as Image N, the outfit never changes between scenes. KEEP OUTFIT DETAIL."

## Wajah talent berubah
- Pakai character reference sheet sebagai Image N (REF-FACE) di setiap adegan yang ada wajahnya.
- Tulis ciri wajah/rambut yang sama persis di bagian Talent dan tutup dengan "KEEP FACE IDENTITY".

## Detail produk hilang/berubah
- Sebut detail konstruksi yang khas secara spesifik (jumlah baris kait, jumlah tingkat adjuster, bahan, tekstur).
- Pakai foto close-up sebagai REF tersendiri dan sebut di adegan macro.
- "KEEP PRODUCT DETAIL exactly as Image ...".

## Lipsync salah / orang yang salah bicara
- Tulis teks dialog yang sama persis di baris adegan dan di prompt Inggris, tambahkan "with accurate lip-sync".
- Untuk suara off-camera: "<Nama> is off-screen, voice only; the talent's mouth stays closed while <Nama> speaks."
- Kalau nama brand salah diucapkan, tulis ejaan bunyi di dialog (mis. "Tu-lan-dut") tanpa teks di layar.

## Muncul teks/subtitle yang tidak diminta
- "No on-screen text, no subtitles, no captions, no watermark" di MASTER STYLE dan, kalau perlu, di akhir prompt adegan.

## Konten ditolak/terlalu vulgar (produk pakaian dalam)
- "tasteful, ad-safe, non-sexualized, no nudity", framing dada ke atas atau produk dipegang, atau talent memakai produk di balik/bersama outfit.

# Format prompt video (template baku)

Salin kerangka di bawah, ganti isi dalam `<...>`. Bagian bertanda (opsional) dipakai hanya jika relevan.

````markdown
# Prompt Video <Nama Produk> <BRAND> (<Generator, mis. TikTok Symphony>)

Rekonstruksi dari video referensi (<durasi> dtk, <rasio>, <fps>). <Ringkasan gaya: UGC/editorial/review, lokasi, siapa talent, tempo cut>. <Apa yang diubah dari video asli>. <Varian: tanpa voice over, tanpa teks di layar / dengan voice over (lipsync), tanpa wording / talking head / dialog 2 orang>.

**Urutan upload foto ke <Generator> (Image N):**
- Image 1 = <nama file> (REF-FRONT)
- Image 2 = <nama file> (REF-BACK)
- Image 3 = <nama file> (REF-SIDE)
- Image 4 = <nama file> (REF-FACE, talent)
- Image 5 = <nama file> (REF-LOGO)

---

## Master style

MASTER STYLE: <gaya render & genre>, <tasteful/ad-safe bila perlu>. <Lokasi + properti + warna dengan hex (#xxxxxx)>. Palette: <warna kulit, warna produk, warna outfit, warna background dengan hex>. <Lighting: key, fill, rim, sumber cahaya>. <Kamera: lensa mm, depth of field, gerak kamera (push-in, orbit, handheld)>. <Tempo cut & transisi>. <Suara: no voice / Indonesian voice with lip-sync / two voices>. Vertical 9:16, 4K, <25/30>fps, photorealistic. No on-screen text, no subtitles, no watermark, no other brand logos.

**Deskripsi produk (konsisten di semua prompt):** <Nama produk BRAND>: <warna, bahan, finishing, bentuk, detail konstruksi, aksesori, logo/tulisan beserta ejaan>. KEEP PRODUCT DETAIL exactly as Image 1, Image 2, Image 3.

**Talent (konsisten di semua prompt):** the same <usia/ciri> from the character reference sheet (Image 4) in every scene: <kulit, wajah, makeup, rambut>. Outfit: <outfit, atau "exactly as Image N (REF-OUTFIT)">. KEEP FACE IDENTITY.

---

## Adegan per adegan

### Adegan 1 — <Nama adegan> (0,0–<x,x> dtk)
Referensi: REF-<A> (Image <n>) + REF-<B> (Image <m>). <Apa yang terjadi di adegan, 1–2 kalimat Indonesia>.
Kamera: <shot size, angle, gerak kamera>.
<(opsional) Voice over: "..."  atau  Dialog: "...">

[MASTER STYLE]. <Prompt Inggris: subjek + Image N, aksi, produk + Image N, framing, gerak kamera, lighting khusus, dialog/VO dengan "with accurate lip-sync" bila ada>. <Kunci: KEEP PRODUCT DETAIL / KEEP FACE IDENTITY / KEEP LOGO DETAIL>.

<(opsional) Teks overlay: "..." (ditambahkan saat editing)>
<(opsional) Logo: <posisi>, blend Screen, KEEP LOGO DETAIL>

### Adegan 2 — ...

### Adegan <terakhir> — CTA logo (<x,x>–<durasi> dtk)
Referensi: REF-LOGO (Image <n>) + REF-FRONT (Image 1). Logo brand di tengah frame, produk di belakangnya (blur lembut), lalu cut ke hitam dengan logo.
Kamera: statis atau slow push-in, hold di akhir.

[MASTER STYLE]. <Logo BRAND exactly as Image n, centered, floating in front of the softly blurred product (Image 1); spell the logo letter by letter if needed>. Hold, then cut to black with the logo. KEEP LOGO DETAIL.

---

<(opsional) **Naskah lengkap / voice over** untuk cek lipsync, nomor per adegan.>

<(opsional) Catatan perbaikan: kalimat tambahan kalau hasil generate melenceng. Lihat perbaikan-umum.md.>
````

## Aturan per bagian

**Timecode**: format Indonesia pakai koma desimal, `(0,0–2,5 dtk)`. Adegan harus menyambung tanpa celah dan total sama dengan durasi target. Ikuti tempo video asli (cut cepat 0,5–2 dtk untuk editorial, 2–7 dtk untuk talking head). Kalau generator membatasi durasi per klip (mis. maksimal 5–10 dtk), boleh gabung beberapa cut asli jadi satu adegan dan sebutkan.

**Baris Referensi**: selalu bahasa Indonesia, format `REF-XXX (Image N)`, gabungkan dengan `+`. Pilih referensi yang benar-benar terlihat di adegan itu (detail strap → REF-STRAP, wajah → REF-FACE).

**Prompt Inggris**: selalu diawali `[MASTER STYLE].`. Sebut Image N setiap kali menyebut produk, talent, logo, atau outfit. Jelaskan dengan kata kerja yang jelas apa yang bergerak (talent, produk, kamera). Akhiri dengan kunci `KEEP ... DETAIL` / `KEEP FACE IDENTITY` yang relevan.

**Overlay & logo**: teks overlay dan logo yang ditempel saat editing (bukan di-generate) ditulis terpisah di bawah prompt sebagai catatan editing. Logo PNG ditempel dengan blend mode **Screen**, catat `KEEP LOGO DETAIL`. Kalau user minta "tanpa wording", jangan ada overlay sama sekali dan pastikan MASTER STYLE berisi "No on-screen text, no subtitles".

**Durasi & jumlah adegan**: samakan dengan video referensi kecuali user minta lain.

## Checklist sebelum kirim
- [ ] Urutan Image N sesuai urutan upload, dan setiap Image N yang disebut memang ada di daftar.
- [ ] MASTER STYLE memuat palet hex, lighting, lensa, rasio 9:16, 4K, fps, dan larangan teks/watermark/logo lain.
- [ ] Deskripsi produk diambil dari foto, nama produk benar, ditutup KEEP PRODUCT DETAIL.
- [ ] Setiap adegan: judul + timecode, Referensi (Image N), Kamera, prompt diawali `[MASTER STYLE].`.
- [ ] Timecode menyambung dan totalnya pas.
- [ ] Dialog/VO ada di baris adegan **dan** di dalam prompt Inggris (dengan "accurate lip-sync").
- [ ] Logo yang muncul di produk dieja huruf per huruf bila AI sering salah eja.
- [ ] Adegan penutup CTA logo (atau sesuai permintaan user).
- [ ] Pengaman dari perbaikan-umum.md yang relevan sudah ditambahkan.
- [ ] Tidak ada tabel atau bagian tambahan yang tidak diminta.

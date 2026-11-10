---
name: video-reverse-engineer
description: Bedah (reverse engineer) video atau konten referensi adegan per adegan, lalu tulis ulang jadi prompt video AI siap tempel ke TikTok Symphony, Veo, Kling, dsb. dengan format MASTER STYLE, Deskripsi produk, Adegan per adegan + timecode, Referensi Image N, dan prompt Inggris. Pakai saat user kirim video/link/screenshot konten dan minta "reverse engineer", "bedah video", "tiru video ini", "bikin prompt video kayak gini", atau minta prompt video produk.
---

# Video Reverse Engineer → Prompt Video AI

Skill ini mengubah video atau konten referensi (TikTok, Reels, iklan) menjadi **prompt video AI per adegan** untuk produk milik user. Hasil akhirnya satu file Markdown yang bisa ditempel adegan per adegan ke generator video (utamanya **TikTok Symphony**), dengan foto produk/talent dilampirkan sebagai Image 1, Image 2, dst.

Bahasa: tulis penjelasan untuk user dalam **bahasa Indonesia santai**. Prompt untuk AI video ditulis dalam **bahasa Inggris**. Dialog/voice over tetap bahasa Indonesia (kecuali user minta lain).

## Alur kerja

### 1. Kumpulkan bahan
Pastikan ada (tanyakan sekali saja yang belum ada, jangan berulang-ulang):
- **Video/konten referensi**: file video, link, atau screenshot per adegan. Kalau user hanya kasih link dan kamu tidak bisa membukanya, minta file videonya atau screenshot tiap adegan.
- **Foto yang akan di-upload ke generator** (produk tampak depan/belakang/samping/detail, character sheet talent, logo, outfit, kemasan). Urutan upload menentukan nomor Image N.
- **Nama produk + brand** yang benar, dan **varian video**: tanpa suara, voice over, talking head, atau dialog 2 orang (lihat `references/variasi-video.md`).
- Perubahan dari video asli (misal: ganti kemasan, ganti outfit, buang end card toko, ganti durasi).

Kalau ada yang belum jelas tapi bisa ditebak, jalan dulu dengan tebakan paling masuk akal dan tulis asumsinya di bagian atas file.

### 2. Bedah video referensi
Ikuti `references/cara-bedah-video.md`. Ringkasnya:
- Kalau file video ada di sandbox, jalankan `scripts/bedah_video.py <video>` untuk durasi, titik potong adegan (timecode), dan contact sheet frame. Lihat gambarnya untuk membaca isi tiap adegan.
- Catat per adegan: timecode mulai–selesai, apa yang terjadi, framing/angle, gerak kamera, gerak talent, properti, lighting, transisi, teks di layar, dan dialog/VO.
- Kalau video ada subtitle tertanam, baca subtitle dari frame untuk dapat naskah aslinya. Kalau tidak ada dan audio tidak bisa ditranskrip, susun ulang naskah dari visual dan bilang ke user.
- Tarik "DNA" videonya: hook, tempo cut, gaya (UGC/editorial/review), palet warna (kode hex), lokasi, lensa, fps, rasio.

### 3. Petakan foto ke Image N
Nomori foto sesuai **urutan upload user ke generator**: Image 1 = foto pertama. Video tidak ikut dihitung. Beri label REF-xxx (REF-FRONT, REF-BACK, REF-SIDE, REF-STRAP, REF-FACE, REF-LOGO, REF-OUTFIT, REF-BOX, dll). Tulis pemetaan ini sekali di atas file.

### 4. Tulis prompt dengan format baku
Format wajib ada di `references/format-prompt.md`. Urutannya:
1. Judul + 1–2 paragraf ringkasan rekonstruksi (Indonesia): sumber, durasi, gaya, apa yang diubah, varian (tanpa wording / VO / dialog).
2. **Urutan upload foto (Image N)**.
3. **Master style**: satu paragraf Inggris diawali `MASTER STYLE:` berisi gaya render, lokasi, palet dengan kode hex, lighting, kamera/lensa, gerak kamera, tempo cut, rasio 9:16, 4K, fps, photorealistic, dan larangan (no on-screen text, no watermark, no other brand logos).
4. **Deskripsi produk (konsisten di semua prompt)**: deskripsi detail produk dari foto, ditutup `KEEP PRODUCT DETAIL exactly as Image ...`. Teks ini sama persis di semua prompt.
5. **Talent/Model (konsisten di semua prompt)** jika ada orang: wajah dari character sheet (Image N), rambut, makeup, outfit. Tutup dengan `KEEP FACE IDENTITY`.
6. **Adegan per adegan**: tiap adegan berisi judul + timecode, baris `Referensi:` (Indonesia, sebut REF + Image N), deskripsi singkat aksi, baris `Kamera:`, baris Dialog/Voice over bila ada, lalu prompt Inggris yang **diawali `[MASTER STYLE].`**.
7. Catatan overlay/logo per adegan bila ada (`Teks overlay:` dan `Logo: ... KEEP LOGO DETAIL`), lalu naskah lengkap (kalau ada suara) dan catatan perbaikan di akhir.

Adegan terakhir biasanya CTA: logo brand (Image N) di tengah dengan produk di belakangnya, lalu cut ke hitam dengan logo. Ganti end card toko (QR, harga) di video asli dengan adegan logo ini.

### 5. Cek kualitas sebelum kirim
Jalankan checklist di `references/format-prompt.md` (bagian "Checklist sebelum kirim") dan tambahkan pengaman dari `references/perbaikan-umum.md` yang relevan (ejaan logo, warna produk yang dipakai di balik baju, outfit terkunci, produk tersembunyi, dsb.).

### 6. Kirim hasil
Simpan sebagai file `.md` dengan nama `<brand>-<produk>-<varian>-video-prompt.md` dan berikan ke user. Di chat, cukup ringkas: berapa adegan, total durasi, urutan upload foto, dan asumsi yang kamu ambil.

## Aturan penting
- Tiap adegan harus bisa ditempel **berdiri sendiri** ke generator: makanya tiap prompt diawali `[MASTER STYLE].` dan menyebut Image N yang dipakai.
- Selalu sebut Image N di samping setiap referensi, baik di baris Referensi maupun di prompt Inggris.
- Deskripsikan produk **dari foto yang dikirim di permintaan itu**, jangan dari ingatan. Konfirmasi nama produk kalau ragu.
- Ringkas: tanpa tabel, tanpa bagian audio/workflow terpisah, kecuali user minta.
- Konten pakaian dalam/produk tubuh: tetap tasteful dan ad-safe (no nudity, non-sexualized).
- Jangan menjiplak merek, logo, atau wajah orang di video referensi. Yang ditiru adalah struktur, tempo, angle, dan gaya, bukan identitas kreator atau brand lain.
- Contoh lengkap ada di folder `examples/`. Isinya brand TULANDUT dan hanya contoh gaya, jangan dipakai untuk produk lain.

## File di skill ini
- `references/format-prompt.md`: template lengkap + checklist.
- `references/variasi-video.md`: aturan varian tanpa suara, voice over, talking head, dialog 2 orang.
- `references/cara-bedah-video.md`: cara membedah video (dengan atau tanpa file).
- `references/perbaikan-umum.md`: masalah yang sering muncul di hasil generate dan kalimat pengamannya.
- `scripts/bedah_video.py`: deteksi potongan adegan + contact sheet (butuh ffmpeg).
- `examples/`: 3 contoh prompt jadi (editorial tanpa suara, review voice over, talking head dialog).

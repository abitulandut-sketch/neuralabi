# neuralabi

Framework untuk menganalisa dokumen yang terdaftar di sheet Lark (daily, weekly, monthly),
dibuka lewat Chrome profile yang sudah login.

## Alur
1. Buka Chrome profile (Playwright, `launch_persistent_context`).
2. Buka tiap sheet Lark, select all + copy, baca clipboard sebagai tabel.
3. Ambil semua link dokumen di tiap baris, buka, ambil teksnya.
4. Analisa dengan Claude (prompt di `neuralabi/analyze.py`).
5. Tulis laporan Markdown ke `reports/`.

## Cara pakai
```bash
pip install -r requirements.txt
cp config.example.yaml config.yaml   # isi path Chrome profile
export ANTHROPIC_API_KEY=...
# Tutup Chrome dulu (profile tidak bisa dibuka dua proses sekaligus)
python run.py --only daily --dry-run   # cek sheet terbaca
python run.py --only daily --limit 3   # analisa 3 baris pertama
python run.py                          # semua sheet
```

Catatan: Chrome versi baru menolak automasi pada folder profile default. Kalau gagal,
salin folder `User Data` ke lokasi lain (atau buat profile khusus, login Lark sekali)
lalu arahkan `user_data_dir` ke salinan itu.

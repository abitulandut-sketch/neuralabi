"""Analyze a document's text with Claude."""
import anthropic

DEFAULT_PROMPT = """Kamu adalah analis laporan. Analisa dokumen berikut ({period}).
Berikan dalam Bahasa Indonesia:
1. Ringkasan singkat (maks 5 poin)
2. Angka/metrik penting yang disebut
3. Masalah atau risiko yang terlihat
4. Rekomendasi tindak lanjut

Info baris di sheet:
{row}

Isi dokumen:
{text}
"""


def analyze(text: str, row: dict, period: str, model: str, prompt: str = DEFAULT_PROMPT) -> str:
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt.format(period=period, row=row, text=text)}],
    )
    return "".join(b.text for b in msg.content if b.type == "text")

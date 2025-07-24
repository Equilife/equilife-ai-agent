# Equilife AI Agent

## Instalasi

1. **Buat virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Aktifkan virtual environment:**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependency utama:**
   ```bash
   pip install google-adk
   ```

4. **Buat file `.env` di dalam folder agent** (misal: `nutritional_coach_agent/.env` atau `workout_agent/.env`)

   Isi file `.env` dengan:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
   ```

## Menjalankan Project

- Untuk menjalankan dev UI, gunakan perintah berikut:
  ```bash
  adk web
  ```

- Untuk menjalankan local FastAPI server (uji cURL lokal sebelum deploy):
  ```bash
  adk api_server
  ```

## Catatan Penting
- **Jangan upload file `.env` dan `.venv/` ke repository.**
- Simpan konfigurasi rahasia di file `.env` (sudah di-ignore oleh git).
- Untuk menambah dependensi lain, gunakan `pip install <package>` lalu update `requirements.txt` dengan `pip freeze > requirements.txt` jika diperlukan.

---

Silakan sesuaikan instruksi di atas sesuai kebutuhan project Anda. 
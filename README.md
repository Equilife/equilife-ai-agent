# Equilife AI Agent

## Instalasi

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/Equilife/equilife-ai-agent.git
   cd equilife-ai-agent
   ```

2. **Buat virtual environment (opsional tapi direkomendasikan):**
   ```bash
   python -m venv .venv
   ```

3. **Aktifkan virtual environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   > Pastikan ada file `requirements.txt` atau `pyproject.toml` di repo ini. Jika belum ada, tambahkan sesuai kebutuhan project Anda.
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Project

- Jalankan agent sesuai kebutuhan, misal:
  ```bash
  python -m nutritional_coach_agent.agent
  python -m workout_agent.agent
  ```

## Catatan Penting
- **Jangan upload file `.env` dan `.venv/` ke repository.**
- Simpan konfigurasi rahasia di file `.env` (sudah di-ignore oleh git).
- Untuk menambah dependensi, gunakan `pip install <package>` lalu update `requirements.txt` dengan `pip freeze > requirements.txt`.

---

Silakan sesuaikan instruksi di atas sesuai kebutuhan project Anda. 
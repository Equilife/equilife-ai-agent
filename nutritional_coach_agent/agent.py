import json
from typing import Dict, Any, List

# Impor library Agent dari Google ADK
# Pastikan Anda sudah menginstal ADK: pip install google-adk
from google.adk.agents import Agent

# Definisikan tipe data untuk user_profile agar lebih mudah dibaca
UserProfile = Dict[str, Any]

def saran_gizi(user_profile: UserProfile) -> Dict[str, Any]:
    """
    Memberikan saran gizi dan rekomendasi makanan berdasarkan data pengguna.

    Args:
        user_profile (UserProfile): Data lengkap pengguna termasuk data diri,
                                    kesehatan, dan tujuan.

    Returns:
        Dict[str, Any]: Sebuah dictionary berisi status dan saran makanan.
    """
    try:
        # --- Logika Analisis Gizi Sederhana ---
        # Di sini Anda bisa menambahkan logika yang lebih kompleks.
        # Contoh: Menghitung Kebutuhan Kalori Harian (BMR * Faktor Aktivitas)
        # BMR (Basal Metabolic Rate) dengan rumus Harris-Benedict (contoh sederhana)
        berat = user_profile["data_diri"]["berat"]
        tinggi = user_profile["data_diri"]["tinggi"]
        usia = user_profile["data_diri"]["usia"]
        jenis_kelamin = user_profile["data_diri"]["jenis_kelamin"]
        goal = user_profile["kesehatan"]["goal_jangka_panjang"]

        kalori_harian = 0
        if jenis_kelamin.lower() == "pria":
            bmr = 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia)
        else: # Wanita
            bmr = 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia)

        # Faktor aktivitas (contoh kasar)
        aktivitas_harian = user_profile["olahraga"]["aktivitas_harian"].lower()
        if "duduk" in aktivitas_harian:
            kalori_harian = bmr * 1.2
        else:
            kalori_harian = bmr * 1.5

        # Penyesuaian kalori berdasarkan tujuan
        if "menurunkan berat" in goal.lower():
            kalori_harian -= 500
        elif "menambah berat" in goal.lower():
            kalori_harian += 500

        # --- Membuat Rekomendasi Makanan ---
        # Ini adalah contoh rekomendasi statis. Idealnya, ini bisa ditenagai oleh
        # model lain atau database gizi yang lebih besar.
        rekomendasi = {
            "target_kalori_harian": round(kalori_harian),
            "pesan": f"Berdasarkan data Anda, untuk mencapai tujuan '{goal}', target kalori harian Anda adalah sekitar {round(kalori_harian)} kkal.",
            "saran_menu": {
                "sarapan (07:00)": "Oatmeal dengan buah-buahan dan segelas susu rendah lemak. (sekitar 400 kkal)",
                "makan_siang (12:30)": "Nasi merah, dada ayam panggang, tumis brokoli dan wortel. (sekitar 600 kkal)",
                "makan_malam (19:00)": "Ikan salmon panggang dengan ubi jalar dan salad sayuran hijau. (sekitar 500 kkal)",
                "camilan": "Yogurt Yunani atau segenggam kacang almond jika merasa lapar."
            }
        }

        return {
            "status": "success",
            "saran": rekomendasi
        }
    except KeyError as e:
        return {
            "status": "error",
            "error_message": f"Data pengguna tidak lengkap. Kolom yang hilang: {e}"
        }


def saran_aktivitas(user_profile: UserProfile) -> Dict[str, Any]:
    """
    Memberikan saran aktivitas fisik/olahraga dalam format JSON.

    Args:
        user_profile (UserProfile): Data lengkap pengguna.

    Returns:
        Dict[str, Any]: Status dan output JSON berisi jadwal aktivitas.
    """
    try:
        preferensi = user_profile["olahraga"]["preferensi_jenis"]
        tujuan = user_profile["olahraga"]["tujuan_olahraga"]

        # --- Logika Pembuatan Jadwal ---
        # Logika ini bisa dibuat lebih pintar, misalnya menghindari jadwal bentrok
        # atau menyesuaikan dengan preferensi hari.
        jadwal_saran = []
        if not preferensi:
            # Jika tidak ada preferensi, berikan saran umum
            preferensi = ["Jalan cepat", "Yoga", "Latihan kekuatan ringan"]

        # Contoh sederhana pembuatan jadwal 3x seminggu
        jadwal_saran.append({"hari": "Senin", "jam": "17:00", "aktivitas": preferensi[0 % len(preferensi)], "durasi_menit": 45, "catatan": f"Fokus untuk {tujuan}"})
        jadwal_saran.append({"hari": "Rabu", "jam": "07:00", "aktivitas": preferensi[1 % len(preferensi)], "durasi_menit": 30, "catatan": "Lakukan sesuai kemampuan."})
        jadwal_saran.append({"hari": "Jumat", "jam": "17:00", "aktivitas": preferensi[2 % len(preferensi)], "durasi_menit": 60, "catatan": "Tantang diri Anda sedikit lebih keras hari ini."})


        output_json = json.dumps(jadwal_saran, indent=4)

        return {
            "status": "success",
            "jadwal_json": output_json
        }
    except KeyError as e:
        return {
            "status": "error",
            "error_message": f"Data pengguna tidak lengkap. Kolom yang hilang: {e}"
        }

# --- Inisialisasi Agent ---
root_agent = Agent(
    name="nutritional_coach_agent",
    model="gemini-1.5-flash", # Anda bisa menggunakan model Gemini yang sesuai
    description="Agent yang berperan sebagai asisten gizi dan kebugaran virtual.",
    instruction=(
        "Anda adalah asisten virtual ahli gizi dan pelatih kebugaran. "
        "Tugas utama Anda adalah:\n"
        "1. Menjawab pertanyaan umum seputar makanan, gizi, dan olahraga.\n"
        "2. Jika pengguna memberikan data profilnya, gunakan tool `saran_gizi` untuk memberikan rekomendasi menu makanan.\n"
        "3. Jika pengguna memberikan data profilnya, gunakan tool `saran_aktivitas` untuk membuat jadwal olahraga.\n"
        "Selalu berikan jawaban yang mendukung, jelas, dan aman."
    ),
    # Daftarkan fungsi Anda sebagai 'tools' yang bisa digunakan oleh agent
    tools=[saran_gizi, saran_aktivitas],
)
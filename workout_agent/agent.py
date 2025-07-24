import json
from typing import List, Dict, Any
from google.adk.agents import Agent

def generate_workout_plan(workout_goal: str, weekly_activity: List[str]) -> Dict[str, Any]:
    """
    Membuat jadwal olahraga, pengingat, dan target berdasarkan tujuan dan
    preferensi aktivitas pengguna.

    Args:
        workout_goal (str): Tujuan olahraga yang diinginkan pengguna (misal: "Menurunkan berat 5 kg").
        weekly_activity (List[str]): Daftar aktivitas/olahraga yang disukai pengguna.

    Returns:
        Dict[str, Any]: Sebuah dictionary yang berisi jadwal, pengingat, dan target.
    """
    # --- Logika Cerdas untuk Membuat Jadwal ---
    
    # 1. Membuat Jadwal (schedule)
    schedule = []
    # Ambil 3 hari standar untuk berolahraga
    workout_days = ["Monday", "Wednesday", "Friday"] 
    for i, day in enumerate(workout_days):
        # Gunakan aktivitas yang diberikan pengguna, putar kembali jika daftarnya lebih pendek
        activity = weekly_activity[i % len(weekly_activity)] if weekly_activity else "Latihan Kardio"
        schedule.append({
            "days": day,
            "hours": "17:00", # Waktu default, bisa dibuat lebih dinamis
            "activity_suggestion": activity
        })

    # 2. Menentukan Pengingat (workout_reminder)
    workout_reminder = 30 # Default 30 menit sebelum jadwal

    # 3. Menentukan Target (target)
    target = {"metrics": "session", "value": 3} # Default target
    goal_lower = workout_goal.lower()

    if "menurunkan berat" in goal_lower or "kg" in goal_lower:
        target = {"metrics": "kg", "value": 5} # Contoh value
    elif "lari" in goal_lower or "jarak" in goal_lower:
        target = {"metrics": "km", "value": 5}
    elif "konsisten" in goal_lower or "sesi" in goal_lower:
        target = {"metrics": "session", "value": len(schedule)}

    # Gabungkan semua menjadi satu objek untuk di-return
    generated_plan = {
        "schedule": schedule,
        "workout_reminder": workout_reminder,
        "target": target
    }

    return generated_plan

# --- Inisialisasi Agent ---
root_agent = Agent(
    name="workout_planner_agent",
    model="gemini-1.5-flash",
    description="Agent untuk membuat jadwal olahraga, pengingat, dan target yang dipersonalisasi.",
    instruction=(
        "Anda adalah asisten perencana kebugaran. Tugas Anda adalah menerima tujuan "
        "olahraga dan daftar aktivitas yang disukai dari pengguna, lalu menggunakan tool "
        "`generate_workout_plan` untuk menghasilkan jadwal terstruktur dalam format JSON. "
        "Jangan menjawab dengan narasi, langsung panggil tool dan kembalikan hasilnya."
    ),
    tools=[generate_workout_plan],
)